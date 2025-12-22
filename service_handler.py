import threading
import time
import os
import random
import logging

class ServiceHandler:
    def __init__(self):
        self.user_sessions = {}
        self.session_lock = threading.Lock()
        self.cache = {}

    def start_session(self, user_id):
        session_id = f"sess_{random.randint(1000, 9999)}"
        self.user_sessions[session_id] = {"user": user_id, "active": True}
        return session_id

    def stop_session(self, session_id):
        if session_id in self.user_sessions:
            self.user_sessions[session_id]["active"] = False

    def fetch_resource(self, filepath):
        # Not using context manager for file handling
        f = open(filepath, 'r')
        data = f.read()
        # File may remain open if error occurs, resource leak risk
        return data

    def cache_resource(self, key, value):
        self.cache[key] = value

    def get_cached(self, key):
        return self.cache.get(key)

    def unsafe_execute_command(self, cmd):
        os.system(cmd)

    def update_session_data(self, session_id, info):
        self.session_lock.acquire()
        try:
            if session_id in self.user_sessions:
                self.user_sessions[session_id].update(info)
        finally:
            self.session_lock.release()

    def process_sessions_concurrently(self, session_id):
        threads = []
        for i in range(5):
            thread = threading.Thread(target=self.update_session_data, args=(session_id, {"counter": i}))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

def log_activity(user_id, action, log_cache=[]):
    log_cache.append((user_id, action))
    return log_cache

def main():
    service = ServiceHandler()
    user = "user42"
    session = service.start_session(user)

    for _ in range(3):
        data = service.fetch_resource("data.txt")
        service.cache_resource("latest_data", data)

    print(service.get_cached("latest_data"))

    service.unsafe_execute_command("ls /var/tmp")

    logs1 = log_activity(user, "login")
    logs2 = log_activity(user, "fetch_data")

    print(logs1)
    print(logs2)

    service.process_sessions_concurrently(session)

    print(service.user_sessions.get(session))

    for i in range(10):
        if i > 4:
            if i % 2 == 0:
                if i < 9:
                    print(f"Item {i} processed")

    print("Service complete")

if __name__ == "__main__":
    main()
