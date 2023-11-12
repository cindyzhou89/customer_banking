
from Account import Account

def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("please enter your savings balance here: "))
    interest_rate_m = float(input("please enter your interest rate here: "))
    months_m = int(input("please enter your months here: "))
    print(savings_balance, interest_rate_m, months_m)
    # Call the create_savings_account function and pass the variables from the user. updated_savings_balance,
    # interest_earned = savings_account.create_savings_account(savings_balance, savings_interest, savings_maturity)
    account = Account(savings_balance, interest_rate_m)
    CSA = account.create_savings_account(months_m)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(f"the interest you earned are: ", CSA, "your saving balance are:", savings_balance, "for", months_m, "months")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    newCDB = float(input("Please enter your new CD balance: "))
    newCDR = float(input("Please enter your new CD interest rate: "))
    newCDM = int(input("Please enter your new CD months: "))
    # Call the create_cd_account function and pass the variables from the user.
    # updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    #   newCD = cd_account.create_cd_account(newCDB, newCDR, newCDM)

    #cd_acc = cd_account(newCDB, newCDR)
    newCD = account.create_cd_account(newCDM)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(newCD)


if __name__ == "__main__":
    # Call the main function.
    main()
class Account:
    def __init__(self, balance, interest_rate=0.85):
        self.balance = balance
        self.interest = interest_rate

    # This method sets the balance of the account.

    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    def get_interest(self):
        """Sets the interest gained for the the account"""
        return self.interest

    def get_balance(self):
        """Sets the interest gained for the the account"""
        return self.balance
    
    def create_savings_account(self,months):
        interest_earned = float(self.balance * (self.interest / 12) * months)
        myNewBalance = self.balance + interest_earned
        self.set_balance(myNewBalance)
        return float(interest_earned)
    
    def create_cd_account(self,months):
        interest_earned = float(self.balance * (self.interest / 12) * months)
        myNewBalance = self.balance + interest_earned
        self.set_balance(myNewBalance)
        return float(interest_earned)
