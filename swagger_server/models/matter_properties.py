# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MatterProperties(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, state: str=None, temperatur: float=None):  # noqa: E501
        """MatterProperties - a model defined in Swagger

        :param id: The id of this MatterProperties.  # noqa: E501
        :type id: int
        :param state: The state of this MatterProperties.  # noqa: E501
        :type state: str
        :param temperatur: The temperatur of this MatterProperties.  # noqa: E501
        :type temperatur: float
        """
        self.swagger_types = {
            'id': int,
            'state': str,
            'temperatur': float
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'temperatur': 'temperatur'
        }
        self._id = id
        self._state = state
        self._temperatur = temperatur

    @classmethod
    def from_dict(cls, dikt) -> 'MatterProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MatterProperties of this MatterProperties.  # noqa: E501
        :rtype: MatterProperties
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this MatterProperties.


        :return: The id of this MatterProperties.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this MatterProperties.


        :param id: The id of this MatterProperties.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def state(self) -> str:
        """Gets the state of this MatterProperties.


        :return: The state of this MatterProperties.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this MatterProperties.


        :param state: The state of this MatterProperties.
        :type state: str
        """
        allowed_values = ["solid", "liquid", "gas", "plasma"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def temperatur(self) -> float:
        """Gets the temperatur of this MatterProperties.


        :return: The temperatur of this MatterProperties.
        :rtype: float
        """
        return self._temperatur

    @temperatur.setter
    def temperatur(self, temperatur: float):
        """Sets the temperatur of this MatterProperties.


        :param temperatur: The temperatur of this MatterProperties.
        :type temperatur: float
        """

        self._temperatur = temperatur
