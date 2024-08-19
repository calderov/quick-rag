import os

# Environment variables and API keys
class EnvironmentVariables:
    __EnvironmentVariablesDict = {
        "LANGCHAIN_TRACING_V2": "true",
        "LANGCHAIN_API_KEY": "<PLACE YOUR LANGCHAIN API KEY HERE>",
        "OPENAI_API_KEY": "<PLACE YOUR OPENAI API KEY HERE>",
    }

    LANGCHAIN_TRACING_V2 = __EnvironmentVariablesDict["LANGCHAIN_TRACING_V2"]
    LANGCHAIN_API_KEY = __EnvironmentVariablesDict["LANGCHAIN_API_KEY"]
    OPENAI_API_KEY = __EnvironmentVariablesDict["OPENAI_API_KEY"]

    @staticmethod
    def keys():
        return [attr for attr in dir(EnvironmentVariables) if not callable(getattr(EnvironmentVariables, attr)) and not attr.startswith("__") and attr != "keys" and attr != "setEnvironmentVariables"]
    
    @staticmethod
    def setEnvironmentVariables():
        for key in EnvironmentVariables.__EnvironmentVariablesDict:
            os.environ[key] = EnvironmentVariables.__EnvironmentVariablesDict[key]

# Database location            
DB_PATH = "chroma"

# Document sources location
DOCUMENTS_PATH = "data/books"

# Similarity threshold used by similarity search, 0 is dissimilar, 1 is most similar.
SIMILARITY_THRESHOLD = 0.72

# Prompt template to set context, query and potentially some additional limitations
PROMPT_TEMPLATE = """
Given the following context answer the query at the very end:

{context}

---

{question}
"""