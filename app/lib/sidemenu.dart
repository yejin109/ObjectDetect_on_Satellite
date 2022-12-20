import 'package:flutter/material.dart';
import 'package:h2m_sate/page/satellite.dart';
import 'package:h2m_sate/page/topographic.dart';
import 'package:h2m_sate/style/pallete.dart';

class SideMenu extends StatelessWidget {
  Pallete pallete = Pallete();
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: <Widget>[
          DrawerHeader(
            child: Text(
              'Map Selection',
              style: TextStyle(color: Colors.white, fontSize: 25),
            ),
            decoration: BoxDecoration(
              color: Colors.purple[200],
              // image: DecorationImage(
              //     fit: BoxFit.fill,
              //     image: AssetImage('assets/images/cover.jpg'))
            ),
          ),
          // ListTile(
          //   leading: Icon(Icons.map),
          //   title: Text('일반 지도'),
          //   onTap: () => {
          //     Navigator.pushAndRemoveUntil(
          //         context,
          //         MaterialPageRoute(
          //             builder: (BuildContext context) =>
          //                 const MyHomePage(title: "SatMap")),
          //         ModalRoute.withName("/home"))
          //   },
          // ),
          ListTile(
            leading: Icon(Icons.public),
            title: Text('위성 지도'),
            onTap: () {
              print("NOT YET");
            },
          ),
          // ListTile(
          //   leading: Icon(Icons.explore),
          //   title: Text('지역 검색'),
          //   onTap: () => {Navigator.pushNamed(context, "/locate")},
          // ),
        ],
      ),
    );
  }
}
