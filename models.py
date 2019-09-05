from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    # 可以創建不存在的欄位
    phones = relationship("Phone", backref="student")

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    number = Column(String(64))
    student_id = Column(Integer, ForeignKey("students.id"))

    def __repr__(self):
        return self.number

    def __str__(self):
        return self.number

if __name__ == "__main__":
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    dn = os.path.dirname(__file__)
    fn = "sqlite:///" + os.path.join(dn, "data.sqlite")
    engine = create_engine(fn, echo=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    S = sessionmaker(bind=engine)
    session = S()
    # 增加
    ps = [Phone(number="0912345678"),
          Phone(number="0911111111")]
    s1 = Student(name="Elwing", phones=ps)
    session.add(s1)

    session.commit()
    # 查詢
    q = session.query(Student).filter_by(name="Elwing")
    # first: 拿第一個, all: 拿全部
    student = q.first()
    print("查到的學生:", student)
    print("這學生的電話:", student.phones)
    for p in student.phones:
        print("電話:", p)
        print("學生:", p.student)
