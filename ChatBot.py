from RAGConfig import DB_PATH
from RAGConfig import PROMPT_TEMPLATE
from RAGConfig import SIMILARITY_THRESHOLD
from RAGConfig import EnvironmentVariables

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate

EnvironmentVariables.setEnvironmentVariables()

def run_query(query: str, database: Chroma, model: ChatOpenAI):
    # Query the database and retrieve the top 3 most relevant results
    results = database.similarity_search_with_relevance_scores(query, k=5)
    results = [result for result in results if result[1] > SIMILARITY_THRESHOLD]
    if len(results) == 0:
        return "I'm sorry, I don't have enough information to give an accurate answer.", []
    
    # Extract context and sources from results
    context = "\n\n---\n\n".join([document.page_content for document, score in results])
    sources = [(document.metadata.get("source", None), score) for document, score in results]

    # Use context and query to create a prompt from a prompt template
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context, question=query)

    # Fetch response from LLM model
    response = model.invoke(prompt)

    return response.content, sources

def main():
    debug = False

    # Load database
    embedding_function = OpenAIEmbeddings()
    database = Chroma(persist_directory=DB_PATH, embedding_function=embedding_function)

    model = ChatOpenAI()

    while True:
        query = input(">> ")

        if query == ".quit":
            print("Good bye!")
            break

        if query == ".debug":
            debug = not debug
            print(f"Debug is: {debug}\n")
            continue

        response, sources = run_query(query, database, model)

        print(response)
        
        if debug:
            print(sources)

        print()

if __name__ == "__main__":
    main()