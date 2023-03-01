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
  
  ---------------------------------------------------------------------------------------------------------------------------------------------------------
                  
                                              Object Detection and Segmentation with YOLOv5
This project demonstrates how to use YOLOv5 to perform object detection and segmentation on images and videos. Specifically, it includes the following functionalities:

Detection of objects in images and videos, with optional saving of the resulting images and text files containing the object labels and confidence scores.
Segmentation of objects in images and videos, with optional hiding of the labels and confidence scores.
Export of YOLOv5 models to the ONNX format.
The code is implemented in Python 3, using the PyTorch deep learning library and the Ultralytics YOLOv5 implementation.

Installation
To use this project, you need to have Python 3 and PyTorch installed on your system. You also need to install the Ultralytics YOLOv5 package, which can be done with the following command:
pip install ultralytics==8.0.0
  
Additionally, you need to have FFmpeg installed if you want to compress the video outputs.
  
Usage
The main functionality of this project is provided by the yolo script, which can be run with the following command:
!yolo task=<task> mode=<mode> model=<model> source=<source> [other options]
Here, the task parameter specifies the YOLOv5 task to perform, which can be either detect for object detection or segment for segmentation. The mode parameter specifies the mode of operation, which can be either predict to make predictions or export to export a YOLOv5 model to the ONNX format. The model parameter specifies the path to the YOLOv5 model file to use. The source parameter specifies the path to the input image or video file to process.

In addition to these mandatory parameters, there are several optional parameters that can be used to customize the behavior of the yolo script. Some of the most important ones are:

save_txt=True to save the object labels and confidence scores to a text file.
hide_labels=True to hide the object labels in the output images or videos.
hide_conf=True to hide the object confidence scores in the output images or videos.
conf=<confidence> to set the confidence threshold for object detection or segmentation.
For more information about the available parameters and their usage, please refer to the comments in the yolo.py file.

Examples
Here are some examples of how to use the yolo script:
# Object detection on a video
!yolo task=detect mode=predict model=yolov8s.pt source='/content/VID-20230301-WA0000.mp4'

# Object detection on a video with compressed output
!rm "/content/result_compressed.mp4"
!yolo task=detect mode=predict model=yolov8s.pt source='/content/VID-20230302-WA0001.mp4' 
save_path = '/content/runs/detect/predict3/VID-20230302-WA0001.mp4'
compressed_path = "/content/result_compressed.mp4"
os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

