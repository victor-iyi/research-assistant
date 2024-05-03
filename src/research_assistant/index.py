from streamlit.runtime.uploaded_file_manager import UploadedFile

from pypdf import PdfReader

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.embeddings import resolve_embed_model


def create_index(uploaded_file: UploadedFile) -> VectorStoreIndex:
    """Loads a PDF file and creates an index of its content.

    Args:
        file (UploadedFile): The PDF file to load.

    Returns:
        VectorStoreIndex: An index of the PDF file content.

    """
    reader = PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += f'\n\n{page.extract_text()}'

    docs = [Document(text=text)]
    node_parser = SentenceSplitter()

    base_nodes = node_parser.get_nodes_from_documents(docs)
    # Set node ids to be a constant
    for idx, node in enumerate(base_nodes):
        node.id_ = f'node-{idx}'

    embed_model = resolve_embed_model('local:BAAI/bge-small-en')

    index = VectorStoreIndex(
        nodes=base_nodes,
        embed_model=embed_model,
        show_progress=True,
    )
    return index
