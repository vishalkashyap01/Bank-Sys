# generate OTP
import random


def generate_otp(length):
    otp = ''
    for i in range(length):
        otp += str(random.randint(0, 9)) # generate random / convert it to string
    print(otp)    
        
        
      
generate_otp(4)

