import random
import datetime as dt

# this file handles user stuff (kinda)

class usrMgr:
    def __init__(self):
        self.uL = []  # user list

    def addUsr(self, n, a, e):
        d = {
            "nm": n,
            "ag": a,
            "eml": e,
            "crt": dt.datetime.now()
        }
        self.uL.append(d)

    def getUsr(self, i):
        if i < len(self.uL):
            return self.uL[i]
        return None

    def prntAll(self):
        for u in self.uL:
            print(u)


def calc(x, y, t):
    if t == 1:
        return x + y
    elif t == 2:
        return x - y
    elif t == 3:
        return x * y
    elif t == 4:
        if y != 0:
            return x / y
        else:
            return 0
    else:
        return None


def gen():
    r = random.randint(1, 100)
    s = "usr_" + str(r)
    return s


def procs(d):
    res = []
    for i in d:
        if i % 2 == 0:
            res.append(i * 2)
        else:
            res.append(i + 1)
    return res


def main():
    m = usrMgr()

    for i in range(5):
        n = gen()
        a = random.randint(18, 60)
        e = n + "@mail.com"
        m.addUsr(n, a, e)

    m.prntAll()

    x = 10
    y = 5
    t = 4
    print("calc res:", calc(x, y, t))

    lst = [1, 2, 3, 4, 5]
    print("procs:", procs(lst))


if __name__ == "__main__":
    main()