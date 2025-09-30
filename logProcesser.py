import datetime
import os

log_file_path = "app.log"
DEFAULT_LEVEL = "INFO"

class Log_Processor:
    def __init__(self, LogLevel):
        self.LogLevel = LogLevel
        
    def ParseLogLine(self, line):
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry_processed = f"[{d}] [{self.LogLevel}] {line.strip()}"
        return log_entry_processed
        
    def write_to_file_func(self, processed_line):
        A = processed_line + "\n"
        with open(log_file_path, "a") as f:
            f.write(A)

def get_log_data_from_file(a_file):
    list = []
    if not os.path.exists(a_file):
        return list
    with open(a_file, "r") as f:
        for _ in f.readlines():
            list.append(_)
            
    return list

def Process_Logs_And_Write(log_lines):
    myProcessor = Log_Processor(DEFAULT_LEVEL)
    for line in log_lines:
        processed_line = myProcessor.ParseLogLine(line)
        myProcessor.write_to_file_func(processed_line)
    print("Log processing complete.")

def MainFunc():
    my_lines = get_log_data_from_file(log_file_path)
    if len(my_lines) == 0:
        print("Log file is empty or does not exist.")
    else:
        Process_Logs_And_Write(my_lines)

if __name__ == "__main__":
    MainFunc()