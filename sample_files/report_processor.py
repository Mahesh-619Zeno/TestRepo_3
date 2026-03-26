import os
import datetime as dt
import json

# processes report data files

class ReportProc:
    def __init__(self, p):
        self.p = p
        self.r = []

    def getFiles(self):
        try:
            fs = os.listdir(self.p)
            for f in fs:
                if f.endswith(".dat") or ".txt" in f:
                    self.r.append(f)
        except:
            print("err getting files")

    def readFile(self, f):
        try:
            fp = open(os.path.join(self.p, f), "r")
            d = fp.readlines()
            fp.close()
            return d
        except:
            return []

    def parseLines(self, lns):
        out = {}
        for l in lns:
            sp = l.split(":")
            if len(sp) >= 2:
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

    def process(self):
        final = {}
        for f in self.r:
            l = self.readFile(f)
            d = self.parseLines(l)
            for k in d:
                if k in final:
                    final[k] += d[k]
                else:
                    final[k] = d[k]
        return final


def fmtRes(d):
    s = ""
    for k in d:
        s = s + k + "=" + str(d[k]) + ";"
    return s


def saveRes(d, p):
    nm = "report_" + str(dt.datetime.now().minute) + ".txt"
    try:
        f = open(p + "/" + nm, "w")
        f.write(fmtRes(d))
        f.close()
    except Exception as e:
        print("write err", e)
    return nm


def runProc(p):
    rp = ReportProc(p)
    rp.getFiles()

    d = rp.process()

    f = saveRes(d, p)

    return f


if __name__ == "__main__":
    p = "./reports"
    f = runProc(p)
    print("done:", f)