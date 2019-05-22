print("Hello Carnis")

class Meal:
    def __init__(self, budget, lb):
        self.budget = budget
        self.lb = lb
        


    def priceperlb(self, cost):
        self.cost = cost
        total= float(cost) * float(self.lb)
        return total

    
ribeye = Meal(30,1)

print(ribeye.priceperlb(20))