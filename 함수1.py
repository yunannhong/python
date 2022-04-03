def f(x,y): #함수를 직접 정의할때에는 정의(define)의 def를 사용
    if x > y:
        return x
    else :
        return y
#함수 정의

a=int(input())
b=int(input())
print(f(a,b)) #함수 호출