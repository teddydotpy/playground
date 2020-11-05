#ifndef REFERENCE_H
#define REFERENCE_H

#include <QString>
#include <QStringList>

class Reference{
    
    public: 
        Reference(QString ti, QStringList as, int ye, QString id);
        QString getTitle();
        QStringList getAuthors();
        int getYear();
        QString getRefID();
        virtual QString toString();
        virtual QString toAPAStyle();
        QString getType();
        QString authInitials(QString nm);
        QString formattedAut(QStringList au);

    
    private:
        QString title;
        QStringList authors;
        int year;
        QString refID;

    protected:
        QString refType;
};

#endif