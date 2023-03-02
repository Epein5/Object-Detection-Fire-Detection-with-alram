import smtplib
import cv2
import argparse
import smtpd
from ultralytics import YOLO
import supervision as sv
import numpy as np
import playsound
ZONE_POLYGON = np.array([
    [0, 0],
    [0.5, 0],
    [0.5, 1],
    [0, 1]
])

def intersect(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    
    x_intersect = not (x1 + w1 < x2 or x2 + w2 < x1)
    y_intersect = not (y1 + h1 < y2 or y2 + h2 < y1)
    
    return x_intersect and y_intersect

def send_mail():
    sender_email = "knypein@gmail.com"
    sender_password = "uxferwaeuqxxnyij"
    recipient_email = "aayushgtm5@gmail.com"
    
    try:
        server = smtplib.SMTP('aayushgtm5@gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, "Warning fire accident has been reported")
        print("Alert mail sent successfully to {}".format(recipient_email))
        server.close()
    
    except Exception as e:
        print(e)

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution", 
        default=[1280, 720], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution
    cap = cv2.VideoCapture('hawa.mp4')
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("yolov8l.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    zone_polygon = (ZONE_POLYGON * np.array(args.webcam_resolution)).astype(int)
    zone = sv.PolygonZone(polygon=zone_polygon, frame_resolution_wh=tuple(args.webcam_resolution))
    zone_annotator = sv.PolygonZoneAnnotator(
        zone=zone, 
        color=sv.Color.red(),
        thickness=2,
        text_thickness=4,
        text_scale=2
    )
    while True:
        ret, frame = cap.read()

        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)
        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]
        
        # Check if any two bounding boxes intersect
        for i in range(len(detections)):
            for j in range(i+1, len(detections)):
                try:
                    if intersect(detections[i].bbox, detections[j].bbox):
                        print("Intersection detected!")
                except Exception:
                    print('detected')
                    m=0
                    if(m==0):
                        send_mail()
                        m=m+1
                    else:
                        pass


        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections, 
            labels=labels
        )

        zone.trigger(detections=detections)
        frame = zone_annotator.annotate(scene=frame)      
        
        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27):
            break


if __name__ == "__main__":
    main()