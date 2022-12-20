import 'package:flutter/material.dart';
import 'package:h2m_sate/api/server.dart';
import 'package:h2m_sate/api/location.dart';
import 'package:h2m_sate/sidemenu.dart';
import 'package:h2m_sate/style/pallete.dart';
import 'package:h2m_sate/widget/appbar.dart';

class LocationSearch extends StatefulWidget {
  LocationSearch({super.key});
  Pallete pallete = Pallete();

  @override
  State<LocationSearch> createState() => _LocationSearchState();
}

class _LocationSearchState extends State<LocationSearch> {
  final TextEditingController _textController = new TextEditingController();
  String search_key = "";
  Future<String> future = load_location();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        drawer: SideMenu(),
        appBar: AppbarTop(
          title: "지역 검색",
        ),
        body: Column(
          children: <Widget>[
            Row(
              children: [
                Flexible(
                  flex: 1,
                  child: TextField(
                    controller: _textController,
                    cursorColor: Colors.grey,
                    decoration: InputDecoration(
                        fillColor: Colors.white,
                        filled: true,
                        border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(10),
                            borderSide: BorderSide.none),
                        hintText: 'Search',
                        hintStyle: TextStyle(
                            color: widget.pallete.purple50, fontSize: 18),
                        prefixIcon: Padding(
                            padding: const EdgeInsets.all(15),
                            child: const Icon(Icons.search))),
                  ),
                ),
                GestureDetector(
                  onTap: () {
                    setState(() {
                      // search_key = _textController.text;
                      print(_textController.text);
                    });
                  },
                  child: Container(
                    margin: EdgeInsets.only(left: 10),
                    padding: EdgeInsets.all(15),
                    decoration: BoxDecoration(
                        color: widget.pallete.hightlight,
                        borderRadius: BorderRadius.circular(5)),
                    child: Icon(Icons.send),
                    width: 50,
                  ),
                )
              ],
            ),
            Flexible(
                child: FutureBuilder(
              future: future,
              builder: (BuildContext context, AsyncSnapshot snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return CircularProgressIndicator();
                } else if (snapshot.hasError) {
                  print("에러!");
                  return Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      'Error: ${snapshot.error}',
                      style: TextStyle(fontSize: 15),
                    ),
                  );
                } else {
                  List<Location> locations = parse_coors(snapshot.data);
                  List<Location> search_result =
                      search_location(locations, _textController.text);
                  return ListView.builder(
                    itemCount: search_result.length,
                    itemBuilder: (BuildContext context, int index) {
                      Location location = search_result[index];
                      String loca_info =
                          "Latitude : ${location.lat.toStringAsFixed(2)}, Longitude : ${location.lon.toStringAsFixed(2)}";
                      return ListTile(
                        title: Text(location.fn),
                        trailing: Text(loca_info),
                        onTap: (() {
                          Navigator.pushNamed(context, '/sate', arguments: {
                            "lat": location.lat,
                            "lon": location.lon,
                            "scale": 0.7,
                            "fn": location.fn,
                          });
                        }),
                      );
                    },
                  );
                }
              },
            ))
          ],
        ));
  }
}

List<Location> search_location(List<Location> total, String _search_key) {
  if (_search_key == "") {
    return total;
  } else {
    List<Location> res = [];
    for (Location corp in total) {
      if (corp.fn.contains(_search_key)) {
        res.add(corp);
      }
    }
    return res;
  }
}
