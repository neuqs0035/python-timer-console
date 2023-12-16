import vlc
from time import sleep

def playtimer(name,seconds):

    counter = int(seconds)
    print("\nTimer " + name + " Starts .......\n")

    while(True):

        if(counter == 0):

            p = vlc.MediaPlayer("sound.mp3")
            print("\nPLaying Timer Audio ........")

            p.play()
            sleep(10)
            p.stop()

            print("\nTimer Audio Stopped ........")
            break

        else:
            sleep(1)
            counter -= 1
            print(counter , "Seconds Remaining ......")
        


print("\nCountDown Timer")

while(True):

    print("\nMain Menu")
    print("\n1 > Add Timer ")
    print("2 > Start Timer")
    print("0 > Exit")

    main_menu_choice = int(input("\nEnter Choice : "))

    if(main_menu_choice == 1):

        print("\nAdd Timer")
        file = open("timers.csv","a")

        timer_name = input("\nEnter Timer Name : ")
        timer_timeout = input("Enter Timer Timeout ( in seconds ) : ")
        timer_data = str(timer_name + "," + timer_timeout + "\n")
        file.write(timer_data)
        file.close()

        print("\nTimer Added Success Fully , To Start Timer Choose 2n Option")

    elif(main_menu_choice == 2):

        print("\nStart Timer")

        file = open("timers.csv","r")

        data = file.readlines()
        file.close()

        if(len(data) == 0):

            print("\nNo Timers Exists , Please Add Timer")
            
        else:

            print("\nExisting Timers\n")
            
            for index,timer in enumerate(data,1):

                timerstr = timer.split(",")
                print(index , " >  " + timerstr[0] + "   " + timerstr[1],end="\n")

            choosed_timter = int(input("\nEnter Timer Number You Want To Start : "))

            if(choosed_timter > len(data)):

                print("\nPlease Enter Valid Number")

            else:

                timer_data = data[choosed_timter-1].split(",")
                playtimer(timer_data[0],timer_data[1])

    elif(main_menu_choice == 0):

        print("\nProgram Stopped ........")
        break

    else:
        print("\nInvalid Input , Enter Valid Choice Number From Above ........")
