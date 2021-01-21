import 'package:flutter/material.dart';
import 'package:todolist/locator.dart';
import 'package:todolist/model/todo.dart';
import 'package:todolist/services/todos_api.dart';

class TodoList extends StatefulWidget {
  @override
  _TodoListState createState() => _TodoListState();
}

class _TodoListState extends State<TodoList> {
  final TodosApi _api = locator<TodosApi>();

  final _formKey = GlobalKey<FormState>();

  final _listKey = GlobalKey<AnimatedListState>();

  String _title;

  String _description;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: false,
        title: Text("Vos todos"),
      ),
      body: FutureBuilder<List<Todo>>(
          future: _api.getTodos(),
          builder: (context, snapshot) => _buildBody(snapshot)),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () async {
          showModalBottomSheet(
                  isDismissible: true,
                  enableDrag: true,
                  isScrollControlled: true,
                  shape: const RoundedRectangleBorder(
                      borderRadius: BorderRadius.only(
                          topLeft: Radius.circular(10),
                          topRight: Radius.circular(10))),
                  builder: _buildBottomSheet,
                  context: context)
              .whenComplete(() => setState(() {}));
        },
      ),
    );
  }

  Widget _buildBody(AsyncSnapshot<List<Todo>> snapshot) {
    if (snapshot.connectionState != ConnectionState.done) {
      return Center(
        child: CircularProgressIndicator(),
      );
    }

    if (_api.todos.isEmpty) {
      // Pas de todos!
      return Center(
        child: Text("Vous n'avez plus de todo à faire!",
            style: Theme.of(context).textTheme.headline6),
      );
    }

    // Affiche les todos
    return AnimatedList(
        key: _listKey,
        initialItemCount: _api.todos.length,
        itemBuilder: (context, index, animation) =>
            _buildListItem(context, _api.todos[index], animation));
  }

  Widget _buildListItem(
          BuildContext context, Todo todo, Animation<double> animation) =>
      FadeTransition(
        opacity: animation,
        child: Padding(
          padding: const EdgeInsets.all(4.0),
          child: todo.description.isEmpty
              ? CheckboxListTile(
                  title: Text(todo.title),
                  value: todo.isDone,
                  onChanged: (value) => _onChanged(todo))
              : CheckboxListTile(
                  title: Text(todo.title),
                  subtitle: Text(todo.description),
                  value: false,
                  onChanged: (value) => _onChanged(todo)),
        ),
      );

  void _onChanged(Todo todo) async {
    // setState(() {
      todo.isDone = !todo.isDone;
      _listKey.currentState.removeItem(_api.todos.indexOf(todo),
          (context, animation) => _buildListItem(context, todo, animation),
          duration: const Duration(milliseconds: 200));
    // });
    await _api.updateTodo(todo);
  }

  Widget _buildBottomSheet(BuildContext context) => Card(
        child: Padding(
          padding: EdgeInsets.fromLTRB(
              8.0, 0, 8, MediaQuery.of(context).viewInsets.bottom),
          child: Form(
            key: _formKey,
            child: SingleChildScrollView(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  Center(
                    child: Padding(
                      padding: const EdgeInsets.only(top: 5.0),
                      child: Container(
                        height: 5,
                        width: 50,
                        decoration: const BoxDecoration(
                            color: Colors.grey,
                            borderRadius:
                                BorderRadius.all(Radius.circular(8.0))),
                      ),
                    ),
                  ),
                  SizedBox(height: 8.0),
                  TextFormField(
                    validator: (value) =>
                        value.isEmpty ? "Veuillez saisir un titre" : null,
                    onSaved: (value) => _title = value,
                    decoration: InputDecoration(
                        border: const OutlineInputBorder(),
                        filled: true,
                        labelText: "Titre"),
                  ),
                  SizedBox(height: 8.0),
                  TextFormField(
                    onSaved: (value) => _description = value,
                    decoration: InputDecoration(
                      border: const OutlineInputBorder(),
                      filled: true,
                      labelText: "Description",
                    ),
                    maxLines: 3,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      RaisedButton(
                          onPressed: () async {
                            if (_formKey.currentState.validate()) {
                              _formKey.currentState.save();
                              await _api.addTodo(_title, _description);
                              Navigator.of(context).pop();
                            }
                          },
                          child: Text("Ajouter")),
                    ],
                  )
                ],
              ),
            ),
          ),
        ),
      );
}
