# OCR and Translation Automation with Google Cloud: Jap to English!

This repository provides a Python-based automation tool that extracts annotated text from PDF files using the Google Cloud Vision API, translates it using the Google Cloud Translation API, and saves the translated output to a file. The scripts automate the process of handling PDF documents, text extraction, and translation in an efficient workflow.

## Features
- **OCR Text Extraction from PDFs**: Uses Google Cloud Vision to detect and extract text from PDF files.
- **Translation**: Translates extracted text into the desired language (English by default) using Google Cloud Translation API (v3).
- **Automated Workflow**: Combines text annotation and translation into a single process, saving the output in a text file.
- **Cross-Language Support**: Easily configurable to translate text into multiple languages.

## File Structure

- `general_functions.py`: Utility functions used throughout the project.
- `annotate_pdf.py`: Script that uses Google Cloud Vision API to annotate and extract text from PDFs.
- `translate.py`: Script that translates the extracted text into the target language using Google Cloud Translation API.
- `annotate_to_translate.py`: Combines the OCR and translation processes into a single workflow.
- `requirements.txt`: Lists the required dependencies to run the project.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ocr-translation-automation.git
   cd ocr-translation-automation
2. **Install the required dependencies**: Make sure you have Python 3 installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

4. **Set up Google Cloud credentials**:

- Set up your Google Cloud project and enable the Vision API and Translation API.
- Download your service account key in JSON format and set the GOOGLE_APPLICATION_CREDENTIALS environment variable:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-key.json"

4. **Run the annotation and translation**: You can run the annotate_to_translate.py script to annotate and translate text in one go:

```bash
python annotate_to_translate.py
```
## Example Usage
The main process involves two parts:

1. **Extracting text from a PDF**: annotate_text.py uses Google Cloud Vision to extract text from a local PDF file.
2. **Translating the extracted text**: translate.py translates the extracted text using Google Cloud Translation API.

Here’s how to run the two processes separately:

- Annotate pdf:

```bash
python annotate_pdf.py "path-to-your-pdf"
```
- Translate Text:

```bash
python translate.py
```
Both processes can be combined by running:

```bash

python annotate_to_translate.py "path-to-your-pdf"
```
### Example Output
The translated text will be saved in a text file called translated_text_output.txt in the current working directory.
