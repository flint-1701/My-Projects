def getdata():
    import datetime
    return datetime.datetime.now()
def retrive():
    print("Select from Following Clients\n"
          "1-akshay\n"
          "2-hammad\n"
          "3-Rohan")
    r=int(input("Enter input:"))
    if r==1:
        print("What do you want to lock\n"
              "1-Exercise\n"
              "2-Diet")
        lck=int(input("Enter the option:"))
        if lck==1:
            with open("akshay_exercise.txt") as f:
                print(f.read())
        else:
            with open("akshay_diet.txt.txt") as f:
                print(f.read())
    elif r==2:
        print("What do you want to lock\n"
              "1-Exercise\n"
              "2-Diet")
        ert=int(input("Enter the option:"))
        if ert==1:
            with open("hammad_exercise.txt") as f:
                print(f.read())
        else:
            with open("hammad_diet.txt") as f:
                print(f.read())
    else:
        print("What do you want to lock\n"
              "1-Exercise\n"
              "2-Diet")
        yui=int(input("Enter the option:"))
        if yui==1:
            with open("Rohan_exercise.txt") as f:
                print(f.read())
        else:
            with open("Rohan_diet.txt") as f:
                print(f.read())
y=open("hammad.txt","w")
i=open("Rohan.txt","w")
print("Select from Following Clients\n"
    "1-akshay\n"
      "2-hammad\n"
      "3-Rohan\n"
      "4-Retrive")
choose=int(input("Enter your choice:"))
if choose==1:
    print("What do you want to lock\n"
          "1-Exercise\n"
          "2-Diet")
    c = int(input("Enter input:"))
    if c == 1:
        f = open("akshay_exercise.txt","a")
        a=str(getdata())
        f.write("\n")
        f.write(a)
        f.write("-")
        wri=input("Enter the exercise\n")
        f.write(wri)
        f.close()
    else:
        f=open("akshay_diet.txt","a")
        b=str(getdata())
        f.write("\n")
        f.write(b)
        f.write("-")
        wri=input("Enter the diet\n")
        f.write(wri)
        f.close()
elif choose==2:
    print("What do you want to lock\n"
          "1-Exercise\n"
          "2-Diet")
    m = int(input("Enter input:"))
    if m == 1:
        f = open("hammad_exercise.txt", "a")
        a = str(getdata())
        f.write("\n")
        f.write(a)
        f.write("-")
        wri = input("Enter the exercise\n")
        f.write(wri)
        f.close()
    else:
        f = open("hammad_diet.txt", "a")
        b = str(getdata())
        f.write("\n")
        f.write(b)
        f.write("-")
        wri = input("Enter the diet\n")
        f.write(wri)
        f.close()
elif choose==3:
    print("What do you want to lock\n"
          "1-Exercise\n"
          "2-Diet")
    p = int(input("Enter input:"))
    if p == 1:
        f = open("Rohan_exercise.txt", "a")
        a = str(getdata())
        f.write("\n")
        f.write(a)
        f.write("-")
        wri = input("Enter the exercise\n")
        f.write(wri)
        f.close()
    else:
        f = open("Rohan_diet.txt", "a")
        b = str(getdata())
        f.write("\n")
        f.write(b)
        f.write("-")
        wri = input("Enter the diet\n")
        f.write(wri)
        f.close()
else:
    retrive()






