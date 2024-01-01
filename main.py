import vlc
from time import sleep

def play_timer(name, seconds):
    counter = int(seconds)
    print("\nTimer " + name + " Starts .......\n")

    while True:
        if counter == 0:
            p = vlc.MediaPlayer("sound.mp3")
            print("\nPlaying Timer Audio ........")
            p.play()
            sleep(10)
            p.stop()
            print("\nTimer Audio Stopped ........")
            break
        else:
            sleep(1)
            counter -= 1
            print(counter, "Seconds Remaining ......")

def edit(type, index):
    file = open("timers.csv", "r")
    all_timers_data = file.readlines()
    file.close()

    if index - 1 > len(all_timers_data) or index - 1 < 0:
        print("\nInvalid Index")
        return

    if type == "name":
        new_name = input("\nEnter New Timer Name: ")
        old_timer_data = all_timers_data[index - 1].split(",")
        new_timer_data = new_name + "," + old_timer_data[1]
    elif type == "time":
        new_time = input("\nEnter New Timer Time (in seconds): ")
        old_timer_data = all_timers_data[index - 1].split(",")
        new_timer_data = old_timer_data[0] + "," + new_time
    else:
        print("\nInvalid type")
        return

    all_timers_data[index - 1] = new_timer_data

    with open("timers.csv", "w") as file:
        file.writelines(all_timers_data)

    if type == "name":
        print("\nTimer Name Updated Successfully")
    elif type == "time":
        print("\nTimer Time Updated Successfully")

def show_timers():
    try:
        file = open("timers.csv")
        all_timers_data = file.readlines()
        file.close()

        if len(all_timers_data) == 0:
            print("\nNo Timers Found")
            return -1
        else:
            print()
            for index, timer in enumerate(all_timers_data, 1):
                timer = timer.split(",")
                print(f"{index} > {timer[0]}    {timer[1]}", end="")
        print()
    except FileNotFoundError:
        print("\nFile not found. No timers exist.")
        return -1

def add_timer(name, timeout):
    file = open("timers.csv", "a")
    timer_data = str(name + "," + timeout + "\n")
    file.write(timer_data)
    file.close()
    print("\nTimer Added Successfully, To Start Timer Choose Option 2")

def delete_timer(index):
    file = open("timers.csv", "r")
    all_timers_data = file.readlines()
    file.close()

    if index - 1 > len(all_timers_data) or index - 1 < 0:
        print("\nInvalid Index")
        return

    del all_timers_data[index - 1]

    with open("timers.csv", "w") as file:
        file.writelines(all_timers_data)

    print("\nTimer Deleted Successfully")

while True:
    print("\nCurrent Timers")
    show_timers()

    print("\nMain Menu")
    print("\n1 > Add Timer ")
    print("2 > Start Timer")
    print("3 > Edit Timer")
    print("4 > Delete Timer")
    print("0 > Exit")

    main_menu_choice = int(input("\nEnter Choice : "))

    if main_menu_choice == 1:
        print("\nAdd Timer")
        timer_name = input("\nEnter Timer Name : ")
        timer_timeout = input("Enter Timer Timeout (in seconds) : ")
        add_timer(timer_name, timer_timeout)

    elif main_menu_choice == 2:
        print("\nStart Timer")
        show_timers()
        file = open("timers.csv", "r")
        data = file.readlines()
        file.close()

        if len(data) == 0:
            print("\nNo Timers Exist, Please Add Timer")
        else:
            print("\nExisting Timers\n")
            for index, timer in enumerate(data, 1):
                timer_str = timer.split(",")
                print(index, " >  " + timer_str[0] + "   " + timer_str[1], end="\n")

            chosen_timer = int(input("\nEnter Timer Number You Want To Start : "))

            if chosen_timer > len(data):
                print("\nPlease Enter a Valid Number")
            else:
                timer_data = data[chosen_timer - 1].split(",")
                play_timer(timer_data[0], timer_data[1])

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
                edit("name", index)
            elif edit_menu_choice == 2:
                index = int(input("\nEnter Index Of Timer You Want To Update : "))
                edit("time", index)
            else:
                print("\nUpdation Canceled")

    elif main_menu_choice == 4:
        if show_timers() == -1:
            print("\nCannot Access This Point")
        else:
            print("\nDelete Timer Menu")
            index = int(input("\nEnter Index Of Timer You Want To Delete : "))
            delete_timer(index)

    elif main_menu_choice == 0:
        print("\nProgram Stopped ........")
        break

    else:
        print("\nInvalid Input, Enter Valid Choice Number From Above ........")
