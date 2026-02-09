import os
from flask import Flask, send_file, jsonify

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

AVATAR_DIR = "avatars"
DEFAULT_AVATAR = os.path.join(AVATAR_DIR, "-1.png")

# create avatars directory if it does not exist
os.makedirs(AVATAR_DIR, exist_ok=True)


@app.route("/status")
def server_status():
    return jsonify({"response": 200, "status": 1})


@app.route("/<int:uid>")
def serve_avatar(uid):
    avatar_path = os.path.join(AVATAR_DIR, f"{uid}.png")
    if os.path.isfile(avatar_path):
        return send_file(avatar_path)
    return send_file(DEFAULT_AVATAR)


@app.errorhandler(404)
def page_not_found(error):
    return send_file(DEFAULT_AVATAR)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5020)
