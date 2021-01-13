import connexion
import six
import json
import logging

from flask import current_app, jsonify
from openapi_server.models import Todo
from openapi_server.models.body import Body  # noqa: E501
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response400 import InlineResponse400  # noqa: E501
from openapi_server.models.inline_response4001 import InlineResponse4001  # noqa: E501
from openapi_server.models.inline_response404 import InlineResponse404  # noqa: E501
from openapi_server.models.todo_request import TodoRequest  # noqa: E501
from openapi_server.db import db
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

    new_todo = Todo(False, todo_request.title, todo_request.description, user_uuid)

    db.session.add(new_todo)
    db.session.commit()

    return None, 200



def todo_user_uuid_todo_id_delete(user_uuid, todo_id):
    try:
        results = db.session.query(Todo).filter(Todo.kid == todo_id).filter(Todo.kuser_uuid == user_uuid).all()

        if len(results) == 0:
            return InlineResponse404('todo_not_found'), 404

        db.session.delete(results[0])
        db.session.commit()
    except:
        logging.error("[todo_user_uuid_todo_id_delete] Delete " + todo_id + " Failed.")
        return 500
    return None, 200


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

    try:
        results = db.session.query(Todo).filter(Todo.kid == todo_id).filter(Todo.kuser_uuid == user_uuid).first()

        if results is None:
            return InlineResponse404('todo_not_found'), 404

        results.kis_done = body.is_done
        results.ktitle = body.title
        results.kdescription = body.description

        db.session.commit()
    except:
        logging.error("[todo_user_uuid_todo_id_delete] Delete " + todo_id + " Failed.")
        return 500

    return {}, 200


def todos_user_uuid_get(user_uuid):  # noqa: E501
    """Récupère la liste des TODOs enregistré pour l&#39;utilisateur désigné.

     # noqa: E501

    :param user_uuid: UUID de l&#39;utilisateur
    :type user_uuid: str

    :rtype: InlineResponse200
    """
    try:
        todos = db.session.query(Todo).filter(Todo.kuser_uuid == user_uuid).all()

        if todos is None:
            return InlineResponse404('user_not_found'), 404
    except:
        logging.error("[todo_user_uuid_todo_id_delete] Get todos for user " + user_uuid + " failed.")
        return 500

    results = []
    for res in todos:
        results.append(res.to_dict())

    return {"todos": results}, 200
