a=int(input())
total=0

for i in range(1,a+1) :
    total = i + total
    if total>=a :
        print(i)
        break