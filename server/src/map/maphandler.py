
import requests
import folium

#naver map api key
client_id = 'kzz7jjmf20';   # 본인이 할당받은 ID 입력
client_secret = 'W1o0IkAKHOSGOZYyBXWslLQFwf6g6p7IzmqgChrp'    # 본인이 할당받은 Secret 입력

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

coords_test = "126.969594,37.586541"
coords_test_lat = 126.969594
coords_test_lon = 37.586541
output = "json"
orders = 'addr'
endpoint = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
url = f"{endpoint}?coords={coords_test}&output={output}&orders={orders}"

# 헤더
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
}

# 요청
res = requests.get(url, headers=headers)
print(res.json())

map_osm = folium.Map(location = [coords_test_lon, coords_test_lat], zoom_start=16)
folium.Marker([coords_test_lon, coords_test_lat]).add_to(map_osm)
map_osm.save('testMapAPI.html')

def calscale() :
    return