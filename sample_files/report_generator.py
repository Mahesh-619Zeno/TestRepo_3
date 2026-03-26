import os
import json as j
import datetime

# generates reports from txt files

class ReportGenerator:
    def __init__(self, path):
        self.p = path
        self.d = []

    def load(self):
        fs = os.listdir(self.p)
        for f in fs:
            if ".txt" in f:
                self.d.append(self.read(f))

    def read(self, f):
        try:
            fl = open(self.p + "/" + f, "r")
            c = fl.read()
            fl.close()
            return c
        except:
            return ""

    def parse(self, c):
        r = {}
        lines = c.split("\n")
        for l in lines:
            if "=" in l:
                k = l.split("=")[0]
                v = l.split("=")[1]
                try:
                    r[k] = int(v)
                except:
                    r[k] = 0
        return r

    def combine(self):
        res = {}
        for i in self.d:
            p = self.parse(i)
            for k in p:
                if k in res:
                    res[k] = res[k] + p[k]
                else:
                    res[k] = p[k]
        return res


def makeStr(d):
    s = ""
    for k in d:
        s += k + ":" + str(d[k]) + ","
    return s[:-1]


def save(r, p):
    nm = "report_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".json"
    try:
        f = open(p + "/" + nm, "w")
        f.write(j.dumps(r))
        f.close()
    except Exception as e:
        print("save er", e)
    return nm


def genReport(p):
    g = ReportGenerator(p)
    g.load()

    c = g.combine()
    f = save(c, p)

    return f


if __name__ == "__main__":
    p = "./data"
    r = genReport(p)
    print("report:", r)