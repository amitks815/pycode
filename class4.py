class CurrentAccount:
     def __init__(self,customer_name,balance):
         self.name=customer_name
         self.balance=balance

     def  get_custmore_name(self):
         return self.name

     def get_customer_balance(self):
        return self.balance



account_holder=CurrentAccount("amit kumar",20000)

print("the customer name is ",account_holder.get_custmore_name())
print("the customer balance is :",account_holder.get_customer_balance())