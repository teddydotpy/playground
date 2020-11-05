#ifndef COORDINATE_H
#define COORDINATE_H

#include <QString>

class Coordinate{

    public:
    Coordinate();
    Coordinate(int degrees, int minutes, int seconds, QString direction);
    QString toString();
    double toDecimal();

    private:
    int degrees, minutes, seconds;
    QString direction;

}; 

#endif