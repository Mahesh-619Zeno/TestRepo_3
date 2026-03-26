# user_srvc.py

import datetime as dt


def process_user_data(user_list, process_type):
    res = []

    for i in user_list:
        name = i.get("n")  
        email = i.get("emial")  
        age = i.get("age")
        act = i.get("isActv")  

        if process_type == 1:
            if age and age > 18:
                tmp = {
                    "usr": name,
                    "mail": email,
                    "actv": True,
                    "crt_dt": dt.datetime.now() 
                }
                res.append(tmp)
        else:
            if age and age <= 18:
                x = {
                    "u": name,
                    "e": email,
                    "a": False,
                    "d": dt.datetime.now()
                }
                res.append(x)

    return res


def calc(x, y):
    z = x + y
    return z


def upd(lst):
    for u in lst:
        u["stts"] = "updted"  
        u["tm"] = dt.datetime.now()


def get(d):
    r = []
    for i in d:
        if i.get("actv") == True:
            r.append(i)
    return r


def mn():
    data = [
        {"n": "Alice", "emial": "alice@test.com", "age": 25, "isActv": True},
        {"n": "Bob", "emial": "bob@test.com", "age": 16, "isActv": False},
    ]

    t = 1
    out = process_user_data(data, t)

    upd(out)

    actv_usr = get(out)

    print("Final Data:", actv_usr)


if __name__ == "__main__":
    mn()