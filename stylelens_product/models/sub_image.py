# coding: utf-8

"""
    bl-db-product

    This is a API document for Product DB

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SubImage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'origin': 'str',
        'mobile': 'str',
        'main': 'int'
    }

    attribute_map = {
        'origin': 'origin',
        'mobile': 'mobile',
        'main': 'main'
    }

    def __init__(self, origin=None, mobile=None, main=None):
        """
        SubImage - a model defined in Swagger
        """

        self._origin = None
        self._mobile = None
        self._main = None

        if origin is not None:
          self.origin = origin
        if mobile is not None:
          self.mobile = mobile
        if main is not None:
          self.main = main

    @property
    def origin(self):
        """
        Gets the origin of this SubImage.

        :return: The origin of this SubImage.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this SubImage.

        :param origin: The origin of this SubImage.
        :type: str
        """

        self._origin = origin

    @property
    def mobile(self):
        """
        Gets the mobile of this SubImage.

        :return: The mobile of this SubImage.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """
        Sets the mobile of this SubImage.

        :param mobile: The mobile of this SubImage.
        :type: str
        """

        self._mobile = mobile

    @property
    def main(self):
        """
        Gets the main of this SubImage.
        1: main, 0: sub image

        :return: The main of this SubImage.
        :rtype: int
        """
        return self._main

    @main.setter
    def main(self, main):
        """
        Sets the main of this SubImage.
        1: main, 0: sub image

        :param main: The main of this SubImage.
        :type: int
        """

        self._main = main

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SubImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
