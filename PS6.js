//Day of the Programmer: 256th day of the year
// durante un año en el rango inclusivo de 1700 s 2700.
// 1700 to 1917, Julian calendar; 
// Since 1919 Gregorian calendar

//QUEDE ACA:
// Pasaron a gregoriano en 1918, when the next day after January 31st era Febrero 14th. 
// Significando que en 1918, Febrero 14th was the 32nd day of the year in Ru.
// Febrero tiene; 29 days during a leap year, and 28 during others. 
// In the Julian calendar, los años bisiestos son divisibles by 4; 
// In the Gregorian calendar, los años bisiestos are Divisible by 400 or Divisible by 4 and not divisible by 100.
// Given a year, encuentra la fecha del 256th day of that year according to the official Ru calendar ese año. 
//imprimirla en el formato dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit mes, and yyyy año .

//Tipo 1984. divisible en 4, so it is a leap year. 
//The 256th day of a año bisiesto after 1918 is September 12, so the answer is 12.09.1984

const DiaProgramador=256
var dia=0
var anio=0
calendario=""
if ( anio =>1700 && anio <=2700 ){
    if (anio =>1700 && anio <=1917){
        console.log("Julian");
    } else if(anio>=1918 && anio <=2700 ){
        console.log("Gregorian");
    }   

}


if (anio==1918){
    if(dia ==31){
        dia32= 45

    }
} else if ( calendario=="Julian"){
    febrero=30
}

if (anio=julian){
    febrero="bisiesto"

}

