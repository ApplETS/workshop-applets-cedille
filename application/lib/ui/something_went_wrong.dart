import 'package:flutter/material.dart';
import 'package:todolist/ui/login.dart';

class SomethingWentWrong extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text("Oups! Quelque chose n'a pas fonctionné comme prévu..."),
              IconButton(
                  icon: Icon(Icons.refresh),
                  onPressed: () {
                    Navigator.of(context).push(
                        MaterialPageRoute(builder: (context) => LoginView()));
                  })
            ],
          ),
        ),
      );
}
