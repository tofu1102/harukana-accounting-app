import heapq

def optimizedAccounting(values):
    """
    最適化されたvaluesを返す
    """
    newValues = [[0] * len(values) for i in range(len(values))]
    sumList = []
    for i in range(len(values)):
        sum = 0
        for j in values[i]:
            sum += j
        sumList.append(sum)
    while(1):
        if sumList == [0]*len(values):break
        Plus = [sumList.index(heapq.nlargest(1,sumList)[0]),heapq.nlargest(1,sumList)[0]]
        Minus = [sumList.index(heapq.nsmallest(1,sumList)[0]),heapq.nsmallest(1,sumList)[0]]
        if abs(Plus[1])>abs(Minus[1]):
            newValues[Minus[0]][Plus[0]] = -1*abs(Minus[1])
            newValues[Plus[0]][Minus[0]] = abs(Minus[1])
            sumList[Minus[0]] += abs(Minus[1])
            sumList[Plus[0]] -= abs(Minus[1])
        else:
            newValues[Minus[0]][Plus[0]] = -1*abs(Plus[1])
            newValues[Plus[0]][Minus[0]] = abs(Plus[1])
            sumList[Minus[0]] += abs(Plus[1])
            sumList[Plus[0]] -= abs(Plus[1])


    return newValues
