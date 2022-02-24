a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

d=(a if (a<b) else b)
e=(b if (b<c) else c)
f=(d if (d<e) else e)
print(f)


#if문 사용 방법
# x if (조건문) else y
# 조건문 만족시 x 출력, 아니면 y출력