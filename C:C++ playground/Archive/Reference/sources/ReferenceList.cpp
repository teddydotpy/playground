#include <QString>
#include <QStringList>

#include "../headers/ReferenceList.h"
#include "../headers/ConferencePaper.h"
#include "../headers/JournalArticle.h"

ReferenceList::~ReferenceList(){
    clear();
}

bool ReferenceList::addReference(Reference* r){

    if(this->isEmpty()){
        this->push_front(r);
        return true;
    } else {
    
        for(int i = 0; i < this->count() ; i++){

            if(this->value(i)->getRefID() == r->getRefID()){
                return false;
            }
        }
            this->append(r);
            return true;
    }
}

QString ReferenceList::generateReferences(QStringList ids, bool full){

    if(ids.isEmpty()){
        return "";
    } else {

        for(int i = 0; i < this->count() ;i++){
            if(this->value(i)->getRefID() == ids.value(i)){
                if(full){
                    return this->value(i)->toString();
                } else {
                    return this->value(i)->toAPAStyle();
                }
            }
        }
    }
}

QStringList ReferenceList::getiDsByAuthor(QString au){

    QStringList ids;

    if(this->isEmpty()){
        return ids;
    } else {

        for(int i = 0; i < this->count() ; i++){
            for(int j = 0; j < this->value(i)->getAuthors().count() ; j++ ){
                    if(this->value(i)->getAuthors().value(j) == au){
                        ids.append(this->value(i)->getRefID());
                }
            }
        }

        return ids;
    }
}

QStringList ReferenceList::getIDsByConference(QString cn){

    QStringList ids; 
    if(this->isEmpty()){
        return ids;
    } else {

        for(int i = 0; i < this->count() ; i++){
                    if(this->value(i)->getType() == "Conference"){

                        ConferencePaper *a = (ConferencePaper*)value(i);

                        if(a->getConfName() == cn){
                            ids.append(this->value(i)->getRefID());
                        }
                }
            }
            return ids;
        }
}

QStringList ReferenceList::getIDsByJournal(QString jn){

    QStringList ids;
    if(this->isEmpty()){
        return ids;
    } else {

        for(int i = 0; i < this->count() ; i++){
                        JournalArticle *a = (JournalArticle*)value(i);

                        if(a->getJournaName() == jn){
                            ids.append(this->value(i)->getRefID());
                        }
            }
            return ids;
        }

}

Reference* ReferenceList::findByID(QString id){

    if(this->isEmpty()){
        return NULL;
    } else {

        for(int i = 0; i < this->count() ; i++){
            if(this->value(i)->getRefID() == id){
                return this->value(i);
            } else {
                return NULL;
            }
        }
    }
}

