import cv2
import threading   
import playsound   
import smtplib     

fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

droidcam_url = "http://192.168.10.76:4747/video"
vid = cv2.VideoCapture(droidcam_url)

runOnce = False

def play_alarm_sound_function(): 
    playsound.playsound('fire_alarm.mp3',True) 
    print("Fire alarm end") 

def send_mail_function():
    
    se = "amanjha3232@gmail.com" 
    sp = "***************" 
    re = "mathtrigo3@gmail.com" 
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(se, sp) 
        server.sendmail(se, re, "Warning fire accident has been reported") 
        print("Alert mail sent successfully to {}".format(re)) 
        server.close()
        
    except Exception as e:
        print(e)

		
while(True):
    Alarm_Status = False
    ret, frame = vid.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        fire = fire_cascade.detectMultiScale(gray, 1.2, 5)

        ## to highlight fire with square 
        for (x,y,w,h) in fire:
            cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            print("Fire alarm initiated")
            threading.Thread(target=play_alarm_sound_function).start() 

            if not runOnce:
                print("Mail send initiated")
                threading.Thread(target=send_mail_function).start()
                runOnce = True
            else:
                print("Mail is already sent once")

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Unable to read frame from camera.")
        break

vid.release()
cv2.destroyAllWindows()