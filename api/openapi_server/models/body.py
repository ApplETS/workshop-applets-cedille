# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.body_all_of import BodyAllOf
from openapi_server.models.todo_request import TodoRequest
from openapi_server import util

from openapi_server.models.body_all_of import BodyAllOf  # noqa: E501
from openapi_server.models.todo_request import TodoRequest  # noqa: E501

class Body(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, title=None, description=None, is_done=None):  # noqa: E501
        """Body - a model defined in OpenAPI

        :param title: The title of this Body.  # noqa: E501
        :type title: str
        :param description: The description of this Body.  # noqa: E501
        :type description: str
        :param is_done: The is_done of this Body.  # noqa: E501
        :type is_done: bool
        """
        self.openapi_types = {
            'title': str,
            'description': str,
            'is_done': bool
        }

        self.attribute_map = {
            'title': 'title',
            'description': 'description',
            'is_done': 'is_done'
        }

        self._title = title
        self._description = description
        self._is_done = is_done

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self):
        """Gets the title of this Body.

        Titre de la TODO.  # noqa: E501

        :return: The title of this Body.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Body.

        Titre de la TODO.  # noqa: E501

        :param title: The title of this Body.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) > 128:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `128`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Body.

        Description de la TODO.  # noqa: E501

        :return: The description of this Body.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body.

        Description de la TODO.  # noqa: E501

        :param description: The description of this Body.
        :type description: str
        """
        if description is not None and len(description) > 280:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `280`")  # noqa: E501

        self._description = description

    @property
    def is_done(self):
        """Gets the is_done of this Body.

        Si la TODO est marquée finie.  # noqa: E501

        :return: The is_done of this Body.
        :rtype: bool
        """
        return self._is_done

    @is_done.setter
    def is_done(self, is_done):
        """Sets the is_done of this Body.

        Si la TODO est marquée finie.  # noqa: E501

        :param is_done: The is_done of this Body.
        :type is_done: bool
        """
        if is_done is None:
            raise ValueError("Invalid value for `is_done`, must not be `None`")  # noqa: E501

        self._is_done = is_done