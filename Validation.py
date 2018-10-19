N=int(input())
for i in range(N):
    number=input()
    if number[0]=='7' or number[0]=='9' or number[0]=='8' and len(number)==10 and number.isdigit()==True:
     print("YES")
    else:
     print("NO")
