FROM = "km"
FROM = "m"
FROM = "cm"
TOO = "m" 
TOO = "cm"
TOO = "km"

FROM = input ("from: ") .strip() .lower()
TOO = input ("to: ") .strip() .lower()

if FROM == "km" and TOO == "m" :
 km =  float(input ("write the value in km:  "))
 meter = km*1000  
 print (f"your measurement in meter is {round(meter,1)}{meter}m")

elif FROM == "km" and TOO == "cm" : 
 km = float(input("write the value in km: "))
 centimeter = km*100000
 print (f"your measurement is{round(centimeter,1)} {centimeter}cm")

elif FROM == "m" and TOO == "cm" : 
 m = float(input("write the value in m: "))
 centimeter = m*100
 print (f"your measurement is {round(centimeter,1)} {centimeter}cm")

elif FROM == "m" and TOO == "km" : 
 m = float(input("write the value in m: "))
 kilometer = m/1000
 print (f"your measurement is {round(kilometer,1)} {kilometer}km")

elif FROM == "cm" and TOO == "km" :
 cm = float(input("write the value in cm: "))
 kilometer = cm/100000
 print (f"your measurement is {round ((kilometer,1))} {kilometer}km")
 
elif FROM == "cm" and TOO == "m" :
 cm = float(input("write the value in cm: "))
 meter = cm/1000
 print (f"your measurement is {round (meter,1)} {meter}km")

 
else :
 print ("error")