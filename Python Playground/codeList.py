 #! /usr/bin/env python3

codeList = ['INF1511' , 'COS2626', 'COS2601', 'INF1505', 'COS2611'] 

codeFirst = codeList[0]
codeLast = codeList[-1]
codeListLen = len(codeList)

print("The first item on the list is: " + codeFirst)
print("The last item on the list is: " + codeLast)
print("The amount of items in the list is: " + str(codeListLen) + " items.")

for i in range(codeListLen):
    print("Item No. " + str(i+1) + " is: " + codeList[i])

