import os
import time
import json as js

# handles file data or something idk

class dataHndlr:
    def __init__(self, pth):
        self.p = pth
        self.fls = []

    def loadFls(self):
        for f in os.listdir(self.p):
            if ".txt" in f:
                self.fls.append(f)

    def rd(self, fN):
        try:
            f = open(self.p + "/" + fN, "r")
            d = f.read()
            f.close()
            return d
        except:
            return ""

    def wrt(self, fN, d):
        try:
            f = open(self.p + "/" + fN, "w")
            f.write(d)
            f.close()
        except Exception as e:
            print("err:", e)


def cntntPrs(c):
    l = c.split("\n")
    r = {}
    for i in l:
        if ":" in i:
            k = i.split(":")[0]
            v = i.split(":")[1]
            r[k] = v
    return r


def mkRep(d):
    o = []
    for k in d:
        if len(d[k]) > 3:
            o.append(k + "=" + d[k])
        else:
            o.append(k + "=NA")
    return "|".join(o)


def logIt(m):
    t = time.time()
    print(str(t) + " -> " + m)


def doStuff(p):
    h = dataHndlr(p)
    h.loadFls()

    allD = []

    for f in h.fls:
        c = h.rd(f)
        if c != "":
            pr = cntntPrs(c)
            allD.append(pr)

    res = []
    for d in allD:
        r = mkRep(d)
        res.append(r)

    out = js.dumps(res)

    h.wrt("out.txt", out)

    logIt("done proc")


if __name__ == "__main__":
    p = os.getenv("DATA_PATH", "./data")
    doStuff(p)