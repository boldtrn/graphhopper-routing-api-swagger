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
 * SWGGeocodingPoint.h
 * 
 * 
 */

#ifndef SWGGeocodingPoint_H_
#define SWGGeocodingPoint_H_

#include <QJsonObject>



#include "SWGObject.h"

namespace Swagger {

class SWGGeocodingPoint: public SWGObject {
public:
    SWGGeocodingPoint();
    SWGGeocodingPoint(QString* json);
    virtual ~SWGGeocodingPoint();
    void init();
    void cleanup();

    QString asJson ();
    QJsonObject* asJsonObject();
    void fromJsonObject(QJsonObject &json);
    SWGGeocodingPoint* fromJson(QString &jsonString);

    double getLat();
    void setLat(double lat);

    double getLng();
    void setLng(double lng);


    virtual bool isSet() override;

private:
    double lat;
    bool m_lat_isSet;
    
    double lng;
    bool m_lng_isSet;
    
};

}

#endif /* SWGGeocodingPoint_H_ */