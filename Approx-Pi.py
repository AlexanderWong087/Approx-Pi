import sys 

def calculate_pi(n): 
    numerator_1=2 
    numerator_2=4 
    denominator_root=3 
    output=4 
    for i in range(n): 
        output*=(numerator_1*numerator_2)/(denominator_root**2) 
        numerator_1+=2 
        numerator_2+=2 
        denominator_root+=2 
    return output  

n_put=input('Please input N: ') 

try: 
    n_put=int(n_put) 
except ValueError: 
    print('ValueError detected. Please input an integer value. Program Ending.') 
    sys.exit() 

print(calculate_pi(n_put))  
