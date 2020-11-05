#ifndef REFERENCELIST_H
#define REFERENCELIST_H

#include <QString>
#include <QList>
#include <QStringList>

#include "Reference.h"

class ReferenceList : public QList<Reference*>{

    public:
        ~ReferenceList();
        bool addReference(Reference* r);
        QString generateReferences(QStringList ids, bool full);
        QStringList getiDsByAuthor(QString au);
        QStringList getIDsByConference(QString cn);
        QStringList getIDsByJournal(QString jn);
    private:
        Reference* findByID(QString id);

};
#endif