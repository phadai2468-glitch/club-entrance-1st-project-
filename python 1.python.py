name = input ("what is your name:")
print (f"hello {name}")
age = input ("what is your age:")
print (f"you are {age} years old")
age_int = int(age)
if age_int < 18:
    print ("you are too young to have sex")
    raise SystemExit

if age_int >= 18 and age_int <=50:
    print ("welcome")
else:
    print ("you are too young to have sex")

if age_int >= 45:
    print (f"{name}, does your dick even rise?")
    raise SystemExit
gender = input("what is your sex: ").strip().lower()
if gender == "male":
    print("have fun Man")
elif gender == "female":
    print("have fun GIRL")
else:
    print ("get the tf out you alien ")

input("Press Enter to continue...")
print("hello sir!")
no_of_person = int(input("how many people are you"))
print (("the entry fees is 15$ each"))
total = no_of_person*15
print (f"your total is {total}$")