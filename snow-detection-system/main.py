from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("saved_model/keras_model.h5", compile=False)

# Load the labels
class_names = open("saved_model/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

def send_email(sender_email, receiver_email, subject, body, app_password):
    # SMTP server setup
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Email header and body setup (UTF-8 encoding)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Header(subject, 'utf-8')

    # Add email body (UTF-8 encoding)
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        # Connect to Gmail server and login
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS (secure connection)
        server.login(sender_email, app_password)

        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error occurred while sending email: {e}")

    finally:
        server.quit()

# Usage example
sender_email = "wwwe7701@gmail.com"
receiver_email = "24s620h0659@sonline20.sen.go.kr"
subject = "Snow Alert!"  # Subject when snow is detected
body = "Snow has been detected. Please take necessary actions."  # Email body when snow is detected
app_password = "oshi hrrt cnjd qvrh"  # Google app password

while True:
    # Grab the webcam's image
    ret, image = camera.read()

    # Resize the raw image to (224-height, 224-width) pixels
    image2 = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the model's input shape
    image2 = np.asarray(image2, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image2 = (image2 / 127.5) - 1

    # Predict the model
    prediction = model.predict(image2)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Check if the prediction is "snow"
    if index == 1: # Check if the predicted class contains "snow"
        print("Snow detected! Sending email...")
        send_email(sender_email, receiver_email, subject, body, app_password)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Listen to the keyboard for presses
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the escape key
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
