import cv2
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load vision-language model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

device = "cpu"
model = model.to(device)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    inputs = processor(images=image, return_tensors="pt").to(device)

    out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)

    print("\nRobot perception:", caption)

        # -------- STEP 4 : SAFETY LOGIC --------
    warning_message = None

    if "person" in caption and "car" in caption:
        warning_message = "Warning. A person is near the vehicle."

    if "many" in caption or "several" in caption:
        warning_message = "Please be careful. There are many obstacles nearby."

    # -------- STEP 5 : ROBOT SPEECH --------
    if warning_message is not None and warning_message != last_caption:
        print("Robot says:", warning_message)

        engine.say(warning_message)
        engine.runAndWait()

        last_caption = warning_message

    cv2.imshow("Femto Bolt Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
