x = 1
for i in range(13,8,1):
    y = (x*i)
    print
print('-------------------------------')
rinda = 7
for i in range(0,rinda):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(rinda, 0, -1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")