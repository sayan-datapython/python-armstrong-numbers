def is_armstrong_number(number):
    length = len(str(number))
    temp=num
    digit=0
    sum=0
    while(temp<o):
        digit=num%10
        sum=sum+digit**length
        temp//=10
    if(sum==num):
        return(True)
    else:
        return(False)
    
    def main():
        num=int(input("Enter a number: "))
        check=is_armstrong_number(num)
        if(check):
            print(f"The (num) is Armstrong number")
        else:
            print(f"The number is not Atmstrong number")
if__name__=='__msin__':
    main()



        
    
  
    

    
      


    
