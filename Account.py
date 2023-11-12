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
