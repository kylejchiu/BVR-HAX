print("Hello World")
age = 15
name = "Kyle"
favorite_color = "Teal"
string = "Hello!"
integer = 1000
float = 0.5
boolean = True
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
area = width * length
print(area)
noun = input("Please enter a noun: ")
verb = input("Please enter an verb: ")
adjective = input("Please enter an adjective: ")
print("The " + adjective + " " + noun + " will " + verb + ".")
score = int(input("What was your score?"))
if (score > 100):
    print("You cheated!")
elif (score > 90):
    print("A is for average")
elif (score > 80):
    print("B is for beating")
elif (score > 70):
    print("C is for can't eat dinner")
elif (score > 60):
    print("D is for don't come home")
elif (score > 0):
    print("F is for find a new family")
elif (score < 0):
    print("You cheated? But why did you get so low of score then...")