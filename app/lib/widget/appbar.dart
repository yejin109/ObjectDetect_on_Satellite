import 'package:flutter/material.dart';
import 'package:h2m_sate/sidemenu.dart';
import 'package:h2m_sate/style/pallete.dart';

class AppbarTop extends StatelessWidget implements PreferredSizeWidget {
  @override
  Size preferredSize = const Size.fromHeight(60.0);
  Pallete pallete = Pallete();
  final String title;

  AppbarTop({required this.title, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      iconTheme: IconThemeData(color: pallete.purple100),
      elevation: 0,
      title: Container(
        margin: const EdgeInsets.fromLTRB(0, 15, 0, 0),
        child: Text(
          this.title,
          style: TextStyle(
              color: pallete.purple10,
              // color: Color(0xffb3cde0),
              fontSize: 30,
              fontWeight: FontWeight.bold),
        ),
      ),
      backgroundColor: Colors.white,
      // leading:
      // GestureDetector(
      //   child: Container(
      //     margin: const EdgeInsets.all(10),
      //     width: 40,
      //     height: 40,
      //     child: Icon(
      //       Icons.arrow_back,
      //       size: 30,
      //       color: pallete.smallButton,
      //     ),
      //   ),
      //   onTap: () {
      //     Navigator.pop(context);
      //   },
      // ),
      actions: <Widget>[],
    );
  }
}
