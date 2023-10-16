# qdrant-setup

This Python project is designed to extract content from a folder and provide answers to user queries about the content. It utilizes OpenAI's GPT-3 for question-answering and integrates with a Qdrant-based vector store for efficient data retrieval.

## Prerequisites

Before getting started with this project, make sure you have the necessary dependencies installed and set up your environment:

### Python Libraries

- `dotenv`: For loading environment variables.
- `openai`: The OpenAI API for question-answering.
- `llama_index`: LlamaIndex is a data framework for LLM applications to ingest, structure, and access data.
- `qdrant_client`: A Python client for the Qdrant vector store.

You can install these libraries using `pip`:

```bash
pip install python-dotenv openai llama_index qdrant_client
```

### Environment Setup

To use the OpenAI API and Qdrant, you need to set the necessary API keys and endpoints in a `.env` file in the project directory:

```dotenv
# .env

OPENAI_API_KEY=your_openai_api_key_here
QDRANT_END_POINT=your_qdrant_endpoint_here
QDRANT_API_KEY=your_qdrant_api_key_here
```

## Usage

1. Add any text or pdf file in data folder.

2. The application will create documents and then parse them to chunks and index them.

3. It will store them in qdrant vector store

4. You can get the qdrant api key and hosted url after creating cluster on your account in qdrant cloud.

5. After that you can ask question about your data

## Note

This project provides a basic example of a question answering app that integrates with Qdrant for efficient data storage and retrieval. It can be further customized and extended.

If you encounter any issues or have questions, please feel free to reach out for assistance.
