
def main():
    a = "Harvard"
    b = "Stamford"
    n = 2


    listA = []
    for i in range(len(a)-n+1):
        tokenA = a[i:i+n]
        listA.append(tokenA)

    listB = []
    for i in range(len(b)-n+1):
        tokenB = b[i:i+n]
        listB.append(tokenB)

    #print(listA)
    #print(set(listA))
    #print(list(set(listA)))

    listA = list(set(listA))
    listB = list(set(listB))

    print('line 25' , intersection(listA,listB))


def  intersection(resultA, resultB):
    finalResult = list(set(resultA) & set(resultB))
    return finalResult

if __name__ == '__main__':
    main()
