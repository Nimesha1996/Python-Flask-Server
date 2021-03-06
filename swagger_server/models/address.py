# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Address(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, street: str=None, city: str=None, state: str=None, zip: str=None):  # noqa: E501
        """Address - a model defined in Swagger

        :param street: The street of this Address.  # noqa: E501
        :type street: str
        :param city: The city of this Address.  # noqa: E501
        :type city: str
        :param state: The state of this Address.  # noqa: E501
        :type state: str
        :param zip: The zip of this Address.  # noqa: E501
        :type zip: str
        """
        self.swagger_types = {
            'street': str,
            'city': str,
            'state': str,
            'zip': str
        }

        self.attribute_map = {
            'street': 'street',
            'city': 'city',
            'state': 'state',
            'zip': 'zip'
        }
        self._street = street
        self._city = city
        self._state = state
        self._zip = zip

    @classmethod
    def from_dict(cls, dikt) -> 'Address':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Address of this Address.  # noqa: E501
        :rtype: Address
        """
        return util.deserialize_model(dikt, cls)

    @property
    def street(self) -> str:
        """Gets the street of this Address.


        :return: The street of this Address.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street: str):
        """Sets the street of this Address.


        :param street: The street of this Address.
        :type street: str
        """

        self._street = street

    @property
    def city(self) -> str:
        """Gets the city of this Address.


        :return: The city of this Address.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this Address.


        :param city: The city of this Address.
        :type city: str
        """

        self._city = city

    @property
    def state(self) -> str:
        """Gets the state of this Address.


        :return: The state of this Address.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this Address.


        :param state: The state of this Address.
        :type state: str
        """

        self._state = state

    @property
    def zip(self) -> str:
        """Gets the zip of this Address.


        :return: The zip of this Address.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip: str):
        """Sets the zip of this Address.


        :param zip: The zip of this Address.
        :type zip: str
        """

        self._zip = zip
