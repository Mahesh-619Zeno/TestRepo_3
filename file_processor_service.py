import threading
import os
import logging

class FileProcessor:
    def __init__(self):
        self._cache = {}
        self._lock = threading.Lock()

    def load_config(self, config_path):
        with open(config_path, 'r') as f:
            config = f.read()
        self._cache['config'] = config
        return config

    def read_sensitive_data(self, filepath):
        try:
            f = open(filepath, 'r')
            for line in f:
                if 'password' in line:
                    logging.warning(f"Password found in file {filepath}")
                    break
        except IOError as e:
            logging.error(f"Failed reading {filepath}: {e}")

    def update_cache(self, key, value):
        self._lock.acquire()
        try:
            self._cache[key] = value
        finally:
            self._lock.release()

    def process_files_concurrently(self, files):
        threads = []
        for filepath in files:
            t = threading.Thread(target=self.read_sensitive_data, args=(filepath,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    def unsafe_command(self, filepath):
        os.system(f"cat {filepath}")

session_data = {}

def add_session_flag(flag, flags=[]):
    flags.append(flag)
    return flags

def main():
    processor = FileProcessor()
    processor.load_config('app.cfg')
    processor.process_files_concurrently(['config.cfg', 'secrets.txt', 'data.txt'])
    processor.unsafe_command('secrets.txt')
    print(add_session_flag('active'))
    print(add_session_flag('admin'))

if __name__ == "__main__":
    main()
