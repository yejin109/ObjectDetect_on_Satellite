class Location {
  List<double> _lats = [];
  List<double> _lons = [];
  double _lat = -1;
  double _lon = -1;
  int _scale = -1;
  String fn = "";

  Location(this._lats, this._lons);

  Location.parse(List<double> lats, List<double> lons, String fn) {
    this._lats = lats;
    this._lons = lons;
    this._lat = lats.map((m) => m).reduce((a, b) => a + b) / lats.length;
    this._lon = lons.map((m) => m).reduce((a, b) => a + b) / lons.length;
    this.fn = fn;
  }

  set scale(int scale) {
    this._scale = scale;
  }

  get lat => this._lat;
  get lon => this._lon;
}

List<Location> parse_coors(String source) {
  List<Location> res = [];
  List<String> coors = source.split("&");
  for (String coor in coors) {
    List<String> tc = coor.split("?");
    List<String> points = tc[1].split("#");
    List<double> lats = [];
    List<double> lons = [];

    for (String point in points) {
      if (point.length == 0) continue;
      List<String> tmp = point.split(":");
      if (tmp.length == 0) continue;
      lats.add(double.parse(tmp[0]));
      lons.add(double.parse(tmp[1]));
    }

    res.add(Location.parse(lats, lons, tc[0]));
  }
  return res;
}
