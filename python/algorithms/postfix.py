from stack import stack
expression=str(input('Enter postfix expression: '))
s1=stack()
operations=['+','-','*','/']
for i in expression:
    if i in operations:
        a=int(s1.POP())
        b=int(s1.POP())
        
        if i=='+':
            summ=a+b
            s1.push(summ)
        elif i=='*':
            mult=a*b
            s1.push(mult)
        elif i=='/':
            div=b/a
            s1.push(div)
        elif i=='-':
            diff=b-a
            s1.push(diff)
        else:
            pass
    else:
        s1.push(i)
print(s1)
        
        
   
        
