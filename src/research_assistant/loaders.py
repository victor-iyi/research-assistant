from llama_index.core import Document
from streamlit.runtime.uploaded_file_manager import UploadedFile
from pypdf import PdfReader


def pdf_loader(uploaded_file: UploadedFile) -> list[Document]:
    """Load PDF file into list of Document objects

    Args:
        uploaded_file (UploadedFile): Uploaded file object

    Returns:
        list[Document] - List of parsed documents

    """

    reader = PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += f'\n\n{page.extract_text()}'

    docs = [Document(text=text)]
    return docs
