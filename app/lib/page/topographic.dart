import 'package:flutter/material.dart';
import 'package:h2m_sate/api/server.dart';
import 'package:h2m_sate/widget/appbar.dart';

class TopoMap extends StatefulWidget {
  const TopoMap({Key? key}) : super(key: key);

  @override
  State<TopoMap> createState() => _TopoMapState();
}

class _TopoMapState extends State<TopoMap> {
  @override
  Widget build(BuildContext context) {
    Map<String, dynamic>? info =
        ModalRoute.of(context)!.settings.arguments as Map<String, dynamic>?;
    double lat = info!["lat"] ?? "";
    double lon = info['lon'] ?? "";
    double scale = info['scale'] ?? "";
    Future<String> future = load_heatmap(lat, lon, scale);
    return Scaffold(
        appBar: AppbarTop(
          title: "히트맵",
        ),
        body: FutureBuilder(
          future: future,
          builder: (BuildContext context, AsyncSnapshot snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return CircularProgressIndicator();
            } else if (snapshot.hasError) {
              return Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  'Error: ${snapshot.error}',
                  style: TextStyle(fontSize: 15),
                ),
              );
            }
            print(snapshot.data);
            return Container(
              child: Text(snapshot.data),
            );
          },
        ));
  }
}
