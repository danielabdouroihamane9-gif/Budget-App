class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []    # This is the instance variable
    
    def deposit(self, amount, description = ""):
        # Create the object (dictionary) and append it to the ledger
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)
    
    def withdraw(self, amount, description = ""):
        # Call check_funds to see if we have enough
        if self.check_funds(amount):   

        # Create the object with a negative amount
            transaction = {"amount": -amount, "description": description} 
        
        # Storage: Append to the instance variable
            self.ledger.append(transaction)
            return True     # The withdrawal took place!
        
        return False        # if check_funds failed
    
    def get_balance(self):
    # Sum up all 'amount' values in the ledger objects
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    def transfer(self, amount, category_instance):
        # first check if the source category has enough money
        if self.check_funds(amount):
        # Withdraw from THIS category
            self.withdraw(amount, f"Transfer to {category_instance.name}")
        
        # Deposit into the OTHER category
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True     # if funds are sufficient
        
        return False      # if funds are insufficient

    def check_funds(self, amount):
    # Get the current balance
        current_balance = self.get_balance()
    
    # Compare it to the requested amount
        if amount > current_balance:
            return False  # Not enough money!
        else:
            return True   # All clear!

    def __str__(self):
    # The Title Line: Center the name with '*' to fill 30 characters
        title = f"{self.name:*^30}\n"
    
        # The Items: Loop through the ledger
        items = ""
        for item in self.ledger:
            # Format description: first 23 characters, left-aligned
            desc = f"{item['description'][:23]:23}"
            # Format amount: 2 decimal places, right-aligned, 7 characters total
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
    
        # The Total Line
        total = f"Total: {self.get_balance():.2f}"
    
        return title + items + total


def create_spend_chart(categories):
    # The header Title
    res = "Percentage spent by category\n"
    
    # CALCULATE PERCENTAGES (The "Process")
    spent = []
    for cat in categories:
        # Sum only the negative amounts (withdrawals)
        sum_neg = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent.append(sum_neg)
    
    total_spent = sum(spent)
    # Round down to the nearest 10 (e.g., 36% -> 30)
    percentages = [(sum_neg / total_spent * 100) // 10 * 10 for sum_neg in spent]

    # BUILD THE Y-AXIS (The "Output")
    # Start at 100, go down to 0, jumping by -10 each time
    for i in range(100, -1, -10):
        # Format the number to be 3 spaces wide: "100| ", " 90| ", etc.
        res += f"{str(i).rjust(3)}| "
        
        # DRAW THE BARS
        for p in percentages:
            if p >= i:
                res += "o  " # Bar exists at this level
            else:
                res += "   " # Empty space
        
        res += "\n" # Move to the next row (e.g., from 100 to 90)
    horizontal_line = "    " + "-" * (len(categories) * 3 + 1)
    
    # 3. Add a newline so the category names start on the next line
    res += horizontal_line + "\n"
    
    # VERTICAL NAMES (Added logic)
    max_len = max(len(cat.name) for cat in categories)
    
    for i in range(max_len):
        res += "     " 
        for cat in categories:
            if i < len(cat.name):
                res += f"{cat.name[i]}  "
            else:
                res += "   "
        
        # Remove newline at the very end
        if i < max_len - 1:
            res += "\n"

    return res


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)

print(food)
print(create_spend_chart([food, clothing]))

   