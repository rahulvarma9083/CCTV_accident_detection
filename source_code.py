from ultralytics import YOLO
import cv2
import math
import keyboard
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


model = YOLO("fire.pt")
classnames = ['fire', 'accident', 'fighting', 'weapon']

incident_data = {}

def send_email_alert(class_name, confidence, frame):
   
    if class_name not in incident_data:
        incident_data[class_name] = {'count': 0, 'images_sent': 0}

    if incident_data[class_name]['images_sent'] < 2:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f'Alert: {class_name} Detected'

        message = f'{class_name} has been detected with a confidence of {confidence}% at srinivasa institute of engineering and technology'
        msg.attach(MIMEText(message, 'plain'))
    
        _, image_buffer = cv2.imencode('.jpg', frame)
        image = MIMEImage(image_buffer.tobytes(), _subtype='jpeg')
        image.add_header('Content-Disposition', f'attachment; filename=incident_frame_{class_name}_{incident_data[class_name]["images_sent"] + 1}.jpg')
        msg.attach(image)
       
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            print(f'Email alert sent for {class_name} - Image {incident_data[class_name]["images_sent"] + 1}')
            incident_data[class_name]['images_sent'] += 1
        except Exception as e:
            print(f'Error sending email: {str(e)}')

    if incident_data[class_name]['images_sent'] >= 2:
        incident_data[class_name]['count'] += 1

        if incident_data[class_name]['count'] == 1:
            print(f'Stopped sending alerts for {class_name}')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("video can't be opened")
    sys.exit()

while True:
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your email here!'
    sender_password = 'your email app password here!'
    recipient_email=''
    ret, frame = cap.read()
    if frame is None:
        print("Unable to read the video")
        break

    if not frame.any():
        continue
   
    frame = cv2.resize(frame, (1280, 720))
    result = model(frame, stream=True)

    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])

            if confidence > 50:
                class_name = classnames[Class]
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                if class_name in ['fire']:
                    recipient_email='email of fire station'
                    print("alert sent to the fire station")
                elif class_name in ['accident' or 'fire' or 'fighting' or 'weapon']:
                    recipient_email='email of police station'
                    print("alert sent to the police station")
                elif class_name in ['accident']:
                    recipient_email='email of hospital'
                    print("alert sent to the hospital")
               
                send_email_alert(class_name, confidence, frame)
                
    cv2.imshow('frame', frame)
    cv2.waitKey(1)

    if keyboard.is_pressed('space'):
        break

cap.release()
cv2.destroyAllWindows()
