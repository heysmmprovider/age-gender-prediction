import insightface
from insightface.app import FaceAnalysis
from flask import Flask, request, jsonify
import numpy as np
import cv2
import base64 

app = Flask(__name__)

# Initialize face analyzer
face_analyzer = FaceAnalysis(
    name='buffalo_l',
    root='models', 
    providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
)
face_analyzer.prepare(ctx_id=0, det_size=(640, 640))

@app.route("/", methods=["POST"])
def predict_age_gender():
    try:
        data = request.get_json()
        if not data or 'img' not in data:
            return jsonify({"error": "Invalid request format"}), 400

        img_array = np.frombuffer(base64.b64decode(data['img']), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        
        faces = face_analyzer.get(img)
        
        ages = []
        genders = []
        
        for face in faces:
            age = {
                "mean": float(face.age),
                "entropy": 0.2  # InsightFace doesn't provide uncertainty
            }
            
            gender = {
                "f": float(face.sex == 0),
                "m": float(face.sex == 1),
                "entropy": 0.1
            }
            
            ages.append(age)
            genders.append(gender)

        return jsonify({
            "ages": ages,
            "genders": genders
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10003)
