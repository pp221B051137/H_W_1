n , m = map(int,input().split())
# n , m = 7, 5
A = [" "]*n
for i in range(n):
  A[i] = [" "]*m

for i in range(n):
  for j in range(m):
    if i == 0 or j == 0 or i ==n-1 or j == m-1:
      A[i][j] = "*" 
for i in range(n):
  for j in range(m):
    if i == (n-1)/2:
        A[i][j] = "*" 
for i in range(n):
    for j in range(m):
        #
        if i == 0 and j == m-1 or i ==(n-1)/2 and j == m-1 or i == m-1 and j == m-1 or i == m and j == m-1:
            A[i][j] = " "
for i in range(n):
    for j in range(m):
        if i == m-1 and j==(m-1)/2 or i == m and j == ((m-1)/2)+1:
           A[i][j] = "*" 
for i in range(n):
    for j in range(m):
        if i == n-1 and j != 0 and j != m-1:
            A[i][j] = " "




for row in A:
   print(''.join(list(map(str,row))))