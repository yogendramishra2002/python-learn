a=["apple", "banana",1 ,2,3 ,  "cherry" , "date", "fig", "grape", "honey"]
city = ["Kathmandu", "Pokhara", "Biratnagar", "Birgunj", "Bhaktapur", "Dharan", "Janakpur", "Hetauda", "Itahari", "Nepalgunj"]  
def calc_length(a):
    print(len(a))

calc_length(a)  
calc_length(city)

def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
        print(fact)
    
    
calc_fact(5)
calc_fact(10)


def converter(usd_val):
    inr = usd_val*85
    print("INR:",inr)
    
# converter(7)

def input(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
    
input(5)
input(6) 

                                   RECURSION
                            
                            
                            
def factorial(n):
    if(n==1 or n==0):
         return 1
    return n*factorial(n-1)
 
print(factorial(10))
            
            
def calc_len(list,idx=0):
    if (idx==len(list)):
        return 0
    print(list[idx])
    calc_len(list,idx+1)

sum = calc_len([1,2,3,4,5,6,7,8,9,10])
print(sum)


