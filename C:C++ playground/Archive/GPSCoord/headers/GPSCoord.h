#ifndef GPSCOORD_H 
#define GPSCOORD_H
#include <QString>
#include "Coordinate.h"

class GPSCoord : public Coordinate{
    public:
        GPSCoord();
        ~GPSCoord();
        GPSCoord(const GPSCoord& g);
        GPSCoord & operator=(const GPSCoord& g);
        void setCoordinate(int d, int m, int s, QChar di);
        QString toString(bool decimal);

    private:
        Coordinate *latitude;
        Coordinate *longitude;
};
#endif