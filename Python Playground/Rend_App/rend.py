
class Rendeni:

    def __init__(self):
        self.age = 0
        self.Saved_Amt = 0
        self.MandelaAmt = 0
        self.CoinsAcq = 0
        self.CarAmt = 0

    def input_items(self):
            self.age = int(input("Age: "))
            self.MandelaAmt = int(input("Amount of each Mandela Coin: R "))
            self.CarAmt = int(input("The Car Amount: R"))

    def Amount_saved(self):
        j=1
        for i in range(self.age + 1): 
            if(i % 2 == 0 and i != 0):
                self.Saved_Amt = self.Saved_Amt + ((j*1000) - 100)
                j = j + 1
               # print(str(i) + ' ' + str(self.Saved_Amt))
            elif(i%2 == 1):
                self.CoinsAcq = self.CoinsAcq + 1
               # print('This is for the odd: ' + str(i))
            else:
               print('This is Zero: ' + str(i))


    def outputs_coin(self):

        self.input_items()
        self.Amount_saved()
        Saved_amt = (self.CoinsAcq * self.MandelaAmt) + self.Saved_Amt

        if( Saved_amt < self.CarAmt):
            amt_diff = self.CarAmt - Saved_amt
            print("Rendeni cannot afford!")
            print("He still needs: R" + str(amt_diff))
        else:
            amot_diff = Saved_amt - self.CarAmt
            print("Rendeni can afford the car!")
            print("He has an excess of: R" + str(amot_diff))
        
        print( '\n' + "Total Saved Amount: R" + str(Saved_amt))
        print("Saved  Amounts: R" + str(self.Saved_Amt))
        print("Mandela Coins: " + str(self.CoinsAcq))
        print("Mandela Amounts: R" + str(self.CoinsAcq * self.MandelaAmt))



