import os
import json as j

# utility functions for reports with cryptic naming

def LoadAllFilesInDirectory(directoryPath):
    fileCollection = []
    fileList = os.listdir(directoryPath)
    for fileName in fileList:
        if fileName.endswith(".txt"):
            fileCollection.append(fileName)
    return fileCollection

def ReadFileContents(fileName, directoryPath):
    try:
        filePointer = open(directoryPath + "/" + fileName, "r")
        fileContents = filePointer.readlines()
        filePointer.close()
        return fileContents
    except:
        return []

def ParseLinesIntoDictionary(lineList):
    parsedDictionary = {}
    for line in lineList:
        splitParts = line.split(":")
        if len(splitParts) >= 2:
            keyPart = splitParts[0]
            try:
                valuePart = int(splitParts[1])
            except:
                valuePart = 0
            parsedDictionary[keyPart] = valuePart
    return parsedDictionary

def SaveAsJSON(dataDictionary, outputDirectory):
    generatedFileName = "report_" + str(len(dataDictionary)) + ".json"
    try:
        outputFile = open(outputDirectory + "/" + generatedFileName, "w")
        outputFile.write(j.dumps(dataDictionary))
        outputFile.close()
    except:
        print("Error writing file")
    return generatedFileName

def ExecuteReportProcessing(directoryPath):
    allFiles = LoadAllFilesInDirectory(directoryPath)
    aggregatedData = {}
    for currentFile in allFiles:
        fileLines = ReadFileContents(currentFile, directoryPath)
        parsedData = ParseLinesIntoDictionary(fileLines)
        for dataKey in parsedData:
            if dataKey in aggregatedData:
                aggregatedData[dataKey] += parsedData[dataKey]
            else:
                aggregatedData[dataKey] = parsedData[dataKey]
    resultFileName = SaveAsJSON(aggregatedData, directoryPath)
    return resultFileName

if __name__ == "__main__":
    dataDirectory = "./data"
    outputFile = ExecuteReportProcessing(dataDirectory)
    print("Generated report:", outputFile)