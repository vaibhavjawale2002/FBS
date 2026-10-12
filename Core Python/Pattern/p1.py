# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*",end = ' ')
#     print()


#use i
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i,end = ' ')
#     print()

#use j
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j,end = ' ')
#     print()


# for i in range(1,6):
#     for j in range(1, 7-i):
#         print("*",end = ' ')
#     print()

# for i in range(1, 6):
#     for j in range(1, 7-i):
#         print(i,end = ' ')
#     print()

# for i in range(1, 6):
#     for j in range(1, 7-i):
#         print(j,end = ' ')
#     print()

# for i in range(1, 6):
#     for j in range(6-i, 0,-1):
#         print(j,end = ' ')
#     print()


for i in range(1, 6):
    for j in range(1, i):
        print(' ', end=' ')
    for j in range(6-i, 0,-1):
        print(j,end=' ')
    print()
    