#include "../headers/GPSCoord.h"
#include <QDebug>
#include <QString>

GPSCoord::GPSCoord(){
    latitude = new Coordinate(0,0,0,"N");
    longitude = new Coordinate(0,0,0,"E");
}

GPSCoord::~GPSCoord(){
    delete latitude;
    delete longitude;
    qDebug() << "The Destructor is executed." ;
}

GPSCoord::GPSCoord(const GPSCoord& g){

    latitude  = new Coordinate(*g.latitude);
    longitude = new Coordinate(*g.longitude);
    qDebug() << "The copy Constructor is executed." ;
}

GPSCoord & GPSCoord::operator=(const GPSCoord& g){
    
    if( &g == this ){
        qDebug() << "The overloaded assignment operator is executed." ;
        return *this;
    }
    
}

void GPSCoord::setCoordinate(int deg, int min, int sec, QChar direc){

    if(direc.toLower() == 'n' || direc.toLower() == 's' ){
        latitude = new Coordinate(deg, min, sec, direc);
    } else if(direc.toLower() == 'e' || direc.toLower() == 'w' ){
        longitude = new Coordinate(deg, min, sec, direc);
    }
}

QString GPSCoord::toString(bool decimal){
    return decimal ?  QString(" %1 %2 ").arg(latitude->toDecimal()).arg(longitude->toDecimal()) 
                                            : latitude->toString() + " " + longitude->toString();
}