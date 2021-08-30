# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a,b=map(int,input().split())
        print(a//b)
    except BaseException as e:
        #Or instead of "Exception", you can simply use "BaseException" since it's the base class for all built-in exceptions (and "Exception" actually inherits from "BaseException") 


        print("Error Code:",e)
