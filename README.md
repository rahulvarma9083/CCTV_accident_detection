# Accident & Incident Detection System 🚨

This project is an AI-powered real-time surveillance system that uses **YOLO (You Only Look Once)** for object detection to identify critical incidents such as **fire, accidents, fighting, and weapons** from live CCTV footage. Once an incident is detected with high confidence, the system automatically sends an **email alert** (with attached frame evidence) to the appropriate authority such as the **fire station, police station, or hospital**.

## 🔹 Key Features
- **Real-time Detection:** Detects fire, accidents, fighting, and weapons using YOLO from live video streams.
- **Automated Alerts:** Sends email notifications with attached incident images to relevant authorities.
- **Customizable Notification System:**
  - Fire → Fire Station & Police Station  
  - Accident → Hospital & Police Station  
  - Fighting/Weapon → Police Station
- **Incident Management:** Limits repeated email alerts to avoid spamming while ensuring critical alerts are sent.
- **Easy Integration:** Works with CCTV cameras or webcam streams.

## 🔹 Technologies Used
- **Python** – core programming language  
- **YOLO (Ultralytics)** – real-time object detection  
- **OpenCV** – video capture and frame processing  
- **smtplib + MIME (Python Email Library)** – sending email alerts with images  
- **Math & Keyboard libraries** – confidence thresholding and user control  

## 🔹 Use Cases
- Campus surveillance (schools, colleges, universities)  
- Public safety monitoring (roads, public areas, offices)  
- Smart city security solutions  
- Industrial safety monitoring  

---

⚡ With this project, emergency services can be **instantly alerted** about dangerous incidents, helping save lives and prevent damage.
