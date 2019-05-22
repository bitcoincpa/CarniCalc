import PriceList as pl

print("Hello Carnis")
#budget_input = "What is your daily budget?"
#lb_input = "How many pounds of meat do you want to eat per day?"

class Meal:
    def __init__(self, budget, lb):
        self.budget = budget
        self.lb = lb
        self.price = pl.Prices()
        


    def priceperlb(self):
        total= self.price.ribeye * self.lb
        return total

    
ribeye = Meal(10,10)

print(ribeye.priceperlb())