import os
import json
import datetime as dt
import random

# manager for report files

class ReportManager:
    def __init__(self, dir_path):
        self.dir = dir_path
        self.files = []

    def findFiles(self):
        try:
            fs = os.listdir(self.dir)
            for f in fs:
                if ".txt" in f or ".log" in f:
                    self.files.append(f)
        except Exception as e:
            print(f"Error listing directory {self.dir}: {e}")

    def readFile(self, f):
        try:
            fp = open(self.dir + "/" + f, "r")
            lines = fp.readlines()
            fp.close()
            return lines
        except Exception as e:
            print("read err", e)
            return []

    def parseFile(self, lines):
        out = {}
        for l in lines:
            if ":" in l:
                sp = l.split(":")
                k = sp[0]
                try:
                    v = int(sp[1])
                except:
                    v = 0

                if k in out:
                    out[k] += v
                else:
                    out[k] = v
        return out

    def mergeFiles(self):
        res = {}
        for f in self.files:
            lines = self.readFile(f)
            parsed = self.parseFile(lines)
            for k in parsed:
                if k in res:
                    res[k] += parsed[k]
                else:
                    res[k] = parsed[k]
        return res


def randomAdjust(d):
    for k in d:
        if random.randint(0, 1) == 1:
            d[k] += random.randint(1, 5)
    return d


def formatStr(d):
    s = ""
    for k in d:
        s += k + "=" + str(d[k]) + ";"
    return s


def saveReport(d, dir_path):
    nm = "report_" + str(dt.datetime.now().microsecond) + ".json"
    try:
        f = open(dir_path + "/" + nm, "w")
        f.write(json.dumps(d))
        f.close()
    except:
        print("save err")
    return nm


def runReports(dir_path):
    mgr = ReportManager(dir_path)
    mgr.findFiles()

    merged = mgr.mergeFiles()

    adjusted = randomAdjust(merged)

    fmt = formatStr(adjusted)  # computed but unused

    out_file = saveReport(adjusted, dir_path)

    return out_file


if __name__ == "__main__":
    path = os.getenv("REPORTS_PATH", "./reports")
    f = runReports(path)
    print("generated report:", f)