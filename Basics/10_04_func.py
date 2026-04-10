def func_one(num1 = 200, num2 = 200):
    res = num1 + num2
    print(res)

func_one()  
func_one(2000,2000)  

def func_two(num1, num2):
    print(num1,num2)

func_two(num2 = 100, num1 = 200)    
# Example 10
# Variable Argument 
# data stored as tuple
def func_one(*param1):
    print(sum(param1))

func_one(10)
func_one(10,20,30,40,50)