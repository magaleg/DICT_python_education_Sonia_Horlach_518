"""Chatbot project"""
print("Hello! My name is Vitalik")
print("I was created in 2023")
print("Please, remind me your name.")
name = input()
print("What a great name you have," + name + "!")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is", age, "; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input())
count = 0
while count <= number:
    print(count, "!")
    count += 1
print("Let's test your programming knowledge.")
print("What is the command for moving to another brunch?")
print("1. git checkout {brunch_name}")
print("2. git add {brunch_name}")
print("3. git commit {brunch_name}")
print("4. git log {brunch_name}")
while True:
    answer = int(input())
    if answer == 1:
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")
        continue

print("Congratulations, have a nice day!")
