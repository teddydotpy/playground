#include <QString>

#include "../headers/ConferencePaper.h"

ConferencePaper::ConferencePaper(QString ti, QStringList as, int ye, QString id, QString cn, int mo)
    : Reference(ti, as, ye, id) {

    confName = cn;
    month = mo;
    refType = "Conference" ;
}

QString ConferencePaper::getConfName(){
    return confName;
}

int ConferencePaper::getMonth(){
    return month;
}


QString monthid(int n){
    switch (n)
    {
    case 1:
        return "January";
        break;
    case 2:
        return "February";
        break;
    case 3:
        return "March";
        break;
    case 4:
        return "April";
        break;
    case 5:
        return "May";
        break;
    case 6:
        return "June";
        break;
    case 7:
        return "July";
        break;
    case 8:
        return "August";
        break;
    case 9:
        return "September";
        break;
    case 10:
        return "October";
        break;
    case 11:
        return "November";
        break;
    case 12:
        return "December";
        break;
    default:
        return "Non-Existent month.";
        break;
    }
}


QString ConferencePaper::toString(){

    return QString(
        "Authors: %1 \n"
        "Year: %2 \n"
        "Title: %3 \n"
        "Type: %4 \n"
        "Ref ID: %5 \n"
        "Conference Name: %6 \n"
    ).arg(formattedAut(getAuthors())).arg(getYear()).arg(getTitle()).arg(refType).arg(getRefID()).arg(confName);

}

QString ConferencePaper::toAPAStyle(){
      return QString("%7 (%9), %10, %11, %12, %6 %2")
        .arg(formattedAut(getAuthors())).arg(getYear()).arg(getTitle()).arg(refType).arg(confName).arg(monthid(month));
}

