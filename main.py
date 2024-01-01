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
        
def edit(type, index):
    file = open("timers.csv", "r")
    all_timers_data = file.readlines()
    file.close()

    if index-1 > len(all_timers_data) or index-1 < 0:
        print("\nInvalid Index")
        return

    if type == "name":
        new_name = input("\nEnter New Timer Name: ")
        old_timer_data = all_timers_data[index-1].split(",")
        new_timer_data = new_name + "," + old_timer_data[1]
    elif type == "time":
        new_time = input("\nEnter New Timer Time (in seconds): ")
        old_timer_data = all_timers_data[index-1].split(",")
        new_timer_data = old_timer_data[0] + "," + new_time
    else:
        print("\nInvalid type")
        return

    all_timers_data[index-1] = new_timer_data

    with open("timers.csv", "w") as file:
        file.writelines(all_timers_data)

    if type == "name":
        print("\nTimer Name Updated Successfully")
    elif type == "time":
        print("\nTimer Time Updated Successfully")

def show_timers():
    
    file = open("timers.csv")

    all_timers_data = file.readlines()

    file.close()

    if len(all_timers_data) == 0:
        print("\nNo Timers Found")
        return -1

    else:
        print()
        for index,timer in enumerate(all_timers_data,1):

            timer = timer.split(",")

            print(f"{index} > {timer[0]}    {timer[1]}",end="")
        
        print()

def add_timer(name,timeout):
    file = open("timers.csv","a")

    timer_data = str(name + "," + timeout + "\n")
    file.write(timer_data)
    file.close()

    print("\nTimer Added Success Fully , To Start Timer Choose 2n Option")

while(True):


    print("\nCurrent Timers")

    show_timers()

    print("\nMain Menu")
    print("\n1 > Add Timer ")
    print("2 > Start Timer")
    print("3 > Edit Timer")
    print("0 > Exit")

    main_menu_choice = int(input("\nEnter Choice : "))

    if(main_menu_choice == 1):

        print("\nAdd Timer")

        timer_name = input("\nEnter Timer Name : ")
        timer_timeout = input("Enter Timer Timeout ( in seconds ) : ")    

        add_timer(timer_name,timer_timeout)

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

    elif main_menu_choice == 3:

        if show_timers() == -1:
            print("\nCannot Access This Point")
        
        else:

            print("\nEdit Timer Menu")

            print("\n1 > Edit Timer Name")
            print("2 > Edit Timer Time")
            print("0 > Cancel Edit Option")

            edit_menu_choice = int(input("\nEnter Choice : "))

            
            if edit_menu_choice == 1:
                
                index = int(input("\nEnter Index Of Timer You Want To Update : "))
                edit("name",index)
            
            elif edit_menu_choice == 2:

                index = int(input("\nEnter Index Of Timer You Want To Update : "))
                edit("time",index)

            else:
                print("\nUpdation Canceled")
    elif(main_menu_choice == 0):

        print("\nProgram Stopped ........")
        break

    else:
        print("\nInvalid Input , Enter Valid Choice Number From Above ........")
