import math
import utils # provided in contest files

PLAYER_NAME='fatant' 
dic=utils.get_common_unique_words_from_corpus("the_adventures_of_sherlock_holmes.txt")
chars="abcdefghijklmnopqrstuvwxyz1234567890'"

def gKD(): # failed attempt of using keyboard mapping
    return {}
    kb = [
        "qwertyuiop",
        "asdfghjkl ",
        "zxcvbnm   "]
    os,rv=[0.25,0.75],{}
    for x in range(2):
        for y in range(10):
            ch = kb[x][y]
            if ch == ' ':
                continue
            for a in range(2):
                for b in range(10):
                    c2 = kb[a][b]
                    if c2 == ' ':
                        continue
                    d, m = math.sqrt((x-a+os[x]-os[a])*(x-a+os[x]-os[a])+(y-b)*(y-b)), 0.25
                    m=0.25
                    if d<1.0+m and d>=1:
                        rv[c2+ch]=rv[ch+c2]=d-m
    return rv

keyd = gKD()

def lev(w1,w2):
    x,y=len(w1)+1,len(w2)+1
    rv=[[0 for j in range(y)]for i in range(x)]
    for i in range(x):rv[i][0]=i
    for j in range(y):rv[0][j]=j
    for j in range(1, y):
        for i in range(1, x):
            rem,ins,sub,swap= rv[i-1][j]+0.97**((i+j)/2), rv[i][j-1]+1.2, rv[i-1][j-1], 99
            if w1[i-1]!=w2[j-1]:sub+=(keyd[w1[i-1]+w2[j-1]] if (w1[i-1]+w2[j-1]) in keyd else 1.2)
            if sorted(w1[i-1:i+1])==sorted(w2[j-1:j+1]):
                if w1[i-1:i+1] == w2[j-1:j+1]:
                    swap=rv[i-1][j-1]
                else:
                    swap=rv[i-1][j-1]-(keyd[w1[i-1]+w2[j-1]] if (w1[i-1]+w2[j-1]) in keyd else 1.2)/2
            rv[i][j]=min(rem,ins,sub,swap)
    return rv[len(w1)][len(w2)]

def let2(w1,w2):
    rv=0
    diff={}
    for c in chars:
        d = w1.count(c)-w2.count(c)
        if d: diff[c] = (abs(d),abs(d)/d) 
        c=[]
        for k in diff:
            for m in diff:
                if m < k or diff[k][1] == diff[m][1]: continue
                km = k+m
                if km in keyd:
                    c.append((keyd[km],km))
        c.sort()
        rv = 0
        for d,p in c:
            f,s=p[0],p[1]
            if diff[f][0] <= diff[s][0]:
                f,s=s,f
            rv += 2*d * abs(diff[s][0])
            diff[f] = (diff[f][0]-diff[s][0], diff[f][1])
            diff[s] = (0, 0)
            for k in diff:
                rv += diff[k][0]
            return rv

def let(w1,w2):
    rv=0
    for c in chars: rv+=abs(w1.count(c)-w2.count(c))
    return rv

def func(lev,let,freq):
    return (lev+let*0.25)**2-math.log(freq)/math.log(7)

def autocorrect(uw):
    pos=(len(uw)>2 and ("'s"in uw or "s'" in uw))
    i,alev,dist,lim=0,[],[],5
    for word in dic:
        if len(word) == 1: continue
        clet,freq=let(word, uw),dic[word]
        if clet/(len(uw)+len(word)) < .4 or clet <= 2:
            clev=lev(word,uw)
            alev+=[clev]
            clet=let2(word,uw)
            dist+=[[func(clev,clet,freq),clev,clet,-dic[word],word]]
        if i%lim==0:
            dist.sort()
            alev.sort()
            i+=1
    dist.sort()
    ret=dist[0][-1]
    if not"'"in ret and pos:ret+="'s"
    if ret==uw:ret=dist[1][-1]
    if not"'"in ret and pos:ret+="'s"
    return ret