from flask import Flask, render_template, Blueprint, request, redirect, url_for
from ultralytics import YOLO
import io
from PIL import Image
import base64
import cv2
import os

app = Flask(__name__)

detection = Blueprint('detection', __name__, url_prefix='/analysis')

seaf_command = Blueprint('pages', __name__, url_prefix='/seaf_command')

@seaf_command.route('/intelligence', methods=['GET'])
def detectionRequestPage():
    return render_template('input_page.html')

def runAnalysis(image):
    
    image = image.convert('RGB')
    image = image.resize((800, 800))
    
    model = YOLO('./best.torchscript', task='detect')

    results = model.predict(
        source=image, 
        task='detect',
        conf=0.25,
        iou=0.5,
        verbose=False
    )
    
    lockedOnImagery = results[0].plot()
    
    _, bytes = cv2.imencode('.png', lockedOnImagery)
    lockedOnImagery_encoded = base64.b64encode(bytes).decode('utf-8')

    detectionList = []
    boxes = results[0].boxes

    classLabels = {0: "Helldiver (Friend)", 1: "Rocket Devastator (Target)"}

    
    if boxes is not None:
        for i, box in enumerate(boxes):
            cornerCoords = box.xyxy[0].tolist()
            confidence = float(box.conf[0])
            classIdInt = int(box.cls[0])
            
            classLabel = classLabels.get(classIdInt, f"Class_{classIdInt}")

            topLeftCornerX = round(cornerCoords[0], 2)
            topLeftCornerY = round(cornerCoords[1], 2)

            bottomRightCornerX = round(cornerCoords[2], 2)
            bottomRightCornerY = round(cornerCoords[3], 2)

            detectionInfo = {
                'id': i + 1,
                'classLabel': classLabel,
                'classID': classIdInt,
                'confidence': confidence,
                'coordinates': {
                    'x1': topLeftCornerX,
                    'y1': topLeftCornerY,
                    'x2': bottomRightCornerX,
                    'y2': bottomRightCornerY
                },
                'center': {
                    'x': round( ( topLeftCornerX + bottomRightCornerX ) / 2, 2),
                    'y': round( ( topLeftCornerY + bottomRightCornerY ) / 2, 2)
                },
                'width': round( bottomRightCornerX - topLeftCornerX , 2),
                'height': round( bottomRightCornerY - topLeftCornerY , 2)
            }

            detectionList.append(detectionInfo)
    
    return detectionList, lockedOnImagery_encoded

@detection.route('/rdev', methods=['POST'])
def detectRdev():
   if request.method == 'POST':
       image = request.files['image']
       if image:
            binaryImage = image.read()
            imageObject = Image.open(io.BytesIO(binaryImage))
            imageName = image.filename

            try:
                detectionList, lockedOnImagery_encoded = runAnalysis(imageObject)
                
                friendsDetectedCount = sum(1 for i in detectionList if i['classID'] == 0)
                targetsDetectedCount = sum(1 for i in detectionList if i['classID'] == 1)

                return render_template('results_page.html',
                                    imageName=imageName,
                                    friendsDetectedCount=friendsDetectedCount,
                                    targetsDetectedCount=targetsDetectedCount,
                                    detectionList=detectionList,
                                    image_encoding=lockedOnImagery_encoded)
            
            except Exception as e:
                return render_template('results_page.html',
                                    imageName=imageName,
                                    friendsDetectedCount=0,
                                    targetsDetectedCount=0,
                                    detectionList=[],
                                    image_encoding=None,
                                    error=f"Error during analysis: {str(e)}")
       else:
           return "No image uploaded.", 400

@app.route('/')
def home():
    return redirect(url_for('pages.detectionRequestPage'))

seaf_command.register_blueprint(detection)
app.register_blueprint(seaf_command)
      
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)
