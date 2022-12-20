// import 'dart:html';
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<String> load_heatmap(double lat, double lon, double scale) async {
  print("Call heatmap");
  Map<String, String> headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Method": "*",
    'Access-Control-Allow-Headers': '*',
    "Connection": "Keep-Alive",
    "Keep-Alive": "timeout=5, max=1000"
  };
  Map<String, String> data = {
    "latitude": lat.toString(),
    "longitude": lon.toString(),
    "scale": scale.toString(),
  };
  var body = jsonEncode(data);
  // https://eunjin3786.tistory.com/266
  http.Response response = await http.get(
    Uri.parse(
        "http://127.0.0.1:5000/SatMap/display?latitude=$lat&longitude=$lon&scale=$scale"),
    // Uri.parse("http://192.168.45.230:5000/heat"),
    // Uri.parse("http://192.168.45.230:5000/heat"),
    headers: headers,
  );
  String res = utf8.decode(response.bodyBytes);
  print("응답");
  return res;
}

Future<String> load_location() async {
  Map<String, String> headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Method": "*",
    'Access-Control-Allow-Headers': '*',
    "Connection": "Keep-Alive",
    "Keep-Alive": "timeout=10, max=10000"
  };

  // https://eunjin3786.tistory.com/266
  http.Response response = await http.get(
    // APP
    // Uri.parse("http://10.0.2.2:5000/locate"),
    // Window
    Uri.parse("http://127.0.0.1:5000/locate"),
    headers: headers,
  );
  String res = utf8.decode(response.bodyBytes);
  print("응답");
  return res;
}

Future<String> load_sate_img(String fn) async {
  Map<String, String> headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Method": "*",
    'Access-Control-Allow-Headers': '*',
    "Connection": "Keep-Alive",
    "Keep-Alive": "timeout=5, max=1000"
  };
  Map<String, String> data = {
    "fn": fn,
  };
  // https://eunjin3786.tistory.com/266
  // final response =
  //     await Dio().post("http://127.0.0.1:5000/sate/view", data: data);
  http.Response response = await http.post(
      Uri.parse("http://127.0.0.1:5000/sate/view"),
      headers: headers,
      body: data);
  // File file = File(response.bodyBytes, "tmp.png");
  String res = utf8.decode(response.bodyBytes);
  // String imageStr = json.decode(response.data)["img"].toString();
  print("응답");
  return res;
}
