# Encrypted-Debuggers
-=-=-=-=-=-=--=-=-=-=-=-=REDME.FILES-=--=-=-=-=-=-=-=-=-=-=-=-===

This repository contains code for :
  -live object detection using the YOLOv8 object detection model,
  -live fire detection and alert system
  -
    for the All Nepal Hakathon.
    
    
                                        OBJECT DETECTION USING YOLO
The script captures video from a webcam, runs the YOLOv8 model on each frame, and displays the output with bounding boxes around detected objects and the label and confidence score for each object.
Additionally, the script includes functionality for defining a polygon zone of interest and highlighting objects detected within that zone with a different color.
Getting Started
Prerequisites
  Python 3.6+
  OpenCV
  PyTorch
  NumPy
  
Installation
Clone the repository:
git clone https://github.com/<your-username>/yolov8-live.git

Install the required packages:
pip install -r requirements.txt

Download the pre-trained YOLOv8 model:
wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt

Usage
Run the script with the following command:
python yolov8_live.py

Press the 'Esc' key to exit the program.

------------------------------------------------------------------------------------------------------------------------------------

                       FIRE DETECTION AND ALERT SYSTEM USING OPENCV                                
This is a fire detection system that uses OpenCV to detect fire in real-time using a webcam or any other video input source. When a fire is detected, the system will sound an alarm and send an alert email to the configured email address.

Requirements
  Python 3.x
  OpenCV
  playsound
  smtplib
 
Installation
Clone the repository:
git clone https://github.com/your-username/fire-detection-system.git

Install the required dependencies:
pip install -r requirements.txt

Download the fire detection cascade model file (XML format) and place it in the project directory.

Usage
Run the script:
python fire_detection_system.py

Press q to stop the script.

Configuration
To change the email address that will receive the alert, modify the re variable in the send_mail_function() function.

To change the email address and password used to send the alert email, modify the se and sp variables in the send_mail_function() function
