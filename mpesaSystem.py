#Lemme show you a cool python project.
def withdraw():
    InMpesa=1000
    AgentNumber = int(input("Enter Agent Number:"))
    amountWithdraw = int(input("Enter amount of money to withdraw:"))
    withdrawMessage= InMpesa - amountWithdraw
    print(amountWithdraw," has been successfully withdrawn from agent number ",AgentNumber)
    print("Your New M-Pesa Balance is,Ksh ",withdrawMessage, "Amount you can transact within a day is, 499 800.")
def send_money():
    def send_money():
        currentBalance=1500
        user = int(input("Enter amount of money to send:"))
        receiver_Num=int(input("Enter number of the Receiver:"))
        sender_Name=(input("Enter Receiver's name: "))
        print("Ksh ",user," has been successfully sent to ",receiver_Num,sender_Name )
        sendMoneyMessage=currentBalance-user
        print("New Mpesa balance is, Ksh",sendMoneyMessage,"Amount you can transact within a day is, 499 800." )

    def mpesa_global():
        print("Welcome to M-PESA Global Services.")
        print("1. Send Money Abroad.")
        print("2. Roaming Pick Ups")
        print("3. Internationa Airtime Transfer")

    def pochi_la_biashara():
        print("Use your Pochi to Transact money from M-Pesa.")
        print("1. pochi")

    def send_to_other_networks():
        print("You can Transact money from M-Pesa to other networks.")

    def HOME():
        print("Press 00 to return back.")
        user=int(input("Enter your Option:"))
        #print("1. pochi")

    while True:
        print("SEND MONEY." )
        print("1. send money" )
        print("2. MPESA Global." )
        print("3.Pochi La Biashara." )
        print("4.Send to other network." )
        print("00. HOME." )
    if user==1:
        send_money()
    elif user==2:
        mpesa_global()
    elif user==3:
        pochi_la_biashara()
    elif user==4:
        send_to_other_networks()
    elif user ==00:
        HOME()
    else:
        print("Sorry !")
def paybill():
    cashInMpesa=20000
    BusinessNumber = int(input("Enter Business Number:"))
    AccountNumber = int(input("Enter Account Number:"))
    AmountToSend = int(input("Enter Amount To send:"))
    paybillMessage= cashInMpesa -AmountToSend
    print("Ksh",AmountToSend," has been successfully paid to Account Number of Business Number",BusinessNumber)
    print("New Mpesa balance is, Ksh", paybillMessage, "Amount you can transact within a day is, 499 800.")

def deposit():
    cashInMpesa=1000
    AgentNumber = int(input("Enter Agent Number:"))
    amountToDeposit = int(input("Enter amount of money to deposit:"))
    balanceMessage= cashInMpesa + amountToDeposit
    print(amountToDeposit," has been successfully deposited into your mpesa account, ")
    print("New M-PESA Balance is ", balanceMessage)
def check_balance():
    cashInMpesa=1000
    print("To Check Your Mpesa Balance Enter Your Pin")
    user = int(input("Enter Your Pin:"))
    '''amountWithdraw = int(input("Enter amount of money to withdraw:"))
    #withdrawMessage= '''

    print("Your new M-Pesa balance is Ksh",cashInMpesa)
def mpesa_offers():
    def payBill():
        print("Hey")
    def BuyGoodsServices():
        print("BuyGoodsServices")
    def pochi_la_biashara():
        print("pochi_la_biashara")
    def BillManager():
        print("BillManager")
    def GlobalPay():
        print("GlobalPay")
    def GovernmentServices():
        print("GovernmentServices")
    def CountyServices():
        print("CountyServices")
    def Transport():
        print("Transport")
    while True:
        print("Your check out our new M-Pesa offers.")
        print("1. Pay Bill .")
        print("2. Buy Goods and Services.")
        print("3. Pochi La Biashara")
        print("4. Bill Manager")
        print("5. Global Pay")
        print("6. Government Services")
        print("7. County Services")
        print("8. Transport")
        user=int(input("Enter Your Choice: "))
        if user==1:
            payBill()
        elif user ==2:
            BuyGoodsServices()
        elif user==3:
            pochi_la_biashara()
        elif user==4:
            BillManager()
        elif user==5:
            GlobalPay()
        elif user==6:
            GovernmentServices()
        elif user==7:
            CountyServices()
        elif user==8:
            Transport()
        else:
            print("Invalid M-PESA offer Option")
