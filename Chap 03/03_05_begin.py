# Greet the useer
print("Hi!")
name = input("what's your name? ")

print("It's nice to meet you,", name)
answer = input("Are you enjoying the course? ") 

if answer == "Yes":
    print("That's good to hear!")
else:
    print("Oh no! That makes me sad!")

print("We may need your personal information moving forward")
answer = input("Are you comfortable with this? ")

if answer == "Yes":
    print("Interesting, Let's begin")
else:
    print("Press Continue")
    