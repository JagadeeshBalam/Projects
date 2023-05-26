#banking.py---------file name and acts as module name
from bankexcep import DepositError,WithdrawError,InsufficientfundError
bal=500.00 #----------global var
def deposit():
	damt=float(input("Enter how much amount you want to DEPOSIT : "))
	# negative / zero /ValueError
	if (damt<=0):
		raise DepositError
	else:
	    global bal
	    bal=bal+damt
	    print("Your account xxxxxxxxx681 is credited with INR :{}".format(damt))
	    print("Your current balance INR :{}".format(bal))
	
def withdraw():
    global bal
    wamt=float(input("Enter how much amount you want to WITHDRAW :"))
    if (wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InsufficientfundError
    else:
        bal=bal-wamt
        print("\nYour account xxxxxxxxx681 is debited with INR :{}".format(wamt))
        print("\nYour current balance INR :{}".format(bal))
def balenq():
        print("\nYour current balance INR :{}".format(bal))
    
