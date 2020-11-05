#include <QStringList>
#include <QInputDialog>
#include <QString>
#include <QDebug>

#include "../headers/Shareprofitmodel.h"

ShareprofitModel::ShareprofitModel(){

    profit = 0;
    InvNo = 0;
}

ShareprofitModel::~ShareprofitModel(){

}

void ShareprofitModel::addAmount(double inv){
    this->append(inv);

    qDebug() << inv << endl ;

    InvNo++;
}

double ShareprofitModel::setProfit(double m_profit){
    profit = m_profit;
    qDebug() << profit << endl ;
}

double ShareprofitModel::totalInvestment(){
    double totInv = 0;
    for(int i = 0; i < this->count();i++){
        totInv += this->at(i);
    }
    return totInv;
}

double ShareprofitModel::percentage(int inv){
    return (this->at(inv - 1)/totalInvestment())*100;
}

double ShareprofitModel::share(int inv){
    return profit*(percentage(inv)/100);
}

QString ShareprofitModel::TexEditout(){
    return QString("\x09%1 \x09%2 \x09%3")
    .arg(InvNo).arg(this->at(InvNo)).arg(percentage(this->at(InvNo)));
}

QString ShareprofitModel::Texwithprof(){
    return QString("\x09%1 \x09%2 \x09%3 \x09%4").arg(InvNo).arg(this->at(InvNo))
        .arg(percentage(this->at(InvNo))).arg(share(this->at(InvNo)));
}