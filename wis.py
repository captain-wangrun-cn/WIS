"""
@ProjectName: WIS (W Image Storage)
@ProjectDescription: 一个简单的图片存储服务，支持进行加密
@Author: WR (captain-wangrun-cn)
@Email: wangrun114514@foxmail.com
@Time: 2024/12/29 12:35
"""
from flask import Flask, render_template, request, send_file, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import sys,getopt,os,base64,io
import util,secure,data

app = Flask(__name__)

@app.route('/api/get_img', methods=['GET'])
def get_img():
    path = request.args.get("path")
    filename = request.args.get("filename")

    if not path or not filename:
        return jsonify({"code": 400, "msg": "Invalid path or filename"}), 400
    
    if path not in util.get_paths():
        return jsonify({"code": 400, "msg": "Invalid path"}), 400
    
    path = util.get_path_by_key(path)

    try:
        if os.path.exists(os.path.join(path, filename)):
            return send_from_directory(path, filename)
        else:
            if os.path.exists(os.path.join(path, filename + ".encrypted")):
                file = util.get_encrypted_file(os.path.join(path, filename + ".encrypted"))
                return send_file(io.BytesIO(file), download_name=filename)
            else:
                return jsonify({"code": 404, "msg": "File not found"}), 404
    except Exception as e:
        return jsonify({"code": 500, "msg": "Internal Server Error", "exception": str(e)}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    json = request.get_json()
    if json is None:
        return jsonify({"code": 400, "msg": "Invalid JSON data"}), 400

    filename = json["filename"]
    path = json["path"]
    file = json["file"]
    need_secure = json["secure"]


    if not filename and not path:
        return jsonify({"code": 400, "msg": "Invalid JSON data"}), 400

    if path not in util.get_paths():
        return jsonify({"code": 400, "msg": "Invalid path"}), 400
    
    try:
        file = base64.b64decode(file)
    except Exception as e:
        return jsonify({"code": 400, "msg": "Invalid file data", "exception": str(e)}), 400

    path = util.get_path_by_key(path)

    try:
        if need_secure:
            file = secure.encrypt(file)
            print("加密中")
            filename += ".encrypted"
        util.save_file(os.path.join(path, filename), file)

        return jsonify({"code": 200, "msg": "Upload success"}), 200
    except Exception as e:
        return jsonify({"code": 500, "msg": "Upload failed", "exception": str(e)}), 500
    

if __name__ == '__main__':
    host="0.0.0.0"
    port=1145

    opts, args = getopt.getopt(sys.argv[1:], "hpd", ["host","port","debug"])
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            host = arg
        if opt in ("-p", "--port"):
            port = int(arg)
        if opt in ("-d", "--debug"):
            app.debug = True

    print(f"WIS is running at {host}:{port} {'in debug mode' if app.debug else ''}")
    data.init()
    app.run(host=host, port=port)
