s=[18,77,68,54,99,15,56,97,64,48]
for i in range(0,9): #i=0~8
    for j in range(i+1,10): #j=1~9
        if s[i]>s[j]: #01 02 03 04 05 06 07 08 09
            t=s[i]    #큰게 t
            s[i]=s[j] #작은게 s[i]
            s[j]=t    #큰게 s[j]
for i in range(0,10):
    print(s[i],end=' ')