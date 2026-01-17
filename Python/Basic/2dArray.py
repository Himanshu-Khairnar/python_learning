arr1=[[0,0,0],[0,0,0],[0,0,0]]
arr2=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        arr1[i][j]=int(input(f"Enter the element of row {i} at position {i},{j}: "))
        
for i in range(3):
    for j in range(3):
        arr2[i][j]=int(input(f"Enter the element of row {i} at position {i},{j}: "))
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        result[i][j] = arr1[i][j]+arr2[i][j]

for i in range(3):
    print(f"{result[i][0]} | {result[i][1]} | {result[i][2]}")