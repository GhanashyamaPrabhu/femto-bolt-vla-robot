import cv2
import torch
from PIL import Image
from transformers import LlavaProcessor, LlavaForConditionalGeneration

model_id = "llava-hf/llava-1.5-7b-hf"

processor = LlavaProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(model_id)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    if not ret:
        break

    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    prompt = "Describe what is happening in the environment."

    inputs = processor(prompt, image, return_tensors="pt")

    output = model.generate(**inputs, max_new_tokens=50)

    text = processor.decode(output[0], skip_special_tokens=True)

    print(text)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
