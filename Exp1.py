num1=input('Enter first number')
num2=input('Enter second number')


sum=float(num1)+float(num2)
sub=float(num1)-float(num2)
mul=float(num1)*float(num2)
div=float(num1)/float(num2)

print('The sum of {0} and {1} is {2}'.format(num1,num2,sum))
print('The subraction of {0} and {1} is {2}'.format(num1,num2,sub))
print('The mutiply of {0} and {1} is {2}'.format(num1,num2,mul))
print('The division of {0} and {1} is {2}'.format(num1,num2,div))

if(num2>num1):
    print('The subraction result will always be negative')
else:
    print('The result will be positive')

count=0
while(count <= 5):
    print('Lets Go')
    count=count+1
    

for i in range(0,5):
    print('HEllo')
print('THE END') 

