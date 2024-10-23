from translate import *
from annotate_pdf import *

# Run the function to get the annotated text from the PDF
annotated_text = sample_batch_annotate_files()

# Translate the extracted annotated text
translated_text = sample_translate_text(annotated_text)
