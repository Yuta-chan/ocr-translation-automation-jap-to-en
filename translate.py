from pdf_annotator import *
from google.cloud import translate_v3
import html

def sample_translate_text(text_to_translate):
    # Create a translation client
    client = translate_v3.TranslationServiceClient()

    # Prepare the request for translation
    request = translate_v3.TranslateTextRequest(
        contents=[text_to_translate],  # The extracted text from the PDF
        target_language_code="en",  # Target language (
        parent="projects/PROJECTID/locations/global"  # Use your project ID and location
    )

    # Make the translation request
    response = client.translate_text(request=request)

   # Get the translated text
    translated_text = response.translations[0].translated_text

    # Decode any HTML entities (if present)
    translated_text = html.unescape(translated_text)

    output_file_path = "translated_text_output.txt"  # Specify your desired file name
    with open(output_file_path, "w", encoding="utf-8") as text_file:
      text_file.write(translated_text)
    # Save the translated text to a file
    print(f"Translated text saved to {output_file_path}")
