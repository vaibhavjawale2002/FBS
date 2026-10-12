def bubbleSort(li):
    size = len(li)
    for i in range(1, size):         
        for j in range(0, size-i):   #fun use in pattern 7-i
            if(li[j] > li[j+1]):
                li[j] ,li[j+1] = li[j+1], li[j]
                print(li)
li = [45,29,13,40,15,32]
print("Before Sorting:", li)
bubbleSort(li)
print("After Sorting:",li)