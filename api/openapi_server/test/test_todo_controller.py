# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.body import Body  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from openapi_server.models.inline_response404 import InlineResponse404  # noqa: E501
from openapi_server.models.todo_request import TodoRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTodoController(BaseTestCase):
    """TodoController integration test stubs"""

    def test_todo_user_uuid_post(self):
        """Test case for todo_user_uuid_post

        Ajoute une TODO dans la liste de TODO de l'utilisateur désigné.
        """
        todo_request = {
  "description" : "Après le workshop j'ai vraiment envie d'essayer les technologies mobile et devops présentées",
  "title" : "Refaire le workshop d'App|ETS et CEDILLE"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/todo/{user_uuid}'.format(user_uuid=27610244-2819-4022-8ed3-6a0763079751),
            method='POST',
            headers=headers,
            data=json.dumps(todo_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_todo_user_uuid_todo_id_delete(self):
        """Test case for todo_user_uuid_todo_id_delete

        Supprime la TODO indiqué pour l'utilisateur désigné
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/todo/{user_uuid}/{todo_id}'.format(user_uuid=27610244-2819-4022-8ed3-6a0763079751, todo_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_todo_user_uuid_todo_id_put(self):
        """Test case for todo_user_uuid_todo_id_put

        Met à jour une TODO dans la liste de TODO de l'utilisateur désigné.
        """
        body = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/todo/{user_uuid}/{todo_id}'.format(user_uuid=27610244-2819-4022-8ed3-6a0763079751, todo_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_todos_user_uuid_get(self):
        """Test case for todos_user_uuid_get

        Récupère la liste des TODOs enregistré pour l'utilisateur désigné.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/todos/{user_uuid}'.format(user_uuid=27610244-2819-4022-8ed3-6a0763079751),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
