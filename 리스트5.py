n=int(input("학생의 수를 입력하세요 : "))
a=[0]*n
min=100
for i in range(n):
    a[i]=int(input("%d번 학생의 성적을 입력하세요 : " %(i+1)))
    if a[i]<min:
        min=a[i]
print("최저 점수는 %d점입니다" %min)