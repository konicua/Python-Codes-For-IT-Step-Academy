while True:
    a = input("Give an email adress: ")
    if a == "STOP":
        print("program ends")
        break
    teller = 0
    controle = 0
    punt = 0
    for x in a:
        if x =="@":
            teller = teller + 1
        elif x == ".":
            punt = punt + 1
        elif x not in "abcdefghijklmnopqrstuvwxyz1234567890":
            controle = controle + 1
    if teller == 1 and punt >= 1 and controle == 0:
        (prefix, domein) = a.split("@")
        if len(prefix) >= 1 and len(domein) >= 2:
            (domein_1, domein_2) = a.split(".")
            if len(domein_1) >= 2 and len(domein_2) >= 2:
                print("email is valid")
            else:
                print("email is invalid")
        else:
            print("email is invalid")
    else:
        print("email is invalid")