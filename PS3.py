def birthday(s, d, m):
    resultado2=[]
    for x in s:
        if x+s[s.index(x)+1] ==d:
            resultado =x,s[s.index(x)+1]
            if resultado not in resultado2:
                resultado2.append(resultado)
    if len(resultado2)==m:
        print(len(resultado2))
        
        
birthday([1,2,1,3,2],3,2)