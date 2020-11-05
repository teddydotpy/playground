#include <QString>

#include "../headers/JournalArticle.h"

JournalArticle::JournalArticle(QString ti, QStringList as, int ye, QString id, QString jn, int vo, int no)
    : Reference(ti, as, ye, id) {

    JournalName = jn;
    volume = vo;
    number = no;
    refType = "Journal" ;
}

QString JournalArticle::getJournaName(){
    return JournalName;
}

int JournalArticle::getVolume(){
    return volume;
}

int JournalArticle::getNumber(){
    return number;
}

QString JournalArticle::toString(){

    return QString(
        "Authors: %1" 
        "Year: %2 \n"
        "Title: %3 \n"
        "Type: %4 \n"
        "Ref ID: %5"
        "Journal Name: %6 \n"
        "Volume: %7 \n"
        "Number: %8 \n"
    ).arg(formattedAut(getAuthors())).arg(getYear()).arg(getTitle()).arg(refType).arg(getRefID()).arg(JournalName).arg(volume).arg(number);

}

QString JournalArticle::toAPAStyle(){
      return QString("%1 (%2), %3, %4, %5, Vol %6 No %7")
        .arg(formattedAut(getAuthors())).arg(getYear()).arg(getTitle()).arg(refType).arg(JournalName).arg(volume).arg(number);
}

