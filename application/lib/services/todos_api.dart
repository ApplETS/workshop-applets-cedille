import 'dart:convert';

import 'package:http/http.dart';
import 'package:todolist/locator.dart';
import 'package:todolist/model/todo.dart';
import 'package:todolist/services/authentication_service.dart';

class TodosApi {
  static const String baseUrl = "https://api.demo-bnc.cedille.club";

  final Client _client = Client();

  final AuthenticationService _authenticationService =
      locator<AuthenticationService>();

  final List<Todo> _todos = [];

  List<Todo> get todos => _todos;

  Future<List<Todo>> getTodos({bool refresh = false}) async {
    if (!refresh && _todos.isNotEmpty) {
      return _todos;
    }
    final res =
        await _client.get("$baseUrl/todos/${_authenticationService.user.uid}");

    print("GetTodos - ${res.statusCode}");
    if (res.statusCode == 404) {
      return [];
    } else if (res.statusCode != 200) {
      print("GetTodos - error - ${res.statusCode}");
      throw Error();
    }

    var json = jsonDecode(res.body)["todos"] as List;

    if (json != null) {
      _todos.clear();
      _todos.addAll(json.map<Todo>((todo) => Todo.fromJson(todo)).toList());
      // Retire les "done"
      _todos.removeWhere((todo) => todo.isDone);
    }

    return _todos;
  }

  Future<bool> updateTodo(Todo todo) async {
    final res = await _client.put(
        "$baseUrl/todo/${_authenticationService.user.uid}/${todo.id}",
        headers: {"Content-Type": "application/json"},
        body: jsonEncode(todo));

    if (res.statusCode == 200) {
      print("UpdateTodo - ${res.statusCode}");
      _todos.remove(todo);
      return true;
    }
    print("UpdateTodo - error - ${res.statusCode}");
    return false;
  }

  Future<bool> addTodo(String title, String description) async {
    final res = await _client.post(
        "$baseUrl/todo/${_authenticationService.user.uid}",
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"title": title, "description": description}));

    print("AddTodos - ${res.statusCode}");
    if (res.statusCode == 200) {
      await getTodos(refresh: true);
      return true;
    }
    return false;
  }
}
