# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*',end=' ')
#     for j in range(1, 6-i):
#         print(' ',end=' ')
#     for j in range(6,10-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         if(i!=5 or j!=5): #(This condition use ony remove the extra *)

#             print('*',end=' ')
#     print()

k=7
for i in range(1, 6):
    for j in range(1, i+1):
        print('*',end=' ')
    for j in range(1, k+1):
        print(' ',end= ' ')
    k-=2
    for j in range(1,i+1):
        if(i!=5 or j!=5): #(This condition use ony remove the extra *)
    
            print('*',end=' ')
    print()
