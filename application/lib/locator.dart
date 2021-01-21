
import 'package:get_it/get_it.dart';
import 'package:todolist/services/authentication_service.dart';
import 'package:todolist/services/todos_api.dart';

GetIt locator = GetIt.instance;

setupLocator() {
  locator.registerLazySingleton(() => AuthenticationService());
  locator.registerLazySingleton(() => TodosApi());
}
