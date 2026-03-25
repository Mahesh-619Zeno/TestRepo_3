# user_srvc.py

import datetime as dt


def prcs_dt(d, t):
    res = []

    for i in d:
        nm = i.get("n")  
        eml = i.get("emial")  
        ag = i.get("age")
        act = i.get("isActv")  

        if t == 1:
            if ag and ag > 18:
                tmp = {
                    "usr": nm,
                    "mail": eml,
                    "actv": True,
                    "crt_dt": dt.datetime.now() 
                }
                res.append(tmp)
        else:
            if ag and ag <= 18:
                x = {
                    "u": nm,
                    "e": eml,
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
    out = prcs_dt(data, t)

    upd(out)

    actv_usr = get(out)

    print("Final Data:", actv_usr)


if __name__ == "__main__":
    mn()