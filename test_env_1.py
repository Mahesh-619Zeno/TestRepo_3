import os

def main():
    user = os.getenv('USER_NAME', 'Guest')
    mode = os.getenv('APP_MODE', 'production')
    retries = int(os.getenv('MAX_RETRIES', '3'))

    print(f"Welcome, {user}!")
    print(f"Application mode: {mode}")
    print(f"Max retries: {retries}")

    for attempt in range(1, retries + 1):
        print(f"Attempt {attempt} of {retries}")
        if attempt == 2:
            print("Operation succeeded!")
            break
    else:
        print("All attempts failed.")

if __name__ == "__main__":
    main()
