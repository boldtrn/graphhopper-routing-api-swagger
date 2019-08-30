//
// Algorithm.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation

/** Use &#x60;objectives&#x60; instead. */
public struct Algorithm: Codable {

    public enum ProblemType: String, Codable { 
        case min = "min"
        case minMax = "min-max"
    }    public enum Objective: String, Codable { 
        case transportTime = "transport_time"
        case completionTime = "completion_time"
    }    public var problemType: ProblemType?
    public var objective: Objective?
    public init(problemType: ProblemType?, objective: Objective?) { 
        self.problemType = problemType
        self.objective = objective
    }
    public enum CodingKeys: String, CodingKey { 
        case problemType = "problem_type"
        case objective
    }

}