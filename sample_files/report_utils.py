import os
import json as j

# utility functions for reports with cryptic naming

def load_all_files_in_directory(directory_path):
    fileCollection = []
    fileList = os.listdir(directory_path)
    for fileName in fileList:
        if fileName.endswith(".txt"):
            fileCollection.append(fileName)
    return fileCollection

def read_file_contents(file_name, directory_path):
    try:
        file_handle = open(os.path.join(directory_path, file_name), "r")
        file_contents = file_handle.readlines()
        file_handle.close()
        return file_contents
    except:
        return []

def parse_lines_into_dictionary(line_list):
    parsed_dictionary = {}
    for line in line_list:
        splitParts = line.split(":")
        if len(splitParts) >= 2:
            keyPart = splitParts[0]
            try:
                valuePart = int(splitParts[1])
            except:
                valuePart = 0
            parsed_dictionary[keyPart] = valuePart
    return parsed_dictionary

def save_as_json(data_dictionary, output_directory):
    generated_file_name = "report_" + str(len(data_dictionary)) + ".json"
    try:
        with open(output_directory + "/" + generated_file_name, "w") as output_file:
            output_file.write(j.dumps(data_dictionary))
    except:
        print("Error writing file")
    return generated_file_name

def execute_report_processing(directory_path):
    all_files = load_all_files_in_directory(directory_path)
    aggregated_data = {}
    for current_file in all_files:
        file_lines = read_file_contents(current_file, directory_path)
        parsed_data = parse_lines_into_dictionary(file_lines)
        for data_key in parsed_data:
            if data_key in aggregated_data:
                aggregated_data[data_key] += parsed_data[data_key]
            else:
                aggregated_data[data_key] = parsed_data[data_key]
    result_file_name = save_as_json(aggregated_data, directory_path)
    return result_file_name

if __name__ == "__main__":
    dataDirectory = "./data"
    outputFile = ExecuteReportProcessing(dataDirectory)
    print("Generated report:", outputFile)