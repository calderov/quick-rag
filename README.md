# quick-rag
A quick and simple RAG implementation

## Instructions
1. Place your OpenAI and LangChain API keys in `RAGConfig.py`
``` python
    __EnvironmentVariablesDict = {
        "LANGCHAIN_TRACING_V2": "true",
        "LANGCHAIN_API_KEY": "<PLACE YOUR LANGCHAIN API KEY HERE>",
        "OPENAI_API_KEY": "<PLACE YOUR OPENAI API KEY HERE>",
    }
```

2. Run `python CreateDataBase.py` to extract the info in `data/books` into a Chroma database, this will be the base of knowledge for our RAG. Be aware that you can add more markdown and text files to the books folder to expand the knowledge base.

3. Run `python ChatBot.py` and chat with the ChatBot interactively, remember that it is constrained to try to respond queries from the knowledge base. Try playing with it, asking questions in and out of the knowledge base to see how it responds.