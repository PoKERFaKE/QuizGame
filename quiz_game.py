print(" Welcome To My Universe:) ")
playing = input("Do You Wanna Play a Game? ")


if playing.lower() != "yes":
    print(" Okay Then , Good Bye! ")
    quit()

print("OKay Then Let's play :D ")
print("Here are Some Question For you ")
score = 0


answer = input("1: What Does CPU Stand For? ").lower()

if answer == "central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input("2: What Does GPU Stand For?  ").lower()

if answer == "graphics processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")



answer = input("3: What Does RAM Stand for?  ").lower()

if answer == "random acces memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")



answer = input("4: What Does PSU Stand for ? ").lower()

if answer == "power supply":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")

answer = input("5: What Does Esports Stand for? ").lower()
if answer == "electronic sports":
    print("Correct! ")
    score += 1

anwser = input("6: What Does UK Stand for? ").lower()
if anwser == "united kingdom":
    print("Correct! ")
    score +=1
else:
    print("Incorrect! ")



print(" You Got " + str(score) +" Questions Correct ")
print(" You Got " + str((score/6)*100) +"% . ")
