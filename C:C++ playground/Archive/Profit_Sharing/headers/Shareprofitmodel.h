#ifndef SHAREPROFITMODEL_H
#define SHAREPROFITMODEL_H

#include <QStringList>
#include <QString>
#include <QList>

class ShareprofitModel : public QList<double>{

    public: 
        ShareprofitModel();
        ~ShareprofitModel();
        void addAmount(double invmnt);
        double setProfit(double profit);
        double totalInvestment();
        double percentage(int invNum);
        double share(int invNum);
        QString TexEditout();
        QString Texwithprof();

    private:
        double profit;
        int InvNo;
};

#endif