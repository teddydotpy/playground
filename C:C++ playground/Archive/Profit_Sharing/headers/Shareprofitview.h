#ifndef SHAREPROFITVIEW_H
#define SHAREPROFITVIEW_H

#include <QDialog>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QTextEdit>
#include <QSpinBox>

#include "Shareprofitmodel.h"

class ShareProfitView : public QDialog{

    Q_OBJECT

    public:
        ShareProfitView(QDialog* parent=0);
        ~ShareProfitView();

    public slots:
        void update();
        void buttHandle();
        
    private:
        QPushButton *p_button, *add_button;
        QVBoxLayout *mainLayout;
        QHBoxLayout *InvAmntsgrid;
        QTextEdit *InvAmounts, *ProfitCol, *NoCol, *PercCol;
        QSpinBox *Profiamnt;
        ShareprofitModel *m_Model;
};

#endif