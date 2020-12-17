from replit import clear
import art
print(art.logo)

test = {}


x = "yes"


while x != "no":
    X1 = input("Pls Enter your Name")
    Y1 = input("Pls Enter your bid")
    test[X1] = Y1
    x = input("Do you want to bid - Yes or No").lower()
    if x == "yes":
      clear()

#z = test[max(test, key=test.get)]
z = max(test, key=test.get)
#print(test)
print(f"The Winner is {z}")