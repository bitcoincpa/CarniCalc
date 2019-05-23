import PriceList

print("Hello Carnis")
#budget_input = "What is your daily budget?"
#lb_input = "How many pounds of meat do you want to eat per day?"

class Meal:
    def __init__(self, budget, lb):
        self.budget = budget
        self.lb = lb
        self.price = PriceList.Prices()
        


    def priceperlb(self):
        total= self.price.ribeye * self.lb
        return total

    
dave = Meal(10,10)

print(dave.priceperlb())