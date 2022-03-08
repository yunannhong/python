n=int(input("학생의 수를 입력하세요: "))
a=[0]*n #리스트를 a라는 이름으로 생성하고, 초기값을 모두 0으로 지정
mx=0 #최고점수
for i in range(n):
    a[i]=int(input("%d번 학생의 성적을 입력하세요" %(i+1)))
    if mx<a[i]:
        mx=a[i]
print("최고 점수는 %d점입니다" %mx)