#include <QString>
#include <QStringList>

#include "../headers/Reference.h"

Reference::Reference(QString ti, QStringList as, int ye, QString id){
    title = ti;
    authors = as;
    year = ye;
    refID = id;
    refType = "Generic" ;
}

QString Reference::getTitle(){
    return title;
}

QStringList Reference::getAuthors(){
    return authors;
}

int Reference::getYear(){
    return year;
}

QString Reference:: getRefID(){
    return refID;
}

QString Reference::getType(){
    return refType;
}

QString Reference::authInitials(QString nm){

    nm.remove(nm.right(nm.lastIndexOf(0x20)));

    QString initial = nm.left(1);
    for(int i = 0 ; i < nm.length() ; i += nm.indexOf(0x20) + 1){
        initial += nm[nm.indexOf(0x20, i) + 1];
    }
    return initial ;
}

QString Reference::formattedAut(QStringList au){
    QString authList;
    foreach(QString aut, au){
        authList += aut.right(aut.lastIndexOf(0x20)) +  ", " + authInitials(aut) + ", ";
    }

    return authList.left(authList.lastIndexOf(0x44) + 1);
}

QString Reference::toString(){

    return QString(
        "Authors: %1 \n"
        "Year: %2 \n"
        "Title: %3 \n"
        "Type: %4 \n"
        "Ref ID: %5 \n"
    ).arg(formattedAut(authors)).arg(year).arg(title).arg(refType).arg(refID);

}

QString Reference::toAPAStyle(){
      return QString("%1 (%2), %3, %4")
        .arg(formattedAut(authors)).arg(year).arg(title).arg(refType);
}
