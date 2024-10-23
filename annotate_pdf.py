from google.cloud import vision_v1
import io

def sample_batch_annotate_files(pdf_file):
    # Create a client
    client = vision_v1.ImageAnnotatorClient()

    # Specify the file path (local PDF file)
    file_name = pdf_file  # Replace with your actual PDF file name

    # Read the PDF file as bytes
    with io.open(file_name, 'rb') as pdf_file:
        content = pdf_file.read()

    # Configure the input with the PDF content
    input_config = vision_v1.InputConfig(
        mime_type='application/pdf',  # Specify the file type as PDF
        content=content
    )

    # Define the features you want to extract, such as document text detection
    features = [vision_v1.Feature(type_=vision_v1.Feature.Type.DOCUMENT_TEXT_DETECTION)]

    # Configure the request
    requests = [vision_v1.AnnotateFileRequest(
        input_config=input_config,
        features=features
    )]

    # Make the synchronous request
    response = client.batch_annotate_files(requests=requests)

    # Handle and store the response
    extracted_text = ""
    for file_response in response.responses:
        if file_response.error.message:
            print(f"Error: {file_response.error.message}")
        else:
           for annotation in file_response.responses:
                extracted_text += annotation.full_text_annotation.text + "\n"

    # Now the `extracted_text` variable contains the full text from the PDF annotations
    # You can either return it or store it for later use in translation
    return extracted_text
