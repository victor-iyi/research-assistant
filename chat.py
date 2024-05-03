from dotenv import load_dotenv
import streamlit as st

from research_assistant.index import create_index

load_dotenv()


st.title('Research Assistant')
st.caption('A chatbot that helps you with your research')


with st.sidebar:
    pdf_file = st.file_uploader('Upload a PDF file')

    if pdf_file:
        # Create a vector index of the PDF file.
        st.session_state.index = create_index(pdf_file)
        # TODO(victor-iyi): Display the title of the paper & a summary.


def add_to_message_history(role: str, content: str) -> None:
    """Adds a message to the message history.

    Args:
        role (str): The role of the message sender.
        content (str): The content of the message.

    """
    st.session_state.messages.append({'role': role, 'content': content})


if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            'role': 'assistant',
            'content': 'Hello! How can I help you today?',
        },
    ]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if 'index' not in st.session_state.keys():
    st.info(f'Please upload a PDF file to get started.')
    st.stop()
else:
    st.session_state.chat_engine = st.session_state.index.as_chat_engine()

if prompt := st.chat_input():
    st.chat_message('user').write(prompt)
    add_to_message_history('user', prompt)
    with st.chat_message('assistant'):
        with st.spinner('Thinking...'):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            add_to_message_history('assistant', response.response)
