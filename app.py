from flask import Flask, request, jsonify, render_template
import os
import brain_tumor

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    print(request.files)
    if 'input' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['input']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    try:
        prediction = brain_tumor.main(file_path)
        os.remove(file_path)
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
