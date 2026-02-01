#input= 12541 d=1
#output= 2541

import sys
input = sys.stdin.readline
n=input() #584675  587465
d="7"
ans=[]

for i in range(len(n)):
    if n[i]==d:
        ans.append(int(n[0:i]+n[i+1:len(n)]))
print (max(ans))