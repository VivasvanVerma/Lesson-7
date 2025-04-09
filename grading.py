math = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))
history = int(input("Enter History marks: "))
calc = int(input("Enter Calculus marks: "))
avg = ((math+science+english+history+calc)/500)*100

if avg >=91 and avg <=100:
    print("You got an A")
elif avg >=81 and avg <=90:
    print("You got a B")
elif avg >=71 and avg <=80:
    print("You got a C")
elif avg >=61 and avg <=70:
    print("You got a D")
elif avg <=60:
    print("You got an F")