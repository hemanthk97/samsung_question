N = 3 #length of Array A
Q = 2 #lenght quries array Q
A = [2,4,8]
NQ = [(1,3),(2,3)]





try:
square_root_of_five = 5**0.5
Phi = (1 + square_root_of_five) / 2
phi = (1 - square_root_of_five) / 2
series = [int((Phi**n - phi**n) / square_root_of_five) if n<45 else int((Phi**n - phi**n) / square_root_of_five)%10**9+7 for n in range(1, max(A)+1) ]
serRes = [series[x-1] for x in A]
for i in NQ:
    temp1 = i[0]
    temp2 = i[1]
    if i[0] == 1:
       print(GCD(serRes[:temp2]))
    else:
       print(GCD(serRes[temp1-1:temp2]))
   
    
