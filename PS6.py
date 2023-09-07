def ejercicio(ano):
    enAgBisiesto=244 
    enAgNormal=243
    diaprogram=256
    if ano >=1700 and ano <=1917:
        if ano%4==0:
            dia=diaprogram-enAgBisiesto
            print(dia,'.','09','.',ano)
        else:
            dia=diaprogram-enAgNormal
            print(dia,'.','09','.',ano)
    elif ano>=1919 and ano <=2700:
        
        if ano%400==0 or (ano%4 ==0 and ano%100 !=0):
            dia=diaprogram-enAgBisiesto
            print(dia,'.','09','.',ano)
        else:
            dia=diaprogram-enAgNormal
            print(dia,'.','09','.',ano)
        

(ejercicio(2016))