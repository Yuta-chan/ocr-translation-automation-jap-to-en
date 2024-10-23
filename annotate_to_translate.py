from translate import *
from annotate_pdf import *

# Set the path to your service account credentials JSON
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/service-account-file.json"

def give_pdf_file():
    try:
        pdf_file = str(input("Which PDF file would you like to extract text from? "))
    except ValueError:
        print("Please enter a valid PDF file name.")
    else:
        print(f"You have selected {pdf_file}")
    return pdf_file
# Get the PDF file name from the user
pdf_file = give_pdf_file()

# Run the function to get the annotated text from the PDF
annotated_text = sample_batch_annotate_files(pdf_file)

# Translate the extracted annotated text
translated_text = sample_translate_text(annotated_text)
