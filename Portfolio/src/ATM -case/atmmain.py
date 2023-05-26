#atmmain.py------------file name
from atmmenu import atmmenu
from banking import deposit,withdraw,balenq
from bankexcep import DepositError,WithdrawError,InsufficientfundError
import sys
def sbi():
    while(True):
        atmmenu()
        try:
            ch=int(input("Enter your choice : "))
            match(ch):
                case 1:
                    try:                    
                        deposit()
                    except ValueError:                    
                        print("\nDon't enter strings/symbols/alpha-numerics")
                    except DepositError:
                        print("\nDon't enter zero and negative values")     
                case 2:
                    try:
                        withdraw()
                    except ValueError:
                        print("\nDon't enter strings/symbols/alpha-numerics")
                    except WithdrawError:
                        print("\nDon't withdraw nwgative or zero values")
                    except InsufficientfundError:
                        print("\nYou don't have sufficient funds")
                case 3:
                    balenq()
                case 4:
                    print("\nThanks for using Our ATM SERVICES")
                    sys.exit()
                case _:
                    print("You have selected invalid operation-TRY AGAIN")
        except ValueError:
            print("\nDon't enter strings/symbols/alpha-numerics ")
