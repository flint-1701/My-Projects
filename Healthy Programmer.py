import time
from plyer import notification
from pygame import mixer
print("----------------I'll Help to Remind Some Basic Stuffs------------")
def Health():
    print("-----------Choose the Work To Remind you-----------\n"
          "1:Water\n"
          "2:Eyes Exercise\n"
          "3:Physical Exercise\n")
    re = int(input("Enter The Choice:"))
    # water drinking reminder
    if re == 1:
        i = 1
        lct = int(input("Enter the time in how many seconds you have to drink water:"))
        repeat = int(input("Enter how many times you should be Reminded:"))
        while i <= repeat:
            time.sleep(lct)
            mixer.init()
            mixer.music.load("water.mp3")
            mixer.music.set_volume(30)
            mixer.music.play()
            notification.notify(
                title="**Please Drink Water Now!!",
                message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
                app_icon="C:\\Users\AKSHAY\PycharmProjects\Pythonpy\water_drink.ico",
                timeout=8
            )

            def getdata():
                import datetime
                return datetime.datetime.now()

            def choice1():
                chs = input("Write Drank After drinking water:")
                if chs.lower() == "drank":
                    mixer.music.stop()
                    a = str(getdata())
                    fw = open("Water.txt", "a")
                    fw.write(a)
                    fw.write("-")
                    fw.write("Drank water")
                    fw.write("\n")
                    print("recorded Successfully")
                else:
                    print("Enter drank to stop the music")
                    choice1()

            choice1()
            i = i + 1
    # Eyes Exercise Reminder
    elif re == 2:
        i = 1
        lct = int(input("Enter the time in how many seconds you have to do Eyes Exercise:"))
        repeat = int(input("Enter how many times you should be Reminded:"))
        while i <= repeat:
            time.sleep(lct)
            mixer.init()
            mixer.music.load("reminder.mp3")
            mixer.music.set_volume(10)
            mixer.music.play()

            def getdata():
                import datetime
                return datetime.datetime.now()

            def choice2():
                chs = input("Write Done after finishing Eyes exercise:")
                if chs.lower() == "done":
                    mixer.music.stop()
                    a = str(getdata())
                    fw = open("Eyes.txt", "a")
                    fw.write(a)
                    fw.write("-")
                    fw.write("done eyes Exercising")
                    fw.write("\n")
                    print("Recorded Successfully")
                else:
                    print("Enter done to stop the music")
                    choice2()

            choice2()
            i = i + 1
    # Physical Exercise
    elif re == 3:
        i = 1
        lct = int(input("Enter the time in how many Seconds you have to do Physical Exercise:"))
        repeat = int(input("Enter how many times you should be Reminded:"))
        while i <= repeat:
            time.sleep(lct)
            mixer.init()
            mixer.music.load("reminder.mp3")
            mixer.music.set_volume(10)
            mixer.music.play()

            def getdata():
                import datetime
                return datetime.datetime.now()

            def choice3():
                chs = input("Write Done after finishing Physical exercise:")
                if chs.lower() == "done":
                    mixer.music.stop()
                    a = str(getdata())
                    fw = open("Exercise.txt", "a")
                    fw.write(a)
                    fw.write("-")
                    fw.write("done Physical Exercising")
                    fw.write("\n")
                    print("Recorded Successfully")
                else:
                    print("Enter done to stop the music")
                    choice3()

            choice3()
            i = i + 1
    else:
        print("Enter Valid Options")
        Health()
Health()





















