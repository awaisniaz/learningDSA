def findTheElementPosition():
    element = max([1,3,5,6])
    data = [1,3,5,6]
    target = 5
    position = 0
    for i in range(element):
        if(target > element):
             position = len(data)
        elif (target < data[0]):
               position =  0
        else:
            for i in range(len(data)):
                if(target > data[i]):
                    position = i+1
    return position

print(findTheElementPosition())