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