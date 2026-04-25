class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []    # This is the instance variable
    
    def deposit(self, amount, description = ""):
        # Create the object (dictionary) and append it to the ledger
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)
    
    def withdraw(self, amount, description = ""):
        # Input/Action: Create the object with a negative amount
        transaction = {"amount": -amount, "description": description}
        
        # Storage: Append to the instance variable
        self.ledger.append(transaction)
        return True
    
    def get_balance(self):
    # Sum up all 'amount' values in the ledger objects
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    def transfer(self, amount, category_instance):
    
        # Withdraw from THIS category
            self.withdraw(amount, f"Transfer to {category_instance.name}")
        
        # Deposit into the OTHER category
            category_instance.deposit(amount, f"Transfer from {self.name}")
        
            return True
    
    


    

    
    
    


    

def create_spend_chart(categories):
    pass    