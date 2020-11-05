#include <QString>
#include <QStringList>
#include <QRandomGenerator>
#include <QDebug>

#include "../headers/Reference.h"
#include "../headers/ReferenceList.h"
#include "../headers/ConferencePaper.h"
#include "../headers/JournalArticle.h"

int main(){
    QStringList default_Auth, auth_List1, auth_List2, auth_List3, JournalID, ConferenceID, AuthorID;
    ReferenceList all_the_things;
    ConferencePaper A1("The cake is a lie.", default_Auth, 1998, QVariant(QRandomGenerator::system()->generate()).toString() , "Subta", 4 );
    ConferencePaper A2("Particle Physics: An exploration.", auth_List1, 2001
                        , QVariant(QRandomGenerator::system()->generate()).toString(), "Villa", 9 );
    JournalArticle B1("The theory of relativity.", auth_List2, 2003
                            , QVariant(QRandomGenerator::system()->generate()).toString(), "The Fc", 12, 6 );    
    JournalArticle B2("Man that was a doozie.", auth_List3, 2020
                        , QVariant(QRandomGenerator::system()->generate()).toString(), "Jeopardy", 3, 16 ); 
    Reference C3("Another python book.", auth_List1, 2005, QVariant(QRandomGenerator::system()->generate()).toString());
    Reference C4("This again.", default_Auth , 2014 , QVariant(QRandomGenerator::system()->generate()).toString());


    all_the_things.addReference(&A1);
    all_the_things.addReference(&A2);
    all_the_things.addReference(&B1);
    all_the_things.addReference(&B2);
    all_the_things.addReference(&C3);
    all_the_things.addReference(&C4);

    qDebug() << all_the_things << endl ;

    AuthorID = all_the_things.getiDsByAuthor("Mark Sherwood");
    ConferenceID = all_the_things.getIDsByConference("Sherbert");
    JournalID = all_the_things.getIDsByJournal("The wood");

    qDebug() << AuthorID << endl ;
    qDebug() << ConferenceID << endl ;
    qDebug() << JournalID << endl ;

    qDebug() << all_the_things.generateReferences(AuthorID, true);
    qDebug() << all_the_things.generateReferences(ConferenceID, false);
    qDebug() << all_the_things.generateReferences(JournalID, true); 
    return EXIT_SUCCESS;
}