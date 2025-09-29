n = int(input())
stacks = list(map(int, input().split()))
summed = sum(stacks)

def findTwoRandom(a):
    findIndex1 = findIndex2 = -1

    for i, v in enumerate(a):
        if v <= 0:
            continue
        if findIndex1 == -1 or v > a[findIndex1]:
            findIndex2 = findIndex1
            findIndex1 = i
        elif findIndex2 == -1 or v > a[findIndex2]:
            findIndex2 = i
    return findIndex1, findIndex2

if summed % 2 == 1 or 2 * max(stacks) > summed:
    #not possible if the sum is odd (1 will be left out)
    #also not possible if one of the stacks is too big for the (A, B) to pick from
    print('no')
else:
    print('yes')
    
    # find 2 random stacks that is more than 0 (NOT SAME STACK)
    while summed != 0:
        findIndex1, findIndex2 = findTwoRandom(stacks)
        
        
        stacks[findIndex1] -= 1
        stacks[findIndex2] -= 1
            
        print(findIndex1+1, findIndex2+1)

        summed -= 2