#Q1
def multiplication_table(m,n):
    for i in range (1,10):
        for j in range(m,n+1):
            print (('%sX%s=%s\t')%(j,i,j*i),end='')
        print("");
    print("");
multiplication_table(1,3)
multiplication_table(4,6)
multiplication_table(7,9)



#Q2
def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'*'*(2*i+1))
pyramid(15)
