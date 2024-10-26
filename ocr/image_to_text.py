import os
import easyocr
import cv2
import pytesseract
import torch
import warnings
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

USER = "Melvin"
pytesseract.pytesseract.tesseract_cmd = os.path.join("C:\\", "Users", USER, "AppData", "Local", "Programs", "Tesseract-OCR", "tesseract.exe")
img_path = os.path.join("ocr", "images", "sample_text2.jpg")

# warnings.filterwarnings("ignore", message="Some weights of.*were not initialized")

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")


def read_text_easyocr(image_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image_path)
    
    full_text = " ".join([text for (bbox, text, prob) in result])
    
    print("EasyOCR Detected Text:")
    print(full_text)

    return full_text


def read_text_tesseract(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Unable to load image.")
        return ""

    upscale_factor = 2
    new_width = int(image.shape[1] * upscale_factor)
    new_height = int(image.shape[0] * upscale_factor)
    image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)
    blurred_image = cv2.GaussianBlur(edges, (5, 5), 0)

    full_text = pytesseract.image_to_string(blurred_image)
    
    print("Tesseract Detected Text:")
    print(full_text)

    return full_text


def read_text_trocr(image_path, max_tokens=50):
    if not os.path.exists(image_path):
        print("Error: Image file does not exist.")
        return ""

    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values, max_new_tokens=max_tokens)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    print("TrOCR Detected Text:")
    print(generated_text)

    return generated_text


easyocr_text = read_text_easyocr(img_path)
print("")
tesseract_text = read_text_tesseract(img_path)
print("")
trocr_text = read_text_trocr(img_path)