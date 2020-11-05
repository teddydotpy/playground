#include <QTextEdit>
#include <QHBoxLayout>
#include <QSpinBox>
#include <QInputDialog>
#include <QLabel>
#include <QDebug>

#include "../headers/Shareprofitview.h"
#include "../headers/Shareprofitmodel.h"

ShareProfitView::ShareProfitView(QDialog* parent)
    :  QDialog(parent){

    this->setWindowTitle("Profit App");
    this->setMinimumSize(600,350);
    add_button = new QPushButton("Add Investor");
    p_button = new QPushButton("Display Profits");
    Profiamnt = new QSpinBox();
    InvAmounts = new QTextEdit();
    InvAmounts->setReadOnly(true);
    Profiamnt->setRange(0,1000000000);
    Profiamnt->setSingleStep(50000);

    InvAmntsgrid = new QHBoxLayout();
    InvAmntsgrid->addWidget(InvAmounts);

    QHBoxLayout *button_h = new QHBoxLayout();
    button_h->addWidget(new QLabel("Set Profit: "));
    button_h->addWidget(Profiamnt);
    button_h->addSpacing(100);
    button_h->addStretch(0);
    button_h->addWidget(add_button);
    button_h->addWidget(p_button);

    mainLayout = new QVBoxLayout(this);

    mainLayout->addWidget(new QLabel("\x09No\x09Investment Amount \x09 Percentage \x09 Profit Amounts"));
    mainLayout->addLayout(InvAmntsgrid);
    mainLayout->addLayout(button_h);

    m_Model = new ShareprofitModel;

   connect(add_button, SIGNAL(clicked()), this, SLOT(buttHandle()));
   connect(p_button, SIGNAL(clicked()), this, SLOT(update()));

}

ShareProfitView::~ShareProfitView(){
    delete InvAmntsgrid;
    delete mainLayout;
    delete InvAmounts;
    delete add_button;
    delete p_button;
    delete ProfitCol;
}

void ShareProfitView::update(){
    m_Model->setProfit(Profiamnt->value());
    InvAmounts->clear();
    for(int i = 0; i<m_Model->count(); i++){
        InvAmounts->append(m_Model->Texwithprof().at(i));
    }

}

void ShareProfitView::buttHandle(){
    double inv = QInputDialog::getDouble(this, "Add Investor Amount", 
    "Enter Amount", 0, 0, 1000000000, 1 , NULL);

    m_Model->addAmount(inv);
    InvAmounts->append(m_Model->TexEditout());
}
