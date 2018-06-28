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


class ResponseInstruction(object):
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
        'text': 'str',
        'street_name': 'str',
        'distance': 'float',
        'time': 'int',
        'interval': 'list[int]',
        'sign': 'int',
        'annotation_text': 'str',
        'annotation_importance': 'int',
        'exit_number': 'int',
        'turn_angle': 'float'
    }

    attribute_map = {
        'text': 'text',
        'street_name': 'street_name',
        'distance': 'distance',
        'time': 'time',
        'interval': 'interval',
        'sign': 'sign',
        'annotation_text': 'annotation_text',
        'annotation_importance': 'annotation_importance',
        'exit_number': 'exit_number',
        'turn_angle': 'turn_angle'
    }

    def __init__(self, text=None, street_name=None, distance=None, time=None, interval=None, sign=None, annotation_text=None, annotation_importance=None, exit_number=None, turn_angle=None):  # noqa: E501
        """ResponseInstruction - a model defined in OpenAPI"""  # noqa: E501

        self._text = None
        self._street_name = None
        self._distance = None
        self._time = None
        self._interval = None
        self._sign = None
        self._annotation_text = None
        self._annotation_importance = None
        self._exit_number = None
        self._turn_angle = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if street_name is not None:
            self.street_name = street_name
        if distance is not None:
            self.distance = distance
        if time is not None:
            self.time = time
        if interval is not None:
            self.interval = interval
        if sign is not None:
            self.sign = sign
        if annotation_text is not None:
            self.annotation_text = annotation_text
        if annotation_importance is not None:
            self.annotation_importance = annotation_importance
        if exit_number is not None:
            self.exit_number = exit_number
        if turn_angle is not None:
            self.turn_angle = turn_angle

    @property
    def text(self):
        """Gets the text of this ResponseInstruction.  # noqa: E501

        A description what the user has to do in order to follow the route. The language depends on the locale parameter.  # noqa: E501

        :return: The text of this ResponseInstruction.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ResponseInstruction.

        A description what the user has to do in order to follow the route. The language depends on the locale parameter.  # noqa: E501

        :param text: The text of this ResponseInstruction.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def street_name(self):
        """Gets the street_name of this ResponseInstruction.  # noqa: E501

        The name of the street to turn onto in order to follow the route.  # noqa: E501

        :return: The street_name of this ResponseInstruction.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this ResponseInstruction.

        The name of the street to turn onto in order to follow the route.  # noqa: E501

        :param street_name: The street_name of this ResponseInstruction.  # noqa: E501
        :type: str
        """

        self._street_name = street_name

    @property
    def distance(self):
        """Gets the distance of this ResponseInstruction.  # noqa: E501

        The distance for this instruction, in meter  # noqa: E501

        :return: The distance of this ResponseInstruction.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this ResponseInstruction.

        The distance for this instruction, in meter  # noqa: E501

        :param distance: The distance of this ResponseInstruction.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def time(self):
        """Gets the time of this ResponseInstruction.  # noqa: E501

        The duration for this instruction, in ms  # noqa: E501

        :return: The time of this ResponseInstruction.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ResponseInstruction.

        The duration for this instruction, in ms  # noqa: E501

        :param time: The time of this ResponseInstruction.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def interval(self):
        """Gets the interval of this ResponseInstruction.  # noqa: E501

        An array containing the first and the last index (relative to paths[0].points) of the points for this instruction. This is useful to know for which part of the route the instructions are valid.  # noqa: E501

        :return: The interval of this ResponseInstruction.  # noqa: E501
        :rtype: list[int]
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ResponseInstruction.

        An array containing the first and the last index (relative to paths[0].points) of the points for this instruction. This is useful to know for which part of the route the instructions are valid.  # noqa: E501

        :param interval: The interval of this ResponseInstruction.  # noqa: E501
        :type: list[int]
        """

        self._interval = interval

    @property
    def sign(self):
        """Gets the sign of this ResponseInstruction.  # noqa: E501

        A number which specifies the sign to show e.g. for right turn etc <br>TURN_SHARP_LEFT = -3<br>TURN_LEFT = -2<br>TURN_SLIGHT_LEFT = -1<br>CONTINUE_ON_STREET = 0<br>TURN_SLIGHT_RIGHT = 1<br>TURN_RIGHT = 2<br>TURN_SHARP_RIGHT = 3<br>FINISH = 4<br>VIA_REACHED = 5<br>USE_ROUNDABOUT = 6  # noqa: E501

        :return: The sign of this ResponseInstruction.  # noqa: E501
        :rtype: int
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """Sets the sign of this ResponseInstruction.

        A number which specifies the sign to show e.g. for right turn etc <br>TURN_SHARP_LEFT = -3<br>TURN_LEFT = -2<br>TURN_SLIGHT_LEFT = -1<br>CONTINUE_ON_STREET = 0<br>TURN_SLIGHT_RIGHT = 1<br>TURN_RIGHT = 2<br>TURN_SHARP_RIGHT = 3<br>FINISH = 4<br>VIA_REACHED = 5<br>USE_ROUNDABOUT = 6  # noqa: E501

        :param sign: The sign of this ResponseInstruction.  # noqa: E501
        :type: int
        """

        self._sign = sign

    @property
    def annotation_text(self):
        """Gets the annotation_text of this ResponseInstruction.  # noqa: E501

        optional - A text describing the instruction in more detail, e.g. like surface of the way, warnings or involved costs.  # noqa: E501

        :return: The annotation_text of this ResponseInstruction.  # noqa: E501
        :rtype: str
        """
        return self._annotation_text

    @annotation_text.setter
    def annotation_text(self, annotation_text):
        """Sets the annotation_text of this ResponseInstruction.

        optional - A text describing the instruction in more detail, e.g. like surface of the way, warnings or involved costs.  # noqa: E501

        :param annotation_text: The annotation_text of this ResponseInstruction.  # noqa: E501
        :type: str
        """

        self._annotation_text = annotation_text

    @property
    def annotation_importance(self):
        """Gets the annotation_importance of this ResponseInstruction.  # noqa: E501

        optional - 0 stands for INFO, 1 for warning, 2 for costs, 3 for costs and warning  # noqa: E501

        :return: The annotation_importance of this ResponseInstruction.  # noqa: E501
        :rtype: int
        """
        return self._annotation_importance

    @annotation_importance.setter
    def annotation_importance(self, annotation_importance):
        """Sets the annotation_importance of this ResponseInstruction.

        optional - 0 stands for INFO, 1 for warning, 2 for costs, 3 for costs and warning  # noqa: E501

        :param annotation_importance: The annotation_importance of this ResponseInstruction.  # noqa: E501
        :type: int
        """

        self._annotation_importance = annotation_importance

    @property
    def exit_number(self):
        """Gets the exit_number of this ResponseInstruction.  # noqa: E501

        optional - Only available for USE_ROUNDABOUT instructions. The count of exits at which the route leaves the roundabout.  # noqa: E501

        :return: The exit_number of this ResponseInstruction.  # noqa: E501
        :rtype: int
        """
        return self._exit_number

    @exit_number.setter
    def exit_number(self, exit_number):
        """Sets the exit_number of this ResponseInstruction.

        optional - Only available for USE_ROUNDABOUT instructions. The count of exits at which the route leaves the roundabout.  # noqa: E501

        :param exit_number: The exit_number of this ResponseInstruction.  # noqa: E501
        :type: int
        """

        self._exit_number = exit_number

    @property
    def turn_angle(self):
        """Gets the turn_angle of this ResponseInstruction.  # noqa: E501

        optional - Only available for USE_ROUNDABOUT instructions. The radian of the route within the roundabout - 0&lt;r&lt;2*PI for clockwise and -2PI&lt;r&lt;0 for counterclockwise transit. Null if the direction of rotation is undefined.  # noqa: E501

        :return: The turn_angle of this ResponseInstruction.  # noqa: E501
        :rtype: float
        """
        return self._turn_angle

    @turn_angle.setter
    def turn_angle(self, turn_angle):
        """Sets the turn_angle of this ResponseInstruction.

        optional - Only available for USE_ROUNDABOUT instructions. The radian of the route within the roundabout - 0&lt;r&lt;2*PI for clockwise and -2PI&lt;r&lt;0 for counterclockwise transit. Null if the direction of rotation is undefined.  # noqa: E501

        :param turn_angle: The turn_angle of this ResponseInstruction.  # noqa: E501
        :type: float
        """

        self._turn_angle = turn_angle

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
        if not isinstance(other, ResponseInstruction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other