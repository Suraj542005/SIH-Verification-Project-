import cv2
import pytesseract
import re
import numpy as np
from pdf2image import convert_from_path


# Convert PDF to images
def pdf_to_images(pdf_path):
    """
    Converts a PDF file into a list of images.

    Args:
        pdf_path (str): Path to the PDF file.
    Returns:
        list: List of images.
    """
    images = convert_from_path(pdf_path)
    return images


# Apply OCR to extract text from an image
def ocr_image(image):
    """
    Extracts text from an image using OCR (Tesseract).

    Args:
        image (PIL.Image.Image): Image from which to extract text.
    Returns:
        str: Extracted text.
    """
    # Convert PIL image to a NumPy array (which OpenCV understands)
    image_np = np.array(image)
    # Convert the image from RGB to BGR format (which OpenCV uses)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(image_bgr)
    return text


# Extract text from all pages of the PDF
def extract_text_from_pdf_images(pdf_path):
    """
    Extracts text from each image page of a PDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: List of extracted texts, one per page.
    """
    images = pdf_to_images(pdf_path)
    extracted_texts = []

    for image in images:
        text = ocr_image(image)
        extracted_texts.append(text)

    return extracted_texts


# Extract specific data from text using regex patterns
def extract_specific_data(text, pattern):
    """
    Extracts specific data from text using a regex pattern.

    Args:
        text (str): The text from which to extract data.
        pattern (str): The regex pattern to match the specific data.

    Returns:
        str: The matched data or None if no match found.
    """
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return None


# Main function to process the PDF and extract specific data
def start_verify(pdf_path):
    """
    Main function to process the PDF, extract text, and then specific data.

    Args:
        pdf_path (str): Path to the PDF file.
    """
    extracted_texts = extract_text_from_pdf_images(pdf_path)

    # Define your patterns for data extraction
    aadhar_pattern = r'\b\d{4}\s\d{4}\s\d{4}\b'  # Matches Aadhar number format
    pan_pattern = r'\b[A-Z]{5}\d{4}[A-Z]\b'  # Matches PAN number format

    for i, text in enumerate(extracted_texts):
        print(f"Text from Page {i + 1}:\n{text}\n{'-' * 40}\n")

        # Extract specific data
        aadhar_number = extract_specific_data(text, aadhar_pattern)
        pan_number = extract_specific_data(text, pan_pattern)

        if aadhar_number:
            print(f"Found Aadhar Number: {aadhar_number}")
            return aadhar_number
        if pan_number:
            print(f"Found PAN Number: {pan_number}")
            return pan_number


# Entry point of the script
# if __name__ == "__main__":
#     # Replace this path with your actual PDF file path
#     pdf_path = "C:\\Users\\Suraj\\PycharmProjects\\SIH_Final\\Retrieved_folder\\suraj@gmail.com_retrieved_pdf.pdf"
#
#     # Call the main function with the PDF path
#     start_verify(pdf_path)


# def verify(pdf_file):
#     start_verify(pdf_file)
