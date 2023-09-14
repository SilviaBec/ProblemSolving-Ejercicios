def ejercicio(ano):
    enAgBisiesto=244 
    enAgNormal=243
    #de enero a agosto no hay 230 dias es el 230avo dia del año
    enAg1918=230
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
        

        #1918 NO FUE BISIESTO feb=28 d
    if ano ==1918:
        dia=diaprogram-enAg1918
        rta=[str(dia),"09",str(ano)]
        print(".".join(rta))
        
(ejercicio(1918))