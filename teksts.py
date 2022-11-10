import json

cilveks = {"vards":"Jānis","uzvards":"Ābols", "vecums":"23"}
def nolasit(nosaukums):
    f = open(nosaukums, encoding = "utf-8")
    cilveks1, cilveks2 = json.load(f)
    print(cilveks1["vards"])
    print(cilveks2["vards"])
    # print(rinda)
    # vardi = rinda.rsplit(" ")
    # print(vardi)
    #     for vards in vardi:
    #         print(vards)
    f.close()

#nolasit("tests.txt")

def ierakstit(nosaukums, teksts):
    f = open(nosaukums, "a", encoding = "utf = 8", newline = "")
    f.write(str(teksts) + "\n")
    json.dump(teksts,f)
    # print(teksts, file = f)
    f.close()

# ierakstit("tests.txt", cilveks)






print(cilveks["vards"])

# ierakstit("tests.txt", cilveks)
nolasit("tests.txt")