from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    mobiles = relationship("Mobile", backref="student")

    def __str__(self):
        return "[Name]:" + self.name

class Mobile(Base):
    __tablename__ = "mobiles"
    id = Column(Integer, primary_key=True)
    number = Column(String(32))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __str__(self):
        return "[Mobile]:" + self.number

if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    dirname = os.path.dirname(__file__)
    fn = "sqlite:///" + os.path.join(dirname, "data.sqlite")
    engine = create_engine(fn, echo=False)
    # 先把舊的資料庫刪除 建立新的table
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # 在開始做任何操作前都要init一個Session
    Session = sessionmaker(bind=engine)
    s = Session()

    # 你所有操作
    # 加入(List,虛擬欄位)
    phones = [Mobile(number="0912345678"),
              Mobile(number="0956781222"),
              Mobile(number="0922222222")]
    s1 = Student(name="Elwing", mobiles=phones)
    s.add(s1)
    # 查詢
    student_list = s.query(Student).filter_by(name="Elwing")
    for student in student_list:
        print(student)
        for mobile in student.mobiles:
            print(mobile)
            print("手機持有人:", mobile.student)

    # 結束所有事情, 記得commit
    s.commit()