text = """
Note calculation system
Average of class is assumed as 50.
"""
print(text)

num1 = int(input("Type your first midterm score: "))
num2 = int(input("Type your second exam score: "))
num3 = int(input("Type your final exam score: "))

result = (num1*0.3)+(num2*0.3)+(num3*0.4)

if result >= 50:
    print(result)
    print("You passed the course")
else:
    print(result)
    print("You failed the course")
