import os

from pypdf import PdfReader
from docx import Document


def load_txt(file_path):
    """
    Load TXT document
    """

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return [
        {
            "text": text,
            "metadata": {
                "source": os.path.basename(file_path),
                "page": 1
            }
        }
    ]


def load_pdf(file_path):
    """
    Load PDF document page by page
    """

    documents = []

    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text and text.strip():

            documents.append(
                {
                    "text": text,
                    "metadata": {
                        "source": os.path.basename(file_path),
                        "page": page_number
                    }
                }
            )

    return documents


def load_docx(file_path):
    """
    Load DOCX document
    """

    doc = Document(file_path)

    text = "\n".join(
        [paragraph.text for paragraph in doc.paragraphs]
    )

    return [
        {
            "text": text,
            "metadata": {
                "source": os.path.basename(file_path),
                "page": 1
            }
        }
    ]


def load_documents(data_folder):
    """
    Load all supported documents
    """

    all_documents = []

    for filename in os.listdir(data_folder):

        file_path = os.path.join(
            data_folder,
            filename
        )

        if filename.endswith(".txt"):

            all_documents.extend(
                load_txt(file_path)
            )

        elif filename.endswith(".pdf"):

            all_documents.extend(
                load_pdf(file_path)
            )

        elif filename.endswith(".docx"):

            all_documents.extend(
                load_docx(file_path)
            )

    return all_documents