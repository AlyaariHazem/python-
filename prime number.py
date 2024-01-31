x=int(input('enter prime number or none '))
def check():
    for a in range(2,int(x/2)):
        if x&a==0:
            return 0
            break
    return 1
y=check()
if y==0:
    print('this number is not prime number : ')
else:
    print('this number is prime number : ')
