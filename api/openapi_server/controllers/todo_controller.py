import connexion
import six

from openapi_server.models.body import Body  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from openapi_server.models.inline_response404 import InlineResponse404  # noqa: E501
from openapi_server.models.todo_request import TodoRequest  # noqa: E501
from openapi_server import util


def todo_user_uuid_post(user_uuid, todo_request=None):  # noqa: E501
    """Ajoute une TODO dans la liste de TODO de l&#39;utilisateur désigné.

    La TODO est créé puis ajouté dans le système, si l&#39;utilisateur n&#39;existe pas dans le système, il est créé. # noqa: E501

    :param user_uuid: UUID de l&#39;utilisateur
    :type user_uuid: str
    :param todo_request: 
    :type todo_request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        todo_request = TodoRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def todo_user_uuid_todo_id_delete(user_uuid, todo_id):  # noqa: E501
    """Supprime la TODO indiqué pour l&#39;utilisateur désigné

     # noqa: E501

    :param user_uuid: UUID de l&#39;utilisateur
    :type user_uuid: str
    :param todo_id: ID de la TODO
    :type todo_id: int

    :rtype: None
    """
    return 'do some magic!'


def todo_user_uuid_todo_id_put(user_uuid, todo_id, body=None):  # noqa: E501
    """Met à jour une TODO dans la liste de TODO de l&#39;utilisateur désigné.

    La TODO est mise-à-jour dans le système. # noqa: E501

    :param user_uuid: UUID de l&#39;utilisateur
    :type user_uuid: str
    :param todo_id: ID de la TODO
    :type todo_id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def todos_user_uuid_get(user_uuid):  # noqa: E501
    """Récupère la liste des TODOs enregistré pour l&#39;utilisateur désigné.

     # noqa: E501

    :param user_uuid: UUID de l&#39;utilisateur
    :type user_uuid: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
