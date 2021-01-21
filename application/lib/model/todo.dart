import 'package:flutter/material.dart';

class Todo {
  final int id;

  bool isDone = false;

  String title;

  String description;

  Todo(
      {@required this.id,
      @required this.isDone,
      @required this.title,
      @required this.description});

  factory Todo.fromJson(Map<String, dynamic> json) => Todo(
      id: json["id"] as int,
      isDone: json["is_done"] as bool,
      title: json["title"] as String,
      description: json["description"] as String);

  Map<String, dynamic> toJson() =>
      {"title": title, "description": description, "is_done": isDone};
}
