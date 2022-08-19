from flask import Flask, request, jsonify
import util
import logging

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']
    logging.info(image_data)
    response = jsonify(util.classify_image((util.get_cropped_image_if_2_eyes(util.get_cv2_image_from_base64_string(image_data),None),None)))
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":

    app.run(debug=True)
    print("Starting Python Flask Server For Harry Potter Character Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
