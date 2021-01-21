import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:todolist/locator.dart';
import 'package:todolist/services/authentication_service.dart';
import 'package:todolist/ui/something_went_wrong.dart';
import 'package:todolist/ui/todo_list.dart';

class LoginView extends StatelessWidget {
  final AuthenticationService _authenticationService =
      locator<AuthenticationService>();

  @override
  Widget build(BuildContext context) => FutureBuilder(
      future: _authenticationService.signIn(),
      builder: (context, snapshot) {
        // Connexion échoué -> affiche login
        if (snapshot.connectionState == ConnectionState.none) {
          return SomethingWentWrong();
        }

        // Connexion réussi -> affiche écran suivant.
        if (snapshot.connectionState == ConnectionState.done) {
          return TodoList();
        }

        // Connexion en cours -> affiche loader.
        return Scaffold(
          body: Center(
            child: CircularProgressIndicator(),
          ),
        );
      });
}
