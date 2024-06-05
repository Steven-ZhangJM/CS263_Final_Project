

fact1=1                            #factorial of 0 is 1
fact2=1                                        #factorial of 1 is 1
n=2                              #1!=1, 2!=2 (2!=4&3 for all i in the range 1,2)
for i in range (1,n+1):                         #for i = 1, 2,..., n-1
    x=i*10+i                                   #x=10 i + i
    fac1=fact1*x
    fac2=fact2*x
    fac3=fac2-fac1
    print(x,fac1,fac2,fac3)
    fact1=fac1                                  #fac1=(10*i+i+1)*i
    fact2=fac2
