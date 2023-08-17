capacity = 200
stock = 70
while True:
    n=int(input(print("how many pepsi bottles you want :")))
    if(n<=stock):
        stock-=n
        for i in range (n):
            print("Take it :)")
        print("Have a good drink")
    elif(n>stock):
        print("insufficient stock avaliable only ",stock,"left");
        print("Have a good drink")
    else:
        print("complected outof stock")
        print("Have a good drink")


    
