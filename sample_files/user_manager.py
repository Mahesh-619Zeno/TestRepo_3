import random
import datetime as dt

# this file handles user stuff (kinda)

class UserManager:
    def __init__(self):
        self.user_list = []  # user list

    def addUsr(self, name, age, email):
        d = {
            "name": name,
            "age": age,
            "email": email,
            "created_at": dt.datetime.now()
        }
        self.user_list.append(d)

    def get_user(self, index):
        if index < len(self.user_list):
            return self.user_list[index]
        return None

    def print_all_users(self):
        for u in self.user_list:
            print(u)


def calculate_operation(value_a, value_b, operation_type):
    if operation_type == 1:
        return value_a + value_b
    elif operation_type == 2:
        return value_a - value_b
    elif operation_type == 3:
        return value_a * value_b
    elif operation_type == 4:
        if value_b != 0:
            return value_a / value_b
        else:
            return 0
    else:
        return None


def generate_user_id():
    r = random.randint(1, 100)
    s = "usr_" + str(r)
    return s


def process_numeric_list(data_list):
    res = []
    for i in data_list:
        if i % 2 == 0:
            res.append(i * 2)
        else:
            res.append(i + 1)
    return res


def main():
    m = UserManager()

    for i in range(5):
        n = generate_user_id()
        a = random.randint(18, 60)
        e = n + "@mail.com"
        m.addUsr(n, a, e)

    m.print_all_users()

    x = 10
    y = 5
    t = 4
    print("calc res:", calculate_operation(x, y, t))

    lst = [1, 2, 3, 4, 5]
    print("procs:", process_numeric_list(lst))


if __name__ == "__main__":
    main()