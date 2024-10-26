import os
import easyocr
import cv2
import pytesseract

USER = "Melvin"
pytesseract.pytesseract.tesseract_cmd = os.path.join("C:\\", "Users", USER, "AppData", "Local", "Programs", "Tesseract-OCR", "tesseract.exe")
img_path = os.path.join("ocr", "images", "note3.jpg")

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

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    full_text = pytesseract.image_to_string(gray_image)
    
    print("Tesseract Detected Text:")
    print(full_text)
    return full_text


easyocr_text = read_text_easyocr(img_path)
tesseract_text = read_text_tesseract(img_path)
