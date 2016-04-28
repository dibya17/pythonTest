from functools import reduce
def checkcontconsonant(teststringX):

    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    #testStringL = teststringX.lower()
    vowelCount=reduce(lambda x,y:int(x)+int(y),map(lambda a:a in VOWELS,  teststringX))
    stringsize=len(teststringX)
    consCount=stringsize-vowelCount


    if vowelCount >= consCount:
        if stringsize >= 3:
            for i in range(stringsize):
                if (teststringX[i] not in VOWELS) and (teststringX[i+1] not in VOWELS) and 	(teststringX[i+2] not in VOWELS):
                    print("hard")
                    return 0
            print("easy")
            return 0
        else:
            print("easy")
            return 0

    elif consCount>vowelCount:
        print("hard")
        return 0

testnumber = int(raw_input())
#print(str(testnumbers))
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

if (testnumber >=1) or (testnumber<=50):
    for j in range(int(testnumber)):
        teststringM=str(raw_input())
        testlen=len(teststringM)
        #print(str(j)+" "+teststring)
        if testlen>=1 or testlen<=50:
            checkcontconsonant(teststringM)