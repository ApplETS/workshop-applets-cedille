# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util
from openapi_server.db import db


class Todo(Model, db.Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """
    __tablename__ = "Todos"
    _id = db.Column(db.Integer, primary_key=True)
    _is_done = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    _title = db.Column(db.String(64), unique=False, nullable=False)
    _description = db.Column(db.String(256), unique=False, nullable=True)

    def __init__(self, id=None, is_done=None, title=None, description=None, user_uuid=None):  # noqa: E501
        """Todo - a model defined in OpenAPI

        :param id: The id of this Todo.  # noqa: E501
        :type id: int
        :param is_done: The is_done of this Todo.  # noqa: E501
        :type is_done: bool
        :param title: The title of this Todo.  # noqa: E501
        :type title: str
        :param description: The description of this Todo.  # noqa: E501
        :type description: str
        :param user_uuid: The user_uuid of this Todo # noqa: E501
        :type user_uuid: str
        """
        self.openapi_types = {
            'id': int,
            'is_done': bool,
            'title': str,
            'description': str,
            'user_uuid': str
        }

        self.attribute_map = {
            'id': 'id',
            'is_done': 'is_done',
            'title': 'title',
            'description': 'description',
            'user_uuid': 'user_uuid'
        }

        self._id = id
        self._is_done = is_done
        self._title = title
        self._description = description
        self._user_uuid = user_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'Todo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Todo of this Todo.  # noqa: E501
        :rtype: Todo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Todo.

        Identifiant unique de la TODO  # noqa: E501

        :return: The id of this Todo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Todo.

        Identifiant unique de la TODO  # noqa: E501

        :param id: The id of this Todo.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_done(self):
        """Gets the is_done of this Todo.

        Si la TODO est marquée finie.  # noqa: E501

        :return: The is_done of this Todo.
        :rtype: bool
        """
        return self._is_done

    @is_done.setter
    def is_done(self, is_done):
        """Sets the is_done of this Todo.

        Si la TODO est marquée finie.  # noqa: E501

        :param is_done: The is_done of this Todo.
        :type is_done: bool
        """
        if is_done is None:
            raise ValueError("Invalid value for `is_done`, must not be `None`")  # noqa: E501

        self._is_done = is_done

    @property
    def title(self):
        """Gets the title of this Todo.

        Titre de la TODO.  # noqa: E501

        :return: The title of this Todo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Todo.

        Titre de la TODO.  # noqa: E501

        :param title: The title of this Todo.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) > 128:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `128`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this Todo.

        Description de la TODO.  # noqa: E501

        :return: The description of this Todo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Todo.

        Description de la TODO.  # noqa: E501

        :param description: The description of this Todo.
        :type description: str
        """
        if description is not None and len(description) > 280:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `280`")  # noqa: E501

        self._description = description

    @property
    def user_uuid(self):
        """Gets the user_uuid of this Todo.

        UUID de l'utilisateur de la TODO.  # noqa: E501

        :return: The user_uuid of this Todo.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the description of this Todo.

        UUID de l'utilisateur de la TODO.  # noqa: E501

        :param user_uuid: The user_uuid of this Todo.
        :type user_uuid: str
        """
        if user_uuid is not None and len(user_uuid) > 280:
            raise ValueError("Invalid value for `user_uuid`, length must be less than or equal to `280`")  # noqa: E501

        self._user_uuid = user_uuid