investment=int(input("please enter amount want to deposit : "))
ROI = 0.5
Tennor=int(input("no of years wants to deposit : "))
Principal= investment * (1 + (ROI*Tennor))
if (investment<=0):
     print("please enter correct amount : ")
else:
       print ("your jackpot is of " , Principal )