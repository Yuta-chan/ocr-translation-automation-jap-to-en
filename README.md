# OCR and Translation Automation

This repository provides a Python-based automation tool that extracts annotated text from PDF files using the Google Cloud Vision API, translates it using the Google Cloud Translation API, and saves the translated output to a file. The scripts automate the process of handling PDF documents, text extraction, and translation in an efficient workflow.

## Features
- **OCR Text Extraction from PDFs**: Uses Google Cloud Vision to detect and extract text from PDF files.
- **Translation**: Translates extracted text into the desired language (English by default) using Google Cloud Translation API (v3).
- **Automated Workflow**: Combines text annotation and translation into a single process, saving the output in a text file.
- **Cross-Language Support**: Easily configurable to translate text into multiple languages.

## File Structure

- `general_functions.py`: Utility functions used throughout the project.
- `annotate_text.py`: Script that uses Google Cloud Vision API to annotate and extract text from PDFs.
- `translate.py`: Script that translates the extracted text into the target language using Google Cloud Translation API.
- `annotate_to_translate.py`: Combines the OCR and translation processes into a single workflow.
- `requirements.txt`: Lists the required dependencies to run the project.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ocr-translation-automation.git
   cd ocr-translation-automation
