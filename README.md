---
title: Information Retrieval System
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: streamlit 
app_file: app.py
---


# 📚 Multi-PDF Chatbot with Gemini (Information Retrieval System) 🧠✨

**Effortlessly extract answers and insights from your documents with the power of Google's Gemini Pro and LangChain!**

This Streamlit-powered RAG (Retrieval-Augmented Generation) application allows you to upload multiple PDF files and then ask questions directly about their content. Get precise, context-aware answers derived straight from your documents.


## ✨ Features

* **Multi-PDF Support:** Upload any number of PDF documents.
* **Intelligent Q&A:** Ask natural language questions about the uploaded content.
* **Gemini Pro Power:** Leverages Google's state-of-the-art Gemini Pro model for understanding and generating responses.
* **LangChain Integration:** Built with the robust LangChain framework for efficient document processing and conversational memory.
* **Streamlit UI:** A clean, intuitive, and interactive user interface.
* **Conversational Memory:** Remembers previous turns in your conversation for a seamless chat experience.


## 🚀 How It Works

1.  **PDF Upload & Text Extraction:** You upload your PDF files, and the system extracts all the textual content.
2.  **Text Chunking:** The extracted text is divided into smaller, manageable chunks.
3.  **Vector Store Creation:** These text chunks are converted into numerical representations (embeddings) using Google's `text-embedding-004` model and stored in a FAISS vector database.
4.  **Intelligent Retrieval:** When you ask a question, the system finds the most relevant text chunks from your PDFs using the vector store.
5.  **Gemini Generates Answer:** The relevant chunks, along with your question and conversation history, are fed to the Gemini Pro model (`gemini-2.5-flash`), which then generates a concise and accurate answer.


## ⚙️ Technologies Used

* **Python**
* **Streamlit:** For the interactive web application.
* **Google Generative AI:** Gemini Pro (`gemini-2.5-flash`) for LLM, `text-embedding-004` for embeddings.
* **LangChain:** For orchestration, RAG pipeline, and conversational memory.
* **PyPDF2:** For PDF text extraction.
* **FAISS:** For efficient similarity search in the vector store.
* **python-dotenv:** For secure management of environment variables.
