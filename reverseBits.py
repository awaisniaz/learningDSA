def reverseBit(number):
    print(bin(number)[2:])
    originaldata = str(bin(number)[2:])
    difference = 32-len(originaldata)
    val = originaldata[::-1] + ("0"*difference)
    decimalNumber = 0
    counter = 0
    N= len(val) - 1
    print(val)
    for i in range(N,0,-1):
        print(i)
        decimalNumber = decimalNumber + int(val[i])*2**counter
        counter = counter + 1
        # i = i -1
    
    print(decimalNumber)
    # print(n)
    # binary = bin(n)
    # print(binary )
    # rep = str(binary)[2:]
    # difference = 32-len(rep)
    # print(difference)
    # val = rep[::-1] + ("0"*difference)
    # print(int(val,2))
    # return int(val,2)

reverseBit(43261596)