n = int(input())
zeus = list(map(int, input().split()))

def checkSorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))

#first check if it is not sorted then print it and exit
if not checkSorted(zeus):
    #apparently we still need a change, wtf..
    flag = False
    for i in range(n-1):
        if zeus[i] > zeus[i+1] and not flag:
            print(zeus[i]+1, end=' ')
            flag = True
        else:
            print(zeus[i], end=' ')
    print(zeus[n-1])
    #for num in zeus:
    #    print(num, end=' ')
    raise SystemExit

lenNums = []
for i in range(n):
    lenNums.append(len(str(zeus[i])))

lenNums.sort(reverse=True)
saveIt = 0 #save the second last num (first in second last)
#print(lenNums)
if lenNums[0] > lenNums[1]: # if the last number is bigger in len than sec last
    print('impossible')
elif len(set(lenNums)) == 1: 
    # if all have same lengths we can just replace first one and then its not sorted
    
    if lenNums[0] == 1:
        #all are single digits, check if last one is 9 its impossible
        if zeus[n-1] == 9:
            print('impossible')
        else:
            #its possible so print 
            print(zeus[n-1]+1, end=' ')
            for i in range(1, len(zeus)):
                print(zeus[i], end=' ')
    else: #all here are atleast >= 2
        #PROBLEM we need to do better 
        # we can put the first digit in the number to be 9 (highest) and then check if its sorted or not
        res2 = []
        put = '9' + str(zeus[0])[1:]
        res2.append(int(put)) # first number done 
        # put rest
        for i in range(1, len(zeus)):
            res2.append(zeus[i])
        if checkSorted(res2):
            #or reduce the last
            put = '1' + str(zeus[n-1])[1:]
            res2.pop()
            res2.append(int(put))
            if checkSorted(res2):

                print('impossible')
            else:
                print(*res2)
        else:
            print(*res2)
        
        #for i in range(n):
        #    if i == 0:
        #        print(zeus[i]+1, end=' ')
        #    else:
        #        print(zeus[i], end=' ')
else:
    #its different lengths we can then change the last numbers (first num to be smaller than first in sec last)
    # if the numbers is 1 its a different case, we need to take the last (non zero) and make it zero
    #  then check if it is sorted or not
    ans = []
    flag = False # check if its the first digit of the last number or another.
    # it matters because if its the first digit then its easy and we just 
    for i in range(n):
        if i == n - 1:
            #make it a list of numbers and print them seperatly
            #res = [int(d) for d in str(zeus[i])[1:]]
            #ans.append(saveIt-1)
            #print(saveIt-1, end='') #print the number - 1
            #putThis = str(saveIt-1)
            #for h in res:
            #    putThis += str(h)
            #ans.append(int(putThis))
            ans.append(zeus[i])
            if checkSorted(ans):
                # its impossible to make the second last bigger, so lets make the last smaller
                ans = []
                for j in range(n):
                    if j == n - 1:
                        #first = int(str(zeus[i])[0])
                        takeIt = int(takeIt) - 1
                        if takeIt > 0:
                            this = str(takeIt) + str(zeus[j])[1:]
                            ans.append(int(this))
                            if checkSorted(ans):
                                print('impossible')
                            else:
                                print(*ans)
                        else:
                            #fix later?
                            print('impossible')

                    elif j == n - 2:
                        takeIt = str(zeus[j])[0]
                    ans.append(zeus[j])
                #print('impossible')
            else:
                print(*ans)
                #print(*ans)
            #print(ans)
            #print(*res, sep='')
            #print(zeus[i][0] + 1, zeus[i][1:], sep='', end=' ')
        elif i == n - 2:
            # if its the second last just put a 9 in the beginning.

            this = '9' + str(zeus[i])[1:]
            ans.append(int(this))
        else:
            ans.append(zeus[i])
            #print(zeus[i], end=' ')
#3
#1 13 14
#1 13 4