/**
 * GraphHopper Directions API
 * You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

/*
 * SWGMatrixRequest.h
 * 
 * 
 */

#ifndef SWGMatrixRequest_H_
#define SWGMatrixRequest_H_

#include <QJsonObject>


#include <QList>
#include <QString>

#include "SWGObject.h"

namespace Swagger {

class SWGMatrixRequest: public SWGObject {
public:
    SWGMatrixRequest();
    SWGMatrixRequest(QString* json);
    virtual ~SWGMatrixRequest();
    void init();
    void cleanup();

    QString asJson ();
    QJsonObject* asJsonObject();
    void fromJsonObject(QJsonObject &json);
    SWGMatrixRequest* fromJson(QString &jsonString);

    QList<QList<double>*>* getPoints();
    void setPoints(QList<QList<double>*>* points);

    QList<QList<double>*>* getFromPoints();
    void setFromPoints(QList<QList<double>*>* from_points);

    QList<QList<double>*>* getToPoints();
    void setToPoints(QList<QList<double>*>* to_points);

    QList<QString*>* getPointHints();
    void setPointHints(QList<QString*>* point_hints);

    QList<QString*>* getFromPointHints();
    void setFromPointHints(QList<QString*>* from_point_hints);

    QList<QString*>* getToPointHints();
    void setToPointHints(QList<QString*>* to_point_hints);

    QList<QString*>* getOutArrays();
    void setOutArrays(QList<QString*>* out_arrays);

    QString* getVehicle();
    void setVehicle(QString* vehicle);


    virtual bool isSet() override;

private:
    QList<QList<double>*>* points;
    bool m_points_isSet;
    
    QList<QList<double>*>* from_points;
    bool m_from_points_isSet;
    
    QList<QList<double>*>* to_points;
    bool m_to_points_isSet;
    
    QList<QString*>* point_hints;
    bool m_point_hints_isSet;
    
    QList<QString*>* from_point_hints;
    bool m_from_point_hints_isSet;
    
    QList<QString*>* to_point_hints;
    bool m_to_point_hints_isSet;
    
    QList<QString*>* out_arrays;
    bool m_out_arrays_isSet;
    
    QString* vehicle;
    bool m_vehicle_isSet;
    
};

}

#endif /* SWGMatrixRequest_H_ */