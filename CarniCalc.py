import PriceList

"""print("Hello Carnis")
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

print(dave.priceperlb())"""

def dpMakeChange(coinValueList,budget,minCoins,coinsUsed):
   for cents in range(budget+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,budget):
   coin = budget
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()