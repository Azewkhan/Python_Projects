import random
import smtplib

digits= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

OTP = ''.join(random.sample(digits,6))  # join is done to join all the digits/ Random.choices can also be 

Message = "Apni amma na chudaoaur OTP btao"+ OTP

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Email ID", "Password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,Message)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")






