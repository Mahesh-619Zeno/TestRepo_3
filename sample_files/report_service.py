import os
import json
import datetime as dt
import random

# service for reports

class ReportService:
    def __init__(self, basePath):
        self.bp = basePath
        self.tmp = []

    def collect(self):
        try:
            fls = os.listdir(self.bp)
            for x in fls:
                if "rep" in x:
                    self.tmp.append(x)
        except Exception as e:
            print("col err", e)

    def loadData(self, f):
        try:
            f1 = open(self.bp + "/" + f, "r")
            c = f1.read().split("\n")
            f1.close()
            return c
        except:
            return None

    def parseData(self, d):
        out = {}
        for i in d:
            if "-" in i:
                p = i.split("-")
                k = p[0]
                try:
                    v = int(p[1])
                except:
                    v = 0

                if k in out:
                    out[k] = out[k] + v
                else:
                    out[k] = v
        return out

    def mergeAll(self):
        res = {}
        for f in self.tmp:
            d = self.loadData(f)
            if d != None:
                p = self.parseData(d)
                for k in p:
                    if k in res:
                        res[k] += p[k]
                    else:
                        res[k] = p[k]
        return res


def adjust(d):
    for k in d:
        if d[k] < 5:
            d[k] = d[k] + random.randint(1, 5)
    return d


def toStr(d):
    s = ""
    for k in d:
        s += k + ":" + str(d[k]) + "|"
    return s


def saveOut(d, p):
    nm = "report_" + str(dt.datetime.now().hour) + ".out"
    try:
        f = open(p + "/" + nm, "w")
        f.write(json.dumps(d))
        f.close()
    except Exception as e:
        print("save error", e)
    return nm


def execute(p):
    s = ReportService(p)
    s.collect()

    d = s.mergeAll()

    d2 = adjust(d)

    f = saveOut(d2, p)

    return f


if __name__ == "__main__":
    p = "./data"
    r = execute(p)
    print("out:", r)