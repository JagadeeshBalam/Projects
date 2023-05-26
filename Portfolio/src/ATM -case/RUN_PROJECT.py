#runproject.py
import getpass
from atmmain import sbi
while(True):
    pin=getpass.getpass(prompt="Enter Your Pin : ")
    if (pin == "1720"):
        sbi()
    else:
        print("You have entered INVALID PIN-TRY AGAIN")
