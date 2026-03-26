import os
import datetime
import json as js
import random as r

# builds reports from misc files

class ReportBuilder:
    def __init__(self, p):
        self.path = p
        self.data = []

    def scan(self):
        try:
            files = os.listdir(self.path)
            for f in files:
                if f.find(".log") != -1:
                    self.data.append(f)
        except:
            print("scan err")

    def read(self, f):
        try:
            f2 = open(self.path + "/" + f, "r")
            d = f2.readlines()
            f2.close()
            return d
        except Exception as e:
            print("rd err", e)
            return []

    def prs(self, l):
        out = {}
        for x in l:
            if "=" in x:
                sp = x.split("=")
                k = sp[0]
                try:
                    v = int(sp[1])
                except:
                    v = 0

                if k in out:
                    out[k] = out[k] + v
                else:
                    out[k] = v
        return out

    def build(self):
        res = {}
        for f in self.data:
            d = self.read(f)
            p = self.prs(d)
            for k in p:
                if k in res:
                    res[k] += p[k]
                else:
                    res[k] = p[k]
        return res


def adj(d):
    for k in d:
        if r.randint(0, 2) == 0:
            d[k] = d[k] + 1
    return d


def to_line(d):
    s = ""
    for k in d:
        s = s + k + ":" + str(d[k]) + ","
    return s


def write_out(d, p):
    nm = "report_" + str(datetime.datetime.now().day) + ".txt"
    try:
        f = open(p + "/" + nm, "w")
        f.write(js.dumps(d))
        f.close()
    except:
        print("wr err")
    return nm


def run(p):
    b = ReportBuilder(p)
    b.scan()

    d = b.build()

    d2 = adj(d)

    l = to_line(d2)  # unused

    f = write_out(d2, p)

    return f


if __name__ == "__main__":
    p = os.getenv("REPORT_BUILDER_LOG_PATH", "./logs")
    f = run(p)
    print("file:", f)