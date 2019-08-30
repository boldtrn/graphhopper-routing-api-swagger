//
// Address.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


public struct Address: Codable {


    /** Specifies the id of the location. */
    public var locationId: String

    /** Name of location. */
    public var name: String?

    /** Longitude of location. */
    public var lon: Double

    /** Latitude of location. */
    public var lat: Double

    /** Optional parameter. Specifies a hint for each address to better snap the coordinates (lon,lat) to road network. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up. */
    public var streetHint: String?
    public init(locationId: String, name: String?, lon: Double, lat: Double, streetHint: String?) { 
        self.locationId = locationId
        self.name = name
        self.lon = lon
        self.lat = lat
        self.streetHint = streetHint
    }
    public enum CodingKeys: String, CodingKey { 
        case locationId = "location_id"
        case name
        case lon
        case lat
        case streetHint = "street_hint"
    }

}