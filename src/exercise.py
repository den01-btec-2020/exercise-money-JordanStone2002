def main():
    #write your code below this line
  def plus(self, addition):
   new_Money = Money()


  class Money:
    new_Money = Money()
    a = Money(10,0)
    b = Money(5,0)

    c = a.plus(b)

    def __init__(self, pounds, pence):
        self.pounds = pounds
        self.pence = pence
 
    def pounds(self):
        return self.pounds
 
    def pence(self):
        return self.pence
 
    def __str__(self):
        zero = ""
        if (self.pence <= 10):
            zero = "0"
 
        return str(self.pounds) + "." + zero + str(self.pence) + "p"

      
if __name__ == '__main__':
    main()
