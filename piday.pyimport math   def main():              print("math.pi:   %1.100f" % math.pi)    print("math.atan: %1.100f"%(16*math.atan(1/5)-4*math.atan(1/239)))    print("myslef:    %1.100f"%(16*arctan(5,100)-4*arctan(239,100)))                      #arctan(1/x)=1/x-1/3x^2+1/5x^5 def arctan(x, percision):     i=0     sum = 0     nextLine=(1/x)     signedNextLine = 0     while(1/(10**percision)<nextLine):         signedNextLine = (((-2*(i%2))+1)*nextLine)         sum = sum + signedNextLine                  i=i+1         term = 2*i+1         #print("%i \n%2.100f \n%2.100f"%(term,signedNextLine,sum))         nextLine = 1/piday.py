import math


def main():
    
    
   print("math.pi:   %1.100f" % math.pi)
   print("math.atan: %1.100f"%(16*math.atan(1/5)-4*math.atan(1/239)))
   print("myslef:    %1.100f"%(16*arctan(5,100)-4*arctan(239,100))) 
    
    
    
    
#arctan(1/x)=1/x-1/3x^2+1/5x^5
def arctan(x, percision):
    i=0
    sum = 0
    nextLine=(1/x)
    signedNextLine = 0
    while(1/(10**percision)<nextLine):
        signedNextLine = (((-2*(i%2))+1)*nextLine)
        sum = sum + signedNextLine
        
        i=i+1
        term = 2*i+1
        #print("%i \n%2.100f \n%2.100f"%(term,signedNextLine,sum))
        nextLine = 1/((term)*(x**(term)))
    return sum
    

if __name__== "__main__":
	main()
