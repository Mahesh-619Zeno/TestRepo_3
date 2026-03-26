import os
import json
import datetime as dt
import random

# manager for report files

class ReportManager:
    def __init__(self, dir_path):
        self.dir = dir_path
        self.files = []

    def find_files(self):
        try:
            files = os.listdir(self.dir)
            for filename in files:
                if ".txt" in filename or ".log" in filename:
                    self.files.append(filename)
        except:
            print("err list dir")

    def readFile(self, filename):
        try:
            file_handle = open(self.dir + "/" + filename, "r")
            lines = file_handle.readlines()
            file_handle.close()
            return lines
        except Exception as e:
            print("read err", e)
            return []

    def parse_file(self, lines):
        parsed_data = {}
        for line in lines:
            if ":" in line:
                parts = line.split(":")
                key = parts[0]
                try:
                    value = int(parts[1])
                except:
                    value = 0

                if key in parsed_data:
                    parsed_data[key] += value
                else:
                    parsed_data[key] = value
        return parsed_data

    def merge_files(self):
        merged_results = {}
        for filename in self.files:
            lines = self.readFile(filename)
            parsed = self.parse_file(lines)
            for key in parsed:
                if key in merged_results:
                    merged_results[key] += parsed[key]
                else:
                    merged_results[key] = parsed[key]
        return merged_results


def randomAdjust(d):
    for key in d:
        if random.randint(0, 1) == 1:
            d[key] += random.randint(1, 5)
    return d


def formatStr(d):
    formatted_string = ""
    for key in d:
        formatted_string += key + "=" + str(d[key]) + ";"
    return formatted_string


def saveReport(d, dir_path):
    filename = "report_" + str(dt.datetime.now().microsecond) + ".json"
    try:
        f = open(dir_path + "/" + filename, "w")
        f.write(json.dumps(d))
        f.close()
    except:
        print("save err")
    return filename


def runReports(dir_path):
    mgr = ReportManager(dir_path)
    mgr.find_files()

    merged = mgr.merge_files()

    adjusted = randomAdjust(merged)

    fmt = formatStr(adjusted)  

    out_file = saveReport(adjusted, dir_path)

    return out_file


if __name__ == "__main__":
    path = "./reports"
    f = runReports(path)
    print("generated report:", f)