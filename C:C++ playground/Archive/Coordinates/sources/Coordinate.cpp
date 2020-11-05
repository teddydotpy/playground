#include "../headers/Coordinate.h"
#include <iostream>
#include <iomanip>
#include <QString>

Coordinate::Coordinate()
     :degrees(0), minutes(0), seconds(0), direction("")
{

}

Coordinate::Coordinate(int con_deg, int con_min, int con_sec , QString con_dirs)
{
    degrees = con_deg ;
    minutes = con_min ;
    seconds = con_sec ;
    direction = con_dirs ; 
}

QString Coordinate::toString(){
    QString output = QString(" %L1%L2 %L3\' %L4\" ").arg(degrees).arg(QChar(0260)).arg(minutes).arg(seconds);
    return  output + direction.toUpper();
}

double Coordinate::toDecimal(){
    double dec_Degrees, dec_Minutes, dec_Seconds;
    bool dec_Direction;

    dec_Seconds = seconds/3600.00;
    dec_Minutes = minutes/60.00;
    dec_Degrees = degrees + dec_Minutes + dec_Seconds;

    if(direction.toLower() == 'n' || direction.toLower() == 'e'){
        dec_Direction = true;
    } else
    {
        dec_Direction = false ;
    }
    
    return dec_Direction ? dec_Degrees : -dec_Degrees ;
}