def pochi_la_biashara():
    def SendMoney():
        print("sending money")

    def SellAirtime():

        print("sell Airtime ")
    def LipanaPochi():
        print("Lipa na Pochi")
    def WithdrawCash():
        print("Withdraw Cash")
    def MoveMoney():
        print("Monve Money")
    def BiasharaSmart():
        print("Biashara Smart")
    def MyAccount():
        print("My Account")
    def MPESAPromosOffers():
        print("MPESA Promos Offers")
    while True:
        print("POCHI LA BIASHARA")
        print("Use your Pochi to Transact money from M-Pesa.")
        print("1. Send Money")
        print("2. Sell Airtime")
        print("3. Lipa na Pochi")
        print("4. Withdraw Cash")
        print("5. Move Money")
        print("6. Biashara Smart")
        print("7. My Account")
        print("8. M-PESA Promos/Offers")
        user=int(input("Enter Your Choice: "))

        if user==1:
            SendMoney()
        elif user==2:
            SellAirtime()
        elif user ==3:
            LipanaPochi()
        elif user==4:
            WithdrawCash()
        elif user==5:
            MoveMoney()
        elif user ==6:
            BiasharaSmart()
        elif user ==7:
            MyAccount()
        elif user==8:
            MPESAPromosOffers()
        else:
            print("Ops Sorry.")


def buy_bundles():
    def press1():
        print("Oya Syoks sh 10 == Dakika 15 (1hr)")
    def press2():
        print("Sh 10 =Dakika 100 (Midnight)")
    def press3():
        print("Sh 20 =Dakika 20 (Midnight)")
    def press4():
        print("Sh 50 =Dakika 25 (Siku 3)")
    def press5():
        print("Sh 100 =Dakika 700 (Siku 7)")
    while True:
        print("Raukia OFA MOTO.")
        print("1. Oya Syoks sh 10 == Dakika 15 (1hr)")
        print("2. Sh 10 =Dakika 100 (Midnight)")
        print("3.Sh 20 =Dakika 20 (Midnight)")
        print("4.Sh 50 =Dakika 25 (Siku 3)")
        print("5.Sh 100 =Dakika 700 (Siku 7)")
        user=int(input("Enter your Option:"))
        if user==1:
            press1()
        elif user==2:
            press2()
        elif user==3:
            press3()
        elif user==4:
            press4()
        elif user ==5:
            press5()
        else:
            print("Invalid Option.")
def buy_airtime():
    def buy_airtime():
        print("buy_airtime")
    def buy_bundles():
        print("buy_bundles")

    while True:
        print("BUY AIRTIME")
        print("1. Buy Airtime")
        print("2. Buy Bundles")
        user =int(input("Enter Your Options:  "))

        if user==1:
            buy_airtime()
        elif user==2:
            buy_bundles()
        else:
            print("Ops! Sorry")

def financial_services():
    def mali():
        print("mali()")
    def mbanking():
        print("mbanking()")
    def saccos():
        print("saccos()")
    def insurance():
        print("insurance()")
    def wealthManagement():
        print("wealthManagement()")
    def unclaimedFunds():
        print("unclaimedFunds()")

    while True:
        print("Welcome to Our Financial Services")
        print("1. MALI")
        print("2. M-Banking")
        print("3. SACCOS")
        print("4. Insurance")
        print("5. Wealth Management")
        print("6. Unclaimed Funds")
        user = int(input("What Financial Services do you want: "))

        if user==1:
            mali()
        elif user==2:
            mbanking()
        elif user==3:
            saccos()
        elif user==4:
            insurance()
        elif user==5:
            wealthManagement()
        elif user==6:
            unclaimedFunds()
        else:
            print("Ops!! Sorry")
   # break

while True:
    print("MPESA STARTING ..")

    print("1. Withdraw Money.")
    print("2. Send Money.")
    print("3. PayBill Money.")
    print("4. Deposit Money.")
    print("5. Check Balance.")
    print("6. Mpesa offers.")
    print("7. Pochi la Biashara.")
    print("8. Buy Bundles.")
    print("9. Buy Airtime.")
    print("10. Financial Services.")
    user=int(input("Enter Your Choice:"))
    if user ==1:
        withdraw()
    elif user == 2:
        send_money()
    elif user ==3:
        paybill()
    elif user ==4:
        deposit()
    elif user ==5:
        check_balance()
    elif user ==6:
        mpesa_offers()
    elif user == 7:
        pochi_la_biashara()
    elif user == 8:
        buy_bundles()
    elif user == 9:
        buy_airtime()
    elif user == 10:
        financial_services()
    else:
        print("Invalid Option")

