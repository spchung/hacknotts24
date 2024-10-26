import os
import easyocr
import cv2
import pytesseract
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

USER = "Melvin"
pytesseract.pytesseract.tesseract_cmd = os.path.join("C:\\", "Users", USER, "AppData", "Local", "Programs", "Tesseract-OCR", "tesseract.exe")
img_path = os.path.join("ocr", "images", "note1.jpg")

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


# Load the model and processor once
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed")

def read_text_trocr(image_path):
    """
    Detect text from an image using Hugging Face's TrOCR model and OpenCV.

    Parameters:
        image_path (str): Path to the image file.

    Returns:
        str: Detected text from the image.
    """
    # Load the image with OpenCV
    image = cv2.imread(image_path)

    # Check if the image loaded successfully
    if image is None:
        print("Error: Could not load image.")
        return ""

    # Convert the image from BGR to RGB format
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resize and normalize the image to match model requirements
    image_resized = cv2.resize(image_rgb, (384, 384))  # Use the resolution required by the model
    image_tensor = torch.tensor(image_resized).permute(2, 0, 1).unsqueeze(0) / 255.0  # Normalize to [0, 1]

    # Preprocess the image and perform OCR
    pixel_values = processor(images=image_tensor, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    print("TrOCR detected Text:")
    print(text)

    return text


trocr_text = read_text_trocr(img_path)