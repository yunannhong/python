def f(x,y):
    if x>y:
        return x
    else :
        return y

a,b,c=map(int, input().split()) #입력받은 여러개의 문자열을 모두 int로 변환
print(f(f(a,b),c))
