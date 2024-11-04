from ultralytics import YOLO
import cv2
import pyttsx3
from collections import Counter
import threading

model = YOLO('best.pt') // Enter the name of your model file here
print(model.names)
textt = "I see "
FPS_wait_coutner = 15


engine = pyttsx3.init()
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('rate', rate*1.5) 
engine.setProperty('volume', volume + 0.5)
counter = 0


def text_to_speech(text):
    if text is None:
        return
    engine.say(text)
    engine.runAndWait()

def calculateDistance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

video_source = 0
cap = cv2.VideoCapture(video_source)
while True:
    ret, frame = cap.read()
    if frame is None:
        print("No Frame Found!")
        break
    width, height, c = frame.shape
    center_point_x, center_point_y = int(width/2), int(height/2)
    if not ret:
        break
    
    result = model(source=frame, show=False, device='cpu')
    box = result[0].boxes
    classes = box.cls
    classes_txt = []
    objects_distances = []
    if len(classes) == 0:
        textt = "No objects detected."
    else:
        
        for i in range(len(classes)):
            cls = int(classes[i].tolist())
            name = result[0].names[cls]
            classes_txt.append(name)
            conf = box.conf[i]
            x1, y1, x2, y2 = box.xyxy[i].tolist()
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            distance = calculateDistance(center_point_x, center_point_y, (x1+x2)/2, (y1+y2)/2)
            objects_distances.append(distance)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{name}: {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
        nearest_object = ""
        if len(objects_distances) > 0:
            min_distance = min(objects_distances)
            min_distance_index = objects_distances.index(min_distance)
            min_distance_object = classes_txt[min_distance_index]
            nearest_object = f" and the nearest object is {min_distance_object}."
        counter += 1
        cv2.waitKey(1)
        duplicates = Counter(classes_txt)
        for value, count in duplicates.items():
            textt += f"{count}: {value}, "
            print(f"{value}: {count} duplicates")
        classes_txt = []
        if counter == FPS_wait_coutner:
            textt += nearest_object
            threading.Thread(target=text_to_speech, args=(textt,)).start()
            counter = 0

        textt = "I see"
        nearest_object = ""
        cv2.imshow("frame: ", frame)
cv2.destroyAllWindows()
cap.release()
exit()
