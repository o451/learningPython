def prime(n):
    i =2
    while(i < n):
        j = 2
        while(j<= i/j) :
            if i%j :
                j = j+1
            else :
                break
        else :
            print(i, end=' ')
        i = i +1

prime(100)

