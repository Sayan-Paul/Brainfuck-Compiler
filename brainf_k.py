import sys
ls=sys.stdin.readlines()
p=""
for l in ls:
    for c in l:
        if c=='%':
            break
        if ord(c)!=10 and ord(c)!=13 :
            p+=c
f,ct,pt,i=0,0,0,0
t,ans,stk=[0]*32768,"",[]
while(i<len(p)):
    c=p[i]
    if c=='+':
       t[pt]+=1
       t[pt]%=256
    if c=='-':
       t[pt]-=1
       if t[pt]<0:
           t[pt]=255
    if c=='<':
        pt-=1
        if pt<0:
            pt=32767
    if c=='>':
        pt+=1
	pt%=32768
    if c=='.':
        ans+=chr(t[pt])
    if c=='[':
        ct+=1
        stk.append(i)
    if c==']':
        ct-=1
        if ct<0:
            f=1
            break
        if t[pt]:
            i=stk[-1]
            continue
        else:
            o=stk.pop()
    i+=1
print ("COMPILE ERROR" if f else ans)
