import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
from twilio.rest import Client
import time

# -------------------------------
# WhatsApp Alert Setup
# -------------------------------
ACCOUNT_SID = "YOUR_TWILIO_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH"
FROM_WHATSAPP = "whatsapp:+14155238886"   # Twilio sandbox
TO_WHATSAPP = "whatsapp:+91YOURNUMBER"   # Your number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_alert(confidence):
    msg = f"⚠️ SNAKE DETECTED!\nConfidence: {confidence*100:.2f}%\nCheck immediately!"
    client.messages.create(
        body=msg,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )
    print("[ALERT SENT] WhatsApp message delivered.")

# -------------------------------
# TFLite Model Setup
# -------------------------------
MODEL_PATH = "snake_model.tflite"

interpreter = tflite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

IMG_SIZE = input_details[0]['shape'][1]   # e.g., 160

# -------------------------------
# Camera Setup
# -------------------------------
cap = cv2.VideoCapture(0)

last_alert_time = 0
COOLDOWN = 30   # seconds

print("🔍 Snake detection system started...\n")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error.")
        break

    # Preprocess
    resized = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = resized.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    # Inference
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])

    # For binary classification: [snake_prob, no_snake_prob]
    snake_conf = float(output[0][0])

    # Display
    cv2.putText(frame, f"Snake: {snake_conf*100:.1f}%", (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if snake_conf>0.6 else (0,0,255), 2)

    cv2.imshow("Snake Detector", frame)

    # Alert logic
    if snake_conf > 0.60:
        now = time.time()
        if now - last_alert_time > COOLDOWN:
            print(f"⚠️ Snake detected! Confidence: {snake_conf:.2f}")
            send_alert(snake_conf)
            last_alert_time = now

    # Quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
