def isvalid(x,y):
    global N,M
    if x > 0 and y > 0 and x < N and y < M and isPrime(maze[x][y]):
       return True
    return False

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
    for i in range(N):
			  if isPrime(maze[0][i]):
			     visited[0][i] = 1
			  else:
			     visited[0][i] = 0
    for i in range(M):
		    if isPrime(maze[i][0]):
		       visited[i][0] = 1
		    else:
		       visited[i][0] = 0
    for i in range(N+1):
		    for j in range(M+1):
		        c = 0
		        arr = []
		        if isPrime(maze[i][j+1]):
		           c += visited[i][j+1]
		           arr.append(((j+1)+1,i+1))
		        if isPrime(maze[i+1][j]):
		           c += visited[i+1][j]
		           arr.append((j+1,(i+1)+1))
		        if isPrime(maze[i+1][j+1]):
		           c += visited[i+1][j+1]
		           arr.append(((j+1)+1,(i+1)+1))
		        visited[i][j] = c
		        print(sorted(arr))
		        mainArr.append((sorted(arr)))
		        print(mainArr)
    return visited

N = 3
M = 3

maze = [[2,3,7],[5,4,2],[3,7,11]]
visited = [[0,0,0],[0,0,0],[0,0,0]]
count = 0
mainArr = []
print(noofpath(maze,visited))
