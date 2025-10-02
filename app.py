import os
os.environ["HOME"] = "/tmp"


import streamlit as st
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain


def user_input(user_question):
    # This is the line that was failing if st.session_state.conversation was None
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']


def main():
    st.set_page_config("Information Retrieval")
    st.header("Information Retrieval System💁")

    # Initialize session state variables if they don't exist
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None

    user_question = st.text_input("Ask a Question from the PDF Files")

    # ----------------------------------------------------
    # 💥 THE FIX: Check if the conversation chain is ready before calling user_input
    if user_question:
        if st.session_state.conversation is not None:
            user_input(user_question)
        else:
            # Inform the user what to do next
            st.warning("Please upload PDF files and click 'Submit & Process' first to begin the conversation.")
    # ----------------------------------------------------

    # Display chat history using modern Streamlit chat elements (Optional but recommended)
    if st.session_state.chatHistory:
        for message in st.session_state.chatHistory:
            # Check the message type (HumanMessage or AIMessage)
            if message.__class__.__name__ == 'HumanMessage':
                with st.chat_message("user"):
                    st.write(message.content)
            else: # Likely AIMessage
                with st.chat_message("assistant"):
                    st.write(message.content)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs: # Ensure files are uploaded before processing
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    vector_store = get_vector_store(text_chunks)
                    # This is where the conversation object is initialized to a callable chain
                    st.session_state.conversation = get_conversational_chain(vector_store)
                    st.success("Processing Complete. You can now ask questions!")
            else:
                st.error("Please upload at least one PDF file.")


if __name__ == "__main__":
    main()