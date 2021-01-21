import 'package:firebase_auth/firebase_auth.dart';

class AuthenticationService {
  final FirebaseAuth _firebaseAuth = FirebaseAuth.instance;

  User _user;

  User get user => _user;

  Future<User> signIn() async {
    final userCredential = await _firebaseAuth.signInAnonymously();

    _user = userCredential.user;

    return _user;
  }
}
