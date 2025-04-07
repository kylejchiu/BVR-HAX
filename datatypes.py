math = ["Robinson", 100]
science = ["Wildes", 98]
history = ["Henry", 94]
english = ["Bollag-Miller", 95]
spanish = ["Morillo", 93]
music = ["Norgaard", 100]
grades = {"Math": math, "Science": science, "History": history, "English": english, "Spanish": spanish, "Music": music}

while True:
    command = input("Please enter a command ('View' to view a grade and 'Çhange' to change a grade.) ")
    print (command)
    if command == "View":
        viewclass = input("Please enter a class to view (Math, Science, History, English, Spanish, or Music). ")
        print ("Teacher: " + grades[viewclass][0] + " Grade: " + str(grades[viewclass][1]))
    elif command == "Change":
        changeclass = input("Please enter a class to change (Math, Science, History, English, Spanish, or Music). ")
        changed = int(input("Please enter if you want to change the Teacher (1) or the Grade (2). "))
        if changed == 1:
            new = input("Please enter what you want to change it to: ")
            grades[changeclass][changed - 1] = new
        elif changed == 2:
            new = int(input("Please enter what you want to change it to: "))
            grades[changeclass][changed - 1] = new
        else:
            print ("Unkown command, please try again")
    else: 
        print ("Unkown command, please try again")