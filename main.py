import streamlit as st
from src.clone import clone_repo
from src.chunk import get_all_chunks
from src.llm import load_llm
from src.vectorstore import create_vectorstore
from src.utils import clean_output

st.set_page_config(page_title="ByteMyRepo", layout="centered")

st.markdown("""
<h1 style='text-align: center; color: #4B8BBE;'>ByteMyRepo</h1>
<p style='text-align: center; color: gray;'>Ask intelligent, code-aware questions about any public GitHub repo using AI.</p>
<hr style='margin-top:20px; margin-bottom:30px'>
""", unsafe_allow_html=True)

# Input UI
st.subheader("📥Provide your GitHub Repository")
repo_url = st.text_input("🔗 GitHub Repo URL", placeholder="https://github.com/shahmeer-irfan/langchain-handbook")

if repo_url and st.button("Clone & Index Repository"):
    with st.spinner("Cloning and processing..."):
        try:
            repo_path = clone_repo(repo_url)
            documents = get_all_chunks(repo_path)
            vectorstore = create_vectorstore(documents, repo_url)
            st.session_state.vectorstore = vectorstore
            st.session_state.repo_url = repo_url
            st.success("Repo indexed!")
        except Exception as e:
            st.error(f"❌ {e}")

# Question-answering UI
if "vectorstore" in st.session_state:
    st.subheader("💬 Ask a question about the codebase")
    question = st.text_input("Your question", placeholder="e.g. How is routing handled?")
    if st.button("Generate Answer") and question.strip():
        with st.spinner("Thinking..."):
            retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
            docs = retriever.invoke(question)
            context = "\n\n".join([doc.page_content for doc in docs])
            prompt = f"""You are a senior software engineer with 10+ years of experience.
                    Always use code snippets as examples from the provided codebase.
                    Use the context below to answer the user's question. If the answer is not present in the context, reply: 'I don't know'.

<CODESNIPPETS>
{context}
</CODESNIPPETS>

Question: {question}
"""
            try:
                llm = load_llm()
                response = llm.invoke(prompt)
                st.markdown("### Answer")
                st.success(clean_output(response.content))
                with st.expander("📄 Source Context Used"):
                    for i, doc in enumerate(docs):
                        st.markdown(f"**Snippet {i+1} — `{doc.metadata.get('source', 'unknown')}`**")
                        st.code(doc.page_content.strip(), language="python")
            except Exception as e:
                st.error(f"❌ LLM Error: {e}")
