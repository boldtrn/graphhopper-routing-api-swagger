/* 
 * GraphHopper Directions API
 *
 * You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// SolutionUnassigned
    /// </summary>
    [DataContract]
    public partial class SolutionUnassigned :  IEquatable<SolutionUnassigned>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SolutionUnassigned" /> class.
        /// </summary>
        /// <param name="Services">An array of ids of unassigned services.</param>
        /// <param name="Shipments">An array of ids of unassigned shipments.</param>
        /// <param name="Breaks">An array of ids of unassigned breaks.</param>
        /// <param name="Details">An array of details, i.e. reason for unassigned services or shipments.</param>
        public SolutionUnassigned(List<string> Services = default(List<string>), List<string> Shipments = default(List<string>), List<string> Breaks = default(List<string>), List<Detail> Details = default(List<Detail>))
        {
            this.Services = Services;
            this.Shipments = Shipments;
            this.Breaks = Breaks;
            this.Details = Details;
        }
        
        /// <summary>
        /// An array of ids of unassigned services
        /// </summary>
        /// <value>An array of ids of unassigned services</value>
        [DataMember(Name="services", EmitDefaultValue=false)]
        public List<string> Services { get; set; }

        /// <summary>
        /// An array of ids of unassigned shipments
        /// </summary>
        /// <value>An array of ids of unassigned shipments</value>
        [DataMember(Name="shipments", EmitDefaultValue=false)]
        public List<string> Shipments { get; set; }

        /// <summary>
        /// An array of ids of unassigned breaks
        /// </summary>
        /// <value>An array of ids of unassigned breaks</value>
        [DataMember(Name="breaks", EmitDefaultValue=false)]
        public List<string> Breaks { get; set; }

        /// <summary>
        /// An array of details, i.e. reason for unassigned services or shipments
        /// </summary>
        /// <value>An array of details, i.e. reason for unassigned services or shipments</value>
        [DataMember(Name="details", EmitDefaultValue=false)]
        public List<Detail> Details { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class SolutionUnassigned {\n");
            sb.Append("  Services: ").Append(Services).Append("\n");
            sb.Append("  Shipments: ").Append(Shipments).Append("\n");
            sb.Append("  Breaks: ").Append(Breaks).Append("\n");
            sb.Append("  Details: ").Append(Details).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as SolutionUnassigned);
        }

        /// <summary>
        /// Returns true if SolutionUnassigned instances are equal
        /// </summary>
        /// <param name="input">Instance of SolutionUnassigned to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SolutionUnassigned input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Services == input.Services ||
                    this.Services != null &&
                    this.Services.SequenceEqual(input.Services)
                ) && 
                (
                    this.Shipments == input.Shipments ||
                    this.Shipments != null &&
                    this.Shipments.SequenceEqual(input.Shipments)
                ) && 
                (
                    this.Breaks == input.Breaks ||
                    this.Breaks != null &&
                    this.Breaks.SequenceEqual(input.Breaks)
                ) && 
                (
                    this.Details == input.Details ||
                    this.Details != null &&
                    this.Details.SequenceEqual(input.Details)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Services != null)
                    hashCode = hashCode * 59 + this.Services.GetHashCode();
                if (this.Shipments != null)
                    hashCode = hashCode * 59 + this.Shipments.GetHashCode();
                if (this.Breaks != null)
                    hashCode = hashCode * 59 + this.Breaks.GetHashCode();
                if (this.Details != null)
                    hashCode = hashCode * 59 + this.Details.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}