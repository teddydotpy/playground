#include "../headers/Coordinate.h"
#include <QString>
#include <QApplication>
#include <QInputDialog>
#include <QMessageBox>
#include <iostream>
#include <QPushButton>
// #include <QDebug> #Uncomment this to view console logging.

void user_Ask(int & user_Deg, int & user_Min, int & user_Sec, QString & User_input){
    User_input = QInputDialog::getText(0, "Coordinates",
          "Enter Coordinate serperated by space: ", QLineEdit::Normal);

        QString spce_char = " ", rem_dir, rem_min, rem_sec;

        rem_dir = User_input.left(User_input.lastIndexOf(spce_char));
        rem_sec = rem_dir.left(rem_dir.lastIndexOf(spce_char));
        rem_min = rem_sec.left(rem_sec.lastIndexOf(spce_char));
        user_Deg = rem_min.toInt();
        user_Min = rem_sec.mid(rem_sec.indexOf(spce_char)+1,3).toInt();
        user_Sec = rem_dir.mid(rem_dir.lastIndexOf(spce_char)+1,3).toInt();
        // qDebug() << rem_dir << " " << rem_sec << " " << rem_min ;        #this too for console logging
        // qDebug() << user_Deg << " " << user_Min << " " << user_Sec ;

}

QChar easy_dir(QString User_input){
    return User_input[User_input.length() - 1].toUpper();
}

void Dial_Resp(int user_Deg, int user_Min, int user_Sec, QString User_input){

    user_Ask(user_Deg, user_Min, user_Sec, User_input );

    if( user_Deg < 60 && user_Min < 180 && user_Sec < 180 && (easy_dir(User_input) == 'N' ||
            easy_dir(User_input) == 'W' || easy_dir(User_input) == 'E' || easy_dir(User_input) == 'S') ){
                
                Coordinate test(user_Deg,user_Min,user_Sec,easy_dir(User_input));

                QMessageBox QCoMsg;
                QString dec = QString("%1").arg(test.toDecimal());
                QCoMsg.setText("Normal Coordinates: " + test.toString() + '\n' +
                                "Decimal Coordinates: " + dec );

                QAbstractButton *tryButton = QCoMsg.addButton("Try Again", QMessageBox::ActionRole);
                QAbstractButton *exitButton = QCoMsg.addButton("Exit", QMessageBox::ActionRole);
                QCoMsg.exec();
                if (QCoMsg.clickedButton() == tryButton) {
                Dial_Resp(user_Deg, user_Min, user_Sec, User_input );
                }
                if (QCoMsg.clickedButton() == exitButton ) {
                    exit(1);
                }
     } else {
     
        QMessageBox badMsg;
        badMsg.setText("You didn't do the right thing \n That input was invalid, shame on you.");
        QAbstractButton *tryButton = badMsg.addButton("Try Again", QMessageBox::ActionRole);
        QAbstractButton *exitButton = badMsg.addButton("Exit", QMessageBox::ActionRole);
        badMsg.exec();
        if (badMsg.clickedButton() == tryButton) {
        Dial_Resp( user_Deg, user_Min, user_Sec, User_input);
        }
        if (badMsg.clickedButton() == exitButton ) {
        }
         exit(1);
        }
    
}

int main(int argc, char ** argv){

    QApplication app(argc,argv);
     int user_Min, user_Sec, user_Deg;
     QString User_input;

     Dial_Resp(user_Deg, user_Min, user_Sec,  User_input);
	std::cout << "this is for effect" << std::endl ;
    return app.exec();
}
