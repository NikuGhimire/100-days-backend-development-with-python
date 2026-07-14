score = 0
ans = input("What is the value of pie: ")
if ans == "22/7" or ans == "3.14":
    score = 1+score
else:
    print("The answer is incorrect")
ans = input("What is the value of perimeter of square: ")
if ans == "4L" or ans == "4*L":
    score = 1+score
else:
    print("The answer is incorrect")
ans = input("What is the value of area of rectangle: ")
if ans =="L^2" or ans == "L*L":
    score = 1+score
else:
    print("The answer is incorrect")
print("Final score:", score)
