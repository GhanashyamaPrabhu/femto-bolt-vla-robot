import cv2
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

cap = cv2.VideoCapture(0)

last_caption = ""

while True:

    ret, frame = cap.read()
    if not ret:
        break

    # Convert image format
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    inputs = processor(images=rgb, return_tensors="pt")

    out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)

    if caption != last_caption:
        print("Scene:", caption)
        last_caption = caption

    cv2.imshow("Scene Understanding", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
