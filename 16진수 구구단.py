

#모범답안

n=int(input(),16) #15(F)까지 16진수로 입력받기

for i in range (1,16) : #1-15까지 i 대입
    print("%X*%X=%X"%(n,i,n*i))
