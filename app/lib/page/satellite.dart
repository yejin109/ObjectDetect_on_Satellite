import 'package:flutter/material.dart';
import 'package:h2m_sate/widget/appbar.dart';
import 'package:h2m_sate/api/server.dart';
import 'package:url_launcher/url_launcher.dart';
import 'dart:async';

class SateMap extends StatefulWidget {
  const SateMap({Key? key}) : super(key: key);

  @override
  State<SateMap> createState() => _SateMapState();
}

class _SateMapState extends State<SateMap> {
  void initState() {
    super.initState();
    // Enable virtual display.
  }

  @override
  Widget build(BuildContext context) {
    Map<String, dynamic>? info =
        ModalRoute.of(context)!.settings.arguments as Map<String, dynamic>?;
    double lat = info!["lat"] ?? "";
    double lon = info['lon'] ?? "";
    double scale = info['scale'] ?? "";
    String fn = info["fn"] ?? "";
    Future<String> future = load_sate_img(fn);
    return Scaffold(
      appBar: AppbarTop(title: fn),
      body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: EdgeInsets.all(50),
              child: Container(child: Text(fn)),
            ),
            ElevatedButton(
              child: Text("Open Link"),
              onPressed: () async {
                // final url = Uri.parse("http://10.0.2.2:5000/sate/view?fn=$fn");
                final url = Uri.parse("http://127.0.0.1:5000/sate/view?fn=$fn");
                // String url = "http://10.0.2.2:5000/sate/view?fn=$fn";
                if (await canLaunchUrl(url)) {
                  launchUrl(url, mode: LaunchMode.externalApplication);
                }
              },
            ),
            ElevatedButton(
              child: Text("Open Link"),
              onPressed: () async {
                // final url = Uri.parse("http://10.0.2.2:5000/sate/view?fn=$fn");
                final url = Uri.parse("http://127.0.0.1:5000/sate/view?fn=$fn");
                // String url = "http://10.0.2.2:5000/sate/view?fn=$fn";
                if (await canLaunchUrl(url)) {
                  launchUrl(url, mode: LaunchMode.externalApplication);
                }
              },
            )
          ]),
      // WebView(
      //   initialUrl: 'http://10.0.2.2:5000/sate/view?fn=$fn',
      //   // onWebViewCreated: (WebViewController webViewController) {
      //   //   _controller = webViewController;
      //   //   _loadHtmlFromAssets(snapshot.data);
      //   // },
      // )

      // FutureBuilder(
      //   future: future,
      //   builder: (BuildContext context, AsyncSnapshot snapshot) {
      //     if (snapshot.connectionState == ConnectionState.waiting) {
      //       return CircularProgressIndicator();
      //     } else if (snapshot.hasError) {
      //       return Padding(
      //         padding: const EdgeInsets.all(8.0),
      //         child: Text(
      //           'Error: ${snapshot.error}',
      //           style: TextStyle(fontSize: 15),
      //         ),
      //       );
      //     }
      //     return
      //     // WebView(
      //     //   initialUrl: 'https://flutter.dev',
      //     //   // onWebViewCreated: (WebViewController webViewController) {
      //     //   //   _controller = webViewController;
      //     //   //   _loadHtmlFromAssets(snapshot.data);
      //     //   // },
      //     // );
      //     // Text(snapshot.data);
      //     // return Image.memory(base64Decode(snapshot.data));
      //   },
      // ),
    );
  }

  // _loadHtmlFromAssets(String fileText) async {
  //   _controller.loadUrl(Uri.dataFromString(fileText,
  //           mimeType: 'text/html', encoding: Encoding.getByName('utf-8'))
  //       .toString());
  // }
}
