# 1.

"""1 2 3
   1 2 3
   1 2 3"""

# n = int(input("enter a number"))
# i = 1
# while i<=n :
#   j=1
#   while j<=n:
#     print(j,end=" ")
#     j=j+1
#   print()
#   i=i+1


# 2.

"""3 2 1
   3 2 1
   3 2 1"""

# n = int(input("enter a number"))
# i = n
# while i>=1 :
#   j=n
#   while j>=1:
#     print(j,end=" ")
#     j=j-1
#   print()
#   i=i-1


# 3.

"""1 2 3 
   4 5 6 
   7 8 9 """

# n = int(input("enter a number"))
# i = 1 
# num = 1
# while i<=n :
#     j=1
#     while j<=n:
#         print(num , end=" ")
#         num = num+1
#         j=j+1
#     print()
#     i=i+1
    
# 4.

"""9 8 7 
   6 5 4
   3 2 1 """

# n = int(input("enter a number"))
# i = 1 
# num = n*n
# while i<=n :
#     j=1
#     while j<=n:
#         print(num , end=" ")
#         num = num-1
#         j=j+1
#     print()
#     i=i+1


# 5.

"""1 
   2 2 
   3 3 3 """

# n = int(input("no of rows"))

# for i in range(1,n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# 6.

"""1 
   2 3 
   3 4 5  """

# n = int(input("no of rows"))

# for i in range(1,n+1):
#     for j in range(i):
#         print(j+i, end=" ")
#     print()


# 7.

"""1 
   2 1 
   3 2 1  """

# n = int(input("no of rows"))

# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()


#8.

# 1 1 1 1 
#   2 2 2 
#     3 3 
#       4 

# n = int(input("no of rows"))
# i= 1
# while(i<=n):
#     space = 1
#     while(space < i):
#         print(" ",end=' ')
#         space = space+1
#     j=1
#     while(j <= n-i+1):
#         print(i, end=' ')
#         j=j+1
#     i=i+1
#     print()


# 9.

#    1
#   22
#  333
# 4444

# n=int(input('enter row no.'))
# i=1
# while(i<=n):
#    space = 1
#    while(space <= n-i):
#       print(" ", end='')
#       space=space+1
#    j=1
#    while(j <= i ):
#       print(i,end='')
#       j=j+1
#    i=i+1
#    print()

# 10.

#       1 
#     1 2 1 
#   1 2 3 2 1 
# 1 2 3 4 3 2 1 

# n= int(input("enter no of rows"))
# i=1
# while(i<=n):
#    space =1
#    while(space <= n-i):
#       print(" ",end=' ')
#       space=space+1
#    j=1
#    while(j<=i):
#       print(j,end=' ')
#       j=j+1
#    k=i-1
#    while(k>=1):
#       print(k,end=' ')
#       k=k-1
#    i=i+1
#    print()

# 11.

# 1234554321
# 1234**4321
# 123****321
# 12******21
# 1********1

n= int(input("enter no of rows"))
i=1
while(i<=n):
   k=1
   while(k<=n-i+1):
      print(k,end='')
      k=k+1
   j=1
   while(j<=2*(i-1)):
      print("*",end='')
      j=j+1
   l=n-i+1
   while(l>0):
      print(l,end='')
      l=l-1
   i=i+1
   print()