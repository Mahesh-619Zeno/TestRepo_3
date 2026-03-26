import os
import json as j
import datetime

# generates reports from txt files

class ReportGenerator:
    def __init__(self, path):
        self.base_path = path
        self.report_data = []

    def load(self):
        fs = os.listdir(self.base_path)
        for f in fs:
            if ".txt" in f:
                self.report_data.append(self.read(f))

    def read(self, f):
        try:
            fl = open(self.base_path + "/" + f, "r")
            content = fl.read()
            fl.close()
            return content
        except:
            return ""

    def parse(self, content):
        r = {}
        lines = content.split("\n")
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
        for i in self.report_data:
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