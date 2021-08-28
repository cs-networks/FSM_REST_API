# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Field(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, type: str=None, title: str=None, value: str=None):  # noqa: E501
        """Field - a model defined in Swagger

        :param name: The name of this Field.  # noqa: E501
        :type name: str
        :param type: The type of this Field.  # noqa: E501
        :type type: str
        :param title: The title of this Field.  # noqa: E501
        :type title: str
        :param value: The value of this Field.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'name': str,
            'type': str,
            'title': str,
            'value': str
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'title': 'title',
            'value': 'value'
        }
        self._name = name
        self._type = type
        self._title = title
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Field':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Field of this Field.  # noqa: E501
        :rtype: Field
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Field.


        :return: The name of this Field.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Field.


        :param name: The name of this Field.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self) -> str:
        """Gets the type of this Field.


        :return: The type of this Field.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Field.


        :param type: The type of this Field.
        :type type: str
        """
        allowed_values = ["hidden", "text", "search", "tel", "url", "email", "password", "datetime", "date", "month", "week", "time", "datetime-local", "number", "range", "color", "checkbox", "radio", "file"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def title(self) -> str:
        """Gets the title of this Field.


        :return: The title of this Field.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Field.


        :param title: The title of this Field.
        :type title: str
        """

        self._title = title

    @property
    def value(self) -> str:
        """Gets the value of this Field.


        :return: The value of this Field.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this Field.


        :param value: The value of this Field.
        :type value: str
        """

        self._value = value
