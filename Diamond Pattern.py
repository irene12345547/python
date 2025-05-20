RowSize = int(input("Enter the Number of Rows:"))
if RowSize%2==0: 
    HalfDiamrRow = int(RowSize/2)
else:
    HalfDiamRow = int(RowSize/2)+1
space = HalfDiamRow-1
for i in range(1, HalfDiamRow+1):
  for j in range(1, space+1):
    print(end=" ")
   space = space-1
  num = 1
  for j in range(2*i-1):
     print(end=str(num))
     num = num+1
  print()
space = 1
for i in range(1, HalfDiamRow):
  for j in range(1, space+1):
    print(end=" ")
   space = space+1
  num = 1