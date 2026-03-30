# Kailyn Ziroli 
# Matchmaker Lite 

print("")
print("Matchmaker 2026")
print("")
print("[[Please answer the following questions on a scale on 1-5. 5 being you agree with the statement and 1 being you don't. You will get the total number of compatability at the end.]]")
print("")

userResponse1 = int(input("Chicago Sports Teams are the Best"))
desiredResponse1 = 5
compatability1 = 5 - abs(userResponse1 - desiredResponse1)
print("Question 1 compatability " + str(compatability1))
print("")

userResponse2 = int(input("The Best thing to eat for breakfast is scrambled eggs"))
desiredResponse2 = 2
compatability2 = 5 - abs(userResponse2 - desiredResponse2)
print("Question 2 compatability " + str(compatability2))
print("")

userResponse3 = int(input("I love to do activities outside"))
desiredResponse3 = 5
compatability3 = 5 - abs(userResponse3 - desiredResponse3)
print("Question 3 compatability " + str(compatability3))
print("")

userResponse4 = int(input("I like to travel"))
desiredResponse4 = 4
compatability4 = 5 - abs(userResponse4 - desiredResponse4)
print("Question 4 compatability " + str(compatability4))
print("")

userResponse5 = int(input("Pineapple on Pizza?"))
desiredResponse5 = 1
compatability5 = 5 - abs(userResponse5 - desiredResponse5)
print("Question 5 compatability " + str(compatability5))
print("")

Totalcompatibility = (compatability1 + compatability2 + compatability3 + compatability4 + compatability5) * 25
print("Total Compatibility" + str(Totalcompatibility))
