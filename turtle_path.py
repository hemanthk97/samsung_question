
def isPrime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	      return False
    return True



def noofpath(maze,visited):
    global N,M,mainArr
    visited[0][0] = 1
    mainArr =[]
    for i in range(1,N):
			  if isPrime(maze[0][i]):
			     visited[0][i] = visited[0][i-1]
			  else:
			     visited[0][i] = 0
    for i in range(1,M):
		    if isPrime(maze[i][0]):
		       visited[i][0] = visited[i-1][0]
		    else:
		       visited[i][0] = 0
    for i in range(1,N):
		    for j in range(1,M):
		        c = 0
		        maxarr = []
		        if isPrime(maze[i-1][j]):
		            c += visited[i-1][j]
		            maxarr.append((int(i-1)+1,j+1))
		        if isPrime(maze[i][j-1]):
		            c += visited[i][j-1]
		            maxarr.append((i+1,int(j-1)+1))
		        if isPrime(maze[i-1][j-1]):
		            c += visited[i-1][j-1]
		            maxarr.append((int(i-1)+1,int(j-1)+1))
		        visited[i][j] = c
		        if len(maxarr)> 0:
		           mainArr.append(max(maxarr))
		        		    
    i = len(mainArr)
    temp = []
    while i > 1:
          i = i - 1
          if sorted(mainArr[i]) == sorted(mainArr[i-1]):
		          temp.append(i)
		          temp.append(i-1)
    for i in temp:
        mainArr.pop(i)
    return visited[N-1][M-1]

N = 3
M = 3

maze = [[2,4,6],[8,9,10],[12,14,15]]
visited = [[0,0,0],[0,0,0],[0,0,0]]
count = 0
mainArr = []
print(noofpath(maze,visited))
print([(1,1)]+mainArr+[(N,M)])

			