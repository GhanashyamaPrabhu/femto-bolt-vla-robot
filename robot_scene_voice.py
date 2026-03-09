import cv2
import pyttsx3
from transformers import BlipProcessor, BlipForConditionalGeneration

engine = pyttsx3.init()

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

cap = cv2.VideoCapture(0)

last_caption = ""

while True:

    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    inputs = processor(images=rgb, return_tensors="pt")

    out = model.generate(**inputs)

    caption = processor.decode(out[0], skip_special_tokens=True)

    if caption != last_caption:
        sentence = "I see " + caption
        print(sentence)

        engine.say(sentence)
        engine.runAndWait()

        last_caption = caption

    cv2.imshow("Robot Vision", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
