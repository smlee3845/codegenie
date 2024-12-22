from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/style-guide", methods=["GET"])
def get_style_guide():
    style_path = "settings/default_style.json"
    output_path = "style_guide.md"
    with open(style_path, "r") as file:
        style = json.load(file)
    with open(output_path, "r") as file:
        guide_content = file.read()
    return jsonify({"style": style, "guide": guide_content})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
