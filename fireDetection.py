import cv2
import threading   # Library for threading -- which allows code to run in backend
import playsound   # Library for alarm sound
import smtplib     # Library for email sending

fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')
 # To access xml file which includes positive and negative images of fire. (Trained images)
                                                                         # File is also provided with the code.

# Set up the DroidCam video stream
droidcam_url = "http://192.168.10.76:4747/video"
vid = cv2.VideoCapture(droidcam_url)

runOnce = False # created boolean

def play_alarm_sound_function(): # defined function to play alarm post fire detection using threading
    playsound.playsound('fire_alarm.mp3',True) # to play alarm # mp3 audio file is also provided with the code.
    print("Fire alarm end") # to print in consol

def send_mail_function(): # defined function to send mail post fire detection using threading
    
    sender_email = "amanjha3232@gmail.com" # your email ID
    sender_password = "sligaxttpgwvygwd" # your email password
    recipient_email = "mathtrigo3@gmail.com" # recipient email ID
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password) # sender's email ID and password
        server.sendmail(sender_email, recipient_email, "Warning fire accident has been reported") # recipient's email with mail message
        print("Alert mail sent successfully to {}".format(recipient_email)) # to print in console to whom mail is sent
        server.close() ## To close server
        
    except Exception as e:
        print(e) # To print error if any

		
while(True):
    Alarm_Status = False
    ret, frame = vid.read() # Value in ret is True # To read video frame
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # To convert frame into gray color
        fire = fire_cascade.detectMultiScale(gray, 1.2, 5) # to provide frame resolution

        ## to highlight fire with square 
        for (x,y,w,h) in fire:
            cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            print("Fire alarm initiated")
            threading.Thread(target=play_alarm_sound_function).start()  # To call alarm thread

            if not runOnce:
                print("Mail send initiated")
                threading.Thread(target=send_mail_function).start() # To call alarm thread
                runOnce = True
            else:
                print("Mail is already sent once")

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Unable to read frame from camera.")
        break


# Release the video capture and close the windows
vid.release()
cv2.destroyAllWindows()