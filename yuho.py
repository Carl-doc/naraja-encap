class Subscription:
     
  def __init__(self,price):
    self.final_price = price + price*0.5

    netflix = Subscription(100)
    netflix.final_price = 0
    print(netflix.final_price)