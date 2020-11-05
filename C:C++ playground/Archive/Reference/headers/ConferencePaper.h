#ifndef CONFERENCEPAPER_H
#define CONFERENCEPAPER_H

#include <QString>
#include <QStringList>

#include "Reference.h"

class ConferencePaper : public Reference {

    public:
        ConferencePaper(QString ti, QStringList as, int ye, QString id, QString cn, int mo);
        QString getConfName();
        int getMonth();
        QString toString();
        QString toAPAStyle();
    
    private: 
        QString confName ;
        int month;
};

#endif