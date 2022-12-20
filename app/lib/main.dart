import 'package:flutter/material.dart';
import 'package:h2m_sate/page/locationList.dart';
import 'package:h2m_sate/page/satellite.dart';
import 'package:h2m_sate/page/topographic.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SatMap',
      theme: ThemeData(
        primarySwatch: Colors.purple,
      ),
      initialRoute: '/locate',
      routes: {
        '/sate': (BuildContext context) => const SateMap(),
        '/topo': (BuildContext context) => const TopoMap(),
        '/locate': (BuildContext context) => LocationSearch()
      },
    );
  }
}
