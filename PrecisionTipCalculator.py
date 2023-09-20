import math 
def get_cost():
    while True:
        try:
            cost= float(input(f"Cost of meal:\t"))
        except ValueError:
            print ("Must be valid decimal number. Please try again.")
            continue
        if cost <= 0:
            print ("Must be greater than 0. Please try again.")
        else:
            return cost
 
       

def  get_tip_percent():
    while True:
        try:
            cost= int(input(f"Tip percent:\t"))
          
        except ValueError:
            print ("Must be valid integer. Please try again.")
            continue
        if cost <= 0:
            print ("Must be greater than 0. Please try again.")
        else:
            return cost
        #else:
            #break            

    
def main():
    print(f"Tip Calculator\n")
    print(f"INPUT")
    #get_cost()
   
   
    price = get_cost()
    tip2 =  get_tip_percent()
    #print("\n")
    print(f"\nOUTPUT")
    print(f"Cost of meal:\t", price)
    print(f"Tip percent:\t", tip2,"%")
    rounding = (price*(tip2/100))
    rounding2= round(rounding,2)
    #rounding2 = (float("%.2f ." % rounding))
    print(f"Tip amount:\t", rounding2)
    adding = (price+rounding2)
    adding2 =  round(adding,2)
    print(f"Total amount:\t", adding2)
   

    



if __name__ == "__main__":
    main ()

