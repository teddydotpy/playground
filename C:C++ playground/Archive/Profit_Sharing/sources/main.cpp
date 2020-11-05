#include <QtGui>
#include <QApplication>

#include "../headers/Shareprofitview.h"
#include "../headers/Shareprofitmodel.h"

int main(int argc, char * argv[]){
    QApplication app(argc, argv);
    ShareProfitView a;

    a.exec();
    return app.exec();
}