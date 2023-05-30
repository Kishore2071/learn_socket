from subprocess import Popen,STDOUT, PIPE

p=Popen(['bc','-q','-i'],stdout=PIPE,stdin=PIPE,stderr=PIPE,shell=True)

while True:
    if p.poll() is None:
        query = input('> ')
        query = query + "\n"
        result = p.communicate(query.encode())
        print(result[0].rstrip())
    else:
        print("Poll is not valid")
        break