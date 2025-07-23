# src/chunk.py

import os
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

SUPPORTED_EXTENSIONS = {'.py', '.js', '.jsx', '.tsx'}
IGNORED_DIRS = {'node_modules', 'venv', 'env', 'dist', 'build', '.git', '__pycache__', '.next', '.vscode', 'vendor'}

def chunk_python_code(file_path: str, source_code: str):
    import ast
    documents = []
    fallback_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    try:
        tree = ast.parse(source_code)
        found_chunks = False
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                start_line = node.lineno - 1
                end_line = getattr(node, 'end_lineno', start_line + 1)
                lines = source_code.splitlines()[start_line:end_line]
                content = "\n".join(lines)
                documents.append(Document(
                    page_content=content,
                    metadata={"source": file_path, "type": type(node).__name__, "name": getattr(node, 'name', 'unknown')}
                ))
                found_chunks = True
        if not found_chunks:
            documents = fallback_splitter.create_documents([source_code])
            for doc in documents:
                doc.metadata["source"] = file_path
    except:
        documents = fallback_splitter.create_documents([source_code])
        for doc in documents:
            doc.metadata["source"] = file_path
    return documents

def chunk_js_code(file_path: str, source_code: str):
    js_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.JS,
        chunk_size=1000,
        chunk_overlap=100
    )
    return js_splitter.create_documents([source_code], metadata=[{"source": file_path}])

def get_all_chunks(repo_path: str):
    all_documents = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext not in SUPPORTED_EXTENSIONS:
                continue
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if ext == '.py':
                docs = chunk_python_code(file_path, content)
            else:
                docs = chunk_js_code(file_path, content)
            all_documents.extend(docs)
    return all_documents
