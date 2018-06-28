# coding: utf-8

"""
    GraphHopper Directions API

    You use the GraphHopper Directions API to add route planning, navigation and route optimization to your software. E.g. the Routing API has turn instructions and elevation data and the Route Optimization API solves your logistic problems and supports various constraints like time window and capacity restrictions. Also it is possible to get all distances between all locations with our fast Matrix API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Algorithm(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'problem_type': 'str',
        'objective': 'str'
    }

    attribute_map = {
        'problem_type': 'problem_type',
        'objective': 'objective'
    }

    def __init__(self, problem_type=None, objective=None):  # noqa: E501
        """Algorithm - a model defined in OpenAPI"""  # noqa: E501

        self._problem_type = None
        self._objective = None
        self.discriminator = None

        if problem_type is not None:
            self.problem_type = problem_type
        if objective is not None:
            self.objective = objective

    @property
    def problem_type(self):
        """Gets the problem_type of this Algorithm.  # noqa: E501


        :return: The problem_type of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """Sets the problem_type of this Algorithm.


        :param problem_type: The problem_type of this Algorithm.  # noqa: E501
        :type: str
        """
        allowed_values = ["min", "min-max"]  # noqa: E501
        if problem_type not in allowed_values:
            raise ValueError(
                "Invalid value for `problem_type` ({0}), must be one of {1}"  # noqa: E501
                .format(problem_type, allowed_values)
            )

        self._problem_type = problem_type

    @property
    def objective(self):
        """Gets the objective of this Algorithm.  # noqa: E501


        :return: The objective of this Algorithm.  # noqa: E501
        :rtype: str
        """
        return self._objective

    @objective.setter
    def objective(self, objective):
        """Sets the objective of this Algorithm.


        :param objective: The objective of this Algorithm.  # noqa: E501
        :type: str
        """
        allowed_values = ["transport_time", "completion_time"]  # noqa: E501
        if objective not in allowed_values:
            raise ValueError(
                "Invalid value for `objective` ({0}), must be one of {1}"  # noqa: E501
                .format(objective, allowed_values)
            )

        self._objective = objective

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Algorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other