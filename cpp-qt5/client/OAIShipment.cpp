/**
 * GraphHopper Directions API
 * You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


#include "OAIShipment.h"

#include "OAIHelpers.h"

#include <QJsonDocument>
#include <QJsonArray>
#include <QObject>
#include <QDebug>

namespace OpenAPI {

OAIShipment::OAIShipment(QString json) {
    init();
    this->fromJson(json);
}

OAIShipment::OAIShipment() {
    init();
}

OAIShipment::~OAIShipment() {
    this->cleanup();
}

void
OAIShipment::init() {
    id = new QString("");
    m_id_isSet = false;
    name = new QString("");
    m_name_isSet = false;
    priority = 0;
    m_priority_isSet = false;
    pickup = new OAIStop();
    m_pickup_isSet = false;
    delivery = new OAIStop();
    m_delivery_isSet = false;
    size = new QList<qint32>();
    m_size_isSet = false;
    required_skills = new QList<QString*>();
    m_required_skills_isSet = false;
    allowed_vehicles = new QList<QString*>();
    m_allowed_vehicles_isSet = false;
    disallowed_vehicles = new QList<QString*>();
    m_disallowed_vehicles_isSet = false;
    max_time_in_vehicle = 0L;
    m_max_time_in_vehicle_isSet = false;
}

void
OAIShipment::cleanup() {
    if(id != nullptr) { 
        delete id;
    }
    if(name != nullptr) { 
        delete name;
    }

    if(pickup != nullptr) { 
        delete pickup;
    }
    if(delivery != nullptr) { 
        delete delivery;
    }

    if(size != nullptr) { 
        delete size;
    }
    if(required_skills != nullptr) { 
        auto arr = required_skills;
        for(auto o: *arr) { 
            delete o;
        }
        delete required_skills;
    }
    if(allowed_vehicles != nullptr) { 
        auto arr = allowed_vehicles;
        for(auto o: *arr) { 
            delete o;
        }
        delete allowed_vehicles;
    }
    if(disallowed_vehicles != nullptr) { 
        auto arr = disallowed_vehicles;
        for(auto o: *arr) { 
            delete o;
        }
        delete disallowed_vehicles;
    }

}

OAIShipment*
OAIShipment::fromJson(QString json) {
    QByteArray array (json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
    return this;
}

void
OAIShipment::fromJsonObject(QJsonObject pJson) {
    ::OpenAPI::setValue(&id, pJson["id"], "QString", "QString");
    
    ::OpenAPI::setValue(&name, pJson["name"], "QString", "QString");
    
    ::OpenAPI::setValue(&priority, pJson["priority"], "qint32", "");
    
    ::OpenAPI::setValue(&pickup, pJson["pickup"], "OAIStop", "OAIStop");
    
    ::OpenAPI::setValue(&delivery, pJson["delivery"], "OAIStop", "OAIStop");
    
    
    ::OpenAPI::setValue(&size, pJson["size"], "QList", "qint32");
    
    ::OpenAPI::setValue(&required_skills, pJson["required_skills"], "QList", "QString");
    
    ::OpenAPI::setValue(&allowed_vehicles, pJson["allowed_vehicles"], "QList", "QString");
    
    ::OpenAPI::setValue(&disallowed_vehicles, pJson["disallowed_vehicles"], "QList", "QString");
    ::OpenAPI::setValue(&max_time_in_vehicle, pJson["max_time_in_vehicle"], "qint64", "");
    
}

QString
OAIShipment::asJson ()
{
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject
OAIShipment::asJsonObject() {
    QJsonObject obj;
    if(id != nullptr && *id != QString("")){
        toJsonValue(QString("id"), id, obj, QString("QString"));
    }
    if(name != nullptr && *name != QString("")){
        toJsonValue(QString("name"), name, obj, QString("QString"));
    }
    if(m_priority_isSet){
        obj.insert("priority", QJsonValue(priority));
    }
    if((pickup != nullptr) && (pickup->isSet())){
        toJsonValue(QString("pickup"), pickup, obj, QString("OAIStop"));
    }
    if((delivery != nullptr) && (delivery->isSet())){
        toJsonValue(QString("delivery"), delivery, obj, QString("OAIStop"));
    }
    if(size->size() > 0){
        toJsonArray((QList<void*>*)size, obj, "size", "");
    }
    if(required_skills->size() > 0){
        toJsonArray((QList<void*>*)required_skills, obj, "required_skills", "QString");
    }
    if(allowed_vehicles->size() > 0){
        toJsonArray((QList<void*>*)allowed_vehicles, obj, "allowed_vehicles", "QString");
    }
    if(disallowed_vehicles->size() > 0){
        toJsonArray((QList<void*>*)disallowed_vehicles, obj, "disallowed_vehicles", "QString");
    }
    if(m_max_time_in_vehicle_isSet){
        obj.insert("max_time_in_vehicle", QJsonValue(max_time_in_vehicle));
    }

    return obj;
}

QString*
OAIShipment::getId() {
    return id;
}
void
OAIShipment::setId(QString* id) {
    this->id = id;
    this->m_id_isSet = true;
}

QString*
OAIShipment::getName() {
    return name;
}
void
OAIShipment::setName(QString* name) {
    this->name = name;
    this->m_name_isSet = true;
}

qint32
OAIShipment::getPriority() {
    return priority;
}
void
OAIShipment::setPriority(qint32 priority) {
    this->priority = priority;
    this->m_priority_isSet = true;
}

OAIStop*
OAIShipment::getPickup() {
    return pickup;
}
void
OAIShipment::setPickup(OAIStop* pickup) {
    this->pickup = pickup;
    this->m_pickup_isSet = true;
}

OAIStop*
OAIShipment::getDelivery() {
    return delivery;
}
void
OAIShipment::setDelivery(OAIStop* delivery) {
    this->delivery = delivery;
    this->m_delivery_isSet = true;
}

QList<qint32>*
OAIShipment::getSize() {
    return size;
}
void
OAIShipment::setSize(QList<qint32>* size) {
    this->size = size;
    this->m_size_isSet = true;
}

QList<QString*>*
OAIShipment::getRequiredSkills() {
    return required_skills;
}
void
OAIShipment::setRequiredSkills(QList<QString*>* required_skills) {
    this->required_skills = required_skills;
    this->m_required_skills_isSet = true;
}

QList<QString*>*
OAIShipment::getAllowedVehicles() {
    return allowed_vehicles;
}
void
OAIShipment::setAllowedVehicles(QList<QString*>* allowed_vehicles) {
    this->allowed_vehicles = allowed_vehicles;
    this->m_allowed_vehicles_isSet = true;
}

QList<QString*>*
OAIShipment::getDisallowedVehicles() {
    return disallowed_vehicles;
}
void
OAIShipment::setDisallowedVehicles(QList<QString*>* disallowed_vehicles) {
    this->disallowed_vehicles = disallowed_vehicles;
    this->m_disallowed_vehicles_isSet = true;
}

qint64
OAIShipment::getMaxTimeInVehicle() {
    return max_time_in_vehicle;
}
void
OAIShipment::setMaxTimeInVehicle(qint64 max_time_in_vehicle) {
    this->max_time_in_vehicle = max_time_in_vehicle;
    this->m_max_time_in_vehicle_isSet = true;
}


bool
OAIShipment::isSet(){
    bool isObjectUpdated = false;
    do{
        if(id != nullptr && *id != QString("")){ isObjectUpdated = true; break;}
        if(name != nullptr && *name != QString("")){ isObjectUpdated = true; break;}
        if(m_priority_isSet){ isObjectUpdated = true; break;}
        if(pickup != nullptr && pickup->isSet()){ isObjectUpdated = true; break;}
        if(delivery != nullptr && delivery->isSet()){ isObjectUpdated = true; break;}
        if(m_size_isSet){ isObjectUpdated = true; break;}
        if(size->size() > 0){ isObjectUpdated = true; break;}
        if(required_skills->size() > 0){ isObjectUpdated = true; break;}
        if(allowed_vehicles->size() > 0){ isObjectUpdated = true; break;}
        if(disallowed_vehicles->size() > 0){ isObjectUpdated = true; break;}
        if(m_max_time_in_vehicle_isSet){ isObjectUpdated = true; break;}
    }while(false);
    return isObjectUpdated;
}
}
