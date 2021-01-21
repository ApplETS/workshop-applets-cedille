
import 'package:get_it/get_it.dart';
import 'package:todolist/services/authentication_service.dart';

GetIt locator = GetIt.instance;

setupLocator() {
  locator.registerLazySingleton(() => AuthenticationService());
}
