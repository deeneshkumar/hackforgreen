import pathway as pw

def build_index(docs_dir):
    """
    Builds a real-time vector index from documents in a directory.
    """
    sources = pw.io.fs.read(docs_dir, format="binary", mode="streaming", with_metadata=True)
    
    # Simple text splitting and embedding (replace with actual model if key available)
    # For this demo, we use a simple keyword/context match if no embedding model key is present,
    # or use Pathway's LLM connectors.
    
    # NOTE: Since we need an embedding model, we assume OpenAI or similar is configured.
    # If not, this part will be mocked for the skeleton, but the structure remains.
    
    documents = sources.select(text=pw.io.fs.read(docs_dir, format="binary", mode="streaming", with_metadata=True))
    
    return documents # Placeholder: In a full app, this returns the index.

def query_rag(query, index, context_data):
    """
    Queries the RAG system with a specific question and current context context.
    """
    # In a real Pathway app, this would use `pw.ml.answer` or similar.
    # For the MVP skeleton, we return a constructed prompt for the LLM.
    
    prompt = f"""
    Context Data: {context_data}
    User Query: {query}
    
    Based on the documents and the live data, explain the situation.
    """
    return prompt
