def check(expr):
    stack=[]
    open_brac=["[","(","{"]
    for i in expr:
        if i in open_brac:
            print(i)
            stack.append[i];
        
        
        elif(i==stack.pop()):
              continue
            

        elif (len(stack)<=0):
            return "balanced";            
                
        else:
            return "unbalanced"

if __name__ == '__main__':    
    a=input()
    print(a,"-",check(a))        