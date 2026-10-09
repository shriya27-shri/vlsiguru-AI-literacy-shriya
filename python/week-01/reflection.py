
print("My Python Learning Reflection")

name = input("What is your name? ")
learned = input("What did you learn this week? ")
challenge = input("What was difficult for you? ")
next_goal = input("What do you want to learn next? ")

with open("reflection.txt", "w") as file:
    file.write("My Python Learning Reflection\n")
    file.write(f"Name: {name}\n")
    file.write(f"What I learned: {learned}\n")
    file.write(f"My challenge: {challenge}\n")
    file.write(f"My next goal: {next_goal}\n")

print("Your reflection has been saved to reflection.txt")
