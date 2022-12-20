import io
import os
import sys
import json
import base64
import numpy as np
from PIL import Image

os.chdir('..')
print(os.getcwd())
sys.path.append(os.getcwd())


from flask import Flask, Response, request, render_template, send_file, make_response
from sate_flask import api
import requests
import json
from src.mid import inter_user
import yaml

app = Flask(__name__)


# @app.route('/heat', methods=["GET", 'POST', 'OPTIONS'])
# def get_heatmap():
#     # body = json.loads(request.get_data()
#     body = request.form
#     print(body)
#     result = api.get_heatmap()
#     # result = api._()
#     res = Response(str(result))
#     res.headers.add("Access-Control-Allow-Origin", "*")
#     res.headers.add("Access-Control-Allow-Headers", "*")
#     res.headers.add("Access-Control-Allow-Methods", "OPTIONS, POST, GET")
#     return res

# https://scribblinganything.tistory.com/119
@app.route('/SatMap/display', methods=["GET"])
def get_heatmap():
    parameter_dict = request.args.to_dict()
    print(parameter_dict)
    latitude = parameter_dict['latitude']
    longitude = parameter_dict['longitude']
    scale = parameter_dict['scale']
    print("Lat: ", latitude)
    print("Lon: ", longitude)
    print("Scale: ", scale)
    result = api.get_heatmap(latitude, longitude, scale)
    res = Response(str(result))
    res.headers.add("Access-Control-Allow-Origin", "*")
    res.headers.add("Access-Control-Allow-Headers", "*")
    res.headers.add("Access-Control-Allow-Methods", "OPTIONS, POST, GET")
    return res


@app.route('/locate', methods=["GET", "OPTIONS"])
def get_location():
    result = api.get_available()
    res = Response(str(result))
    res.headers.add("Access-Control-Allow-Origin", "*")
    res.headers.add("Access-Control-Allow-Headers", "*")
    res.headers.add("Access-Control-Allow-Methods", "OPTIONS, POST, GET")
    return res

# https://yong0810.tistory.com/22
@app.route('/sate/view', methods=["GET", "POST", "OPTIONS"])
def get_sate_img():
    fn = request.args.get("fn")
    # fn = request.get_data().decode("utf-8").split("=")[-1]
    # fn = json.loads(request.get_data())["fn"]
    
    print("File Name: ", fn)    
    image_fn = api.update_sate_img(fn)
    # image_fn = "/".join(image_fn.split("/")[1:])
    # data_object = {}
    # image = Image.open(image_fn)
    # b = io.BytesIO()
    # # image.save(b, format="jpeg")
    # b.seek(0)
    # data_object["img"] = base64.b64encode(b.read()).decode('ascii')

    # res = make_response(send_file(image_fn, as_attachment=True))
    res = Response(str(render_template('view.html', data_list=[{"dir": image_fn}])))
    res.headers.add("Access-Control-Allow-Origin", "*")
    res.headers.add("Access-Control-Allow-Headers", "*")
    res.headers.add("Access-Control-Allow-Methods", "OPTIONS, POST, GET")
    return res


if __name__=="__main__":
    with open('_config.yml', 'r') as f:
        cfg = yaml.safe_load(f)
    inter_user.turn_on(cfg)
    app.run("0.0.0.0", port=5000)