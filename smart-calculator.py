


from collections import deque

###


dic= {}

intl = ('1','2','3','4','5','6','7','8','9')



def lef(ls):
    for j in ls:
        if j in intl:
            print("Invalid identifier")
            return 0
    return 1
    

def right(ls):
    try:
        
        if ls in dic:
            return 2
        int(ls)
        return 0
    except ValueError:
        if ls not in dic :
            flag = 1
        alpha =0
        num=0
        for j in ls:
            if j not in intl:
                alpha = 1
            elif j in intl:
                num = 1
            if(alpha == 1 and num ==1):
                flag = 2
                break
        if flag == 1:
            print("Unknown variable")
            return 1 
        else:
            print("Invalid assignment")
            return 1

def infix_post(y): ### passing a list
    stack = deque()

    oper = {'*': 1 , '/': 1 ,'+': 2, '-': 2}

    par = ["(", ")"]

    result = ''
    
    
    for j in y :
        if (j not in oper) and (j not in par):
            result += j + ' '
        else:
            x = 0
            if (len(stack) != 0):
                x = stack.pop()
                stack.append(x)
            if(len(stack)==0 or x == "("):  # if satck is empty add operator
                stack.append(j)
            
            else: 
                if j in oper:
                    if (len(stack) != 0):
                        x = stack.pop()
                        stack.append(x)
                        ###print(stack)
                    while(len(stack)!= 0 and ( oper[j] >= oper[x] ) and x != '(' ):
                        result += stack.pop() + " "
                    ###print("added to result") 
                        if (len(stack) != 0):
                            x = stack.pop()
                            stack.append(x)
                    else:
                        stack.append(j)
                else:
                    if (j == "("):
                        stack.append(j)
                    else:
                        if (len(stack) != 0):
                            x = stack.pop()
                            stack.append(x)
                        while(x != '('):
                            result += stack.pop() + " "
                            if (len(stack) != 0):
                                x = stack.pop()
                                stack.append(x)
                        else:
                            stack.pop()
                
    while(len(stack)!= 0 ):
        result += stack.pop() + " "
    
    return(result)


def cal(s):
    stack = deque()  
    ls = ['*', '/', '+', '-']
    y = s.split()
    
    for j in y:
        if j not in ls:
            stack.append(j)
        else:
            if j =="+":
                x = int(stack.pop())
                y = int(stack.pop())
                r = y+x
                stack.append((r))
            elif j =="-":
                x = int(stack.pop())
                y = int(stack.pop())
                r = y-x
                stack.append((r))
            elif j =="*":
                r = int(stack.pop()) * int(stack.pop())
                stack.append(r)
            elif j =="/":
                x = int(stack.pop())
                y = int(stack.pop())
                r = y/x
                stack.append(r)
    return(stack.pop())



def check(s):
    y  = s.split()
    if(len(y)>1):
        for i in y:
            if (i.count("*")) >1 or (i.count('/')>1):
                print("Invalid Expression")
                return 1
    if( s.count('(') != s.count(')') ):
        print("Invalid Expression")
        return 1
 
    stack = deque()
    if(len(y)>1):
        for i in range(len(y)):
            if y[i].count('+')>=1 or y[i].count('-')>1:
                x = y[i]
                stack.append(x[0])
                for j in range(1,len(x)):
                    n = stack.pop()
                    if(n != x[j]):
                        stack.append('-')
                    else:
                        stack.append('+')
                y[i]= stack.pop()   
        s = " ".join(y)
    return (s)



ls = ['*', '/', '+', '-', '(', ')','=']

while True:
    a = input()
    c = a
    if(a== "/exit"):
        print("Bye!")
        break
    elif(a=='/help'):
        print("The program calculates the sum of numbers")
        continue
    elif(a == ''):
        continue
    elif (a[0]=='/'):
        print("Unknown command")
        continue
    else:
        y = check(a)
        if(y !=1):
            a = y
            for i in ls:
                y = a.split(i)
                a = " {} ".format(i).join(y)
            y = a.split()
            b = y
            y = a.split()
            a = "".join(y)
            x = a.find("=")
    
            if(x>0):
                if (lef(a[0:x]) == 1):
                    ri = right(a[x+1:])
                if(ri==0):
                    dic[a[0:x]] = a[x+1:]
                elif(ri==2):
                    dic[a[0:x]] = dic[a[x+1:]]
                
                continue
            y = b
            for j in range(len(y)):
                if y[j] in dic:
                    y[j] = dic[y[j]]
            
            if("+" in y or '-' in y or '*' in y or '/' in y):
                conv = infix_post(y)
                print(cal(conv))
            
            else:
                try:
                    a = c
                    print(dic[a])
                except Exception:
                    print("Unknown variable")
            
