import subprocess
f = open("result.log", "w", encoding="utf-8")
# WIN: command = ["dir"]
command = ["ls", "-al"]
# WIN: shell = True
result = subprocess.run(command,
                        stdout=f)
f.close()