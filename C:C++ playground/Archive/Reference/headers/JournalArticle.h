#ifndef JOURNALARTICLE_H
#define JOURNALARTICLE_H

#include <QString>
#include <QStringList>

#include "Reference.h"

class JournalArticle : public Reference {

    public:
        JournalArticle(QString ti, QStringList as, int ye, QString id, QString jn, int vo, int no);
        QString getJournaName();
        int getVolume();
        int getNumber();
        QString toString();
        QString toAPAStyle();

    private:
        QString JournalName;
        int volume;
        int number;
};

#endif