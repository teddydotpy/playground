 #include <QTextStream>
#include <iostream>
#include <QDebug>
#include <QString>
#include "../headers/GPSCoord.h"

void user_Ask_lang(int & user_Deg_lang, int & user_Min_lang, int & user_Sec_lang, QString & user_dir_lang){

    QTextStream cin(stdin);
    std::cout << "Enter latitude: " ;
    user_dir_lang = cin.readLine();

        QString spce_char = " ", rem_dir, rem_min, rem_sec;

        rem_dir = user_dir_lang.left(user_dir_lang.lastIndexOf(spce_char));
        rem_sec = rem_dir.left(rem_dir.lastIndexOf(spce_char));
        rem_min = rem_sec.left(rem_sec.lastIndexOf(spce_char));
        user_Deg_lang = rem_min.toInt();
        user_Min_lang = rem_sec.mid(rem_sec.indexOf(spce_char)+1,3).toInt();
        user_Sec_lang = rem_dir.mid(rem_dir.lastIndexOf(spce_char)+1,3).toInt();
        // qDebug() << rem_dir << " " << rem_sec << " " << rem_min ;        #this too for console logging
        // qDebug() << user_Deg << " " << user_Min << " " << user_Sec ;

}

void user_Ask_long(int & user_Deg_long, int & user_Min_long, int & user_Sec_long, QString & user_dir_long){

    QTextStream cin(stdin);
    std::cout << "Enter longitude: " ;
    user_dir_long = cin.readLine();

        QString spce_char = " ", rem_dir, rem_min, rem_sec;

        rem_dir = user_dir_long.left(user_dir_long.lastIndexOf(spce_char));
        rem_sec = rem_dir.left(rem_dir.lastIndexOf(spce_char));
        rem_min = rem_sec.left(rem_sec.lastIndexOf(spce_char));
        user_Deg_long = rem_min.toInt();
        user_Min_long = rem_sec.mid(rem_sec.indexOf(spce_char)+1,3).toInt();
        user_Sec_long = rem_dir.mid(rem_dir.lastIndexOf(spce_char)+1,3).toInt();
        // qDebug() << rem_dir << " " << rem_sec << " " << rem_min ;        #this too for console logging
        // qDebug() << user_Deg << " " << user_Min << " " << user_Sec ;

}

QChar easy_dir(QString User_input){
    return User_input[User_input.length() - 1].toUpper();
}


int main(){
    int user_Deg_lang, user_Min_lang, user_Sec_lang;
    int user_Deg_long, user_Min_long, user_Sec_long;
    QString user_dir_lang, user_dir_long;

    user_Ask_lang(user_Deg_lang, user_Min_lang, user_Sec_lang,user_dir_lang);
    user_Ask_long(user_Deg_long, user_Min_long, user_Sec_long,user_dir_long);

    qDebug() << user_Deg_long << " " << user_Min_long << " " << user_Sec_long << " " << user_dir_long ;

       if( (user_Deg_lang < 60 && user_Min_lang < 180 && user_Sec_lang < 180) &&
            (user_Deg_long < 60 && user_Min_long < 180 && user_Sec_long < 180) &&
        (easy_dir(user_dir_lang) == 'N' || easy_dir(user_dir_long) == 'W' || 
        easy_dir(user_dir_long) == 'E' || easy_dir(user_dir_lang) == 'S') ){
                
            GPSCoord test;
            GPSCoord test2(test);
            GPSCoord test3 ;
            test2 = test3; 
            
            test.setCoordinate(user_Deg_lang, user_Min_lang, user_Sec_lang, easy_dir(user_dir_lang));
            test.setCoordinate(user_Deg_long, user_Min_long, user_Sec_long, easy_dir(user_dir_long));
            qDebug() << test.toString(true);
            qDebug() << test.toString(false);

     }else{
            qDebug() << "You sincerely suck." ;
            exit(1);
        }
    return EXIT_SUCCESS;
}