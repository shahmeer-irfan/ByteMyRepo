
 <body>
 
 <h1>ByteMyRepo</h1>

 <p>Ask intelligent, context-aware questions about any public <strong>GitHub codebase</strong> using <strong>AI-powered retrieval-augmented generation (RAG)</strong>.</p>

 <span class="badge"><img src="https://img.shields.io/badge/Built%20With-Streamlit-orange?style=flat-square" alt="Built With Streamlit"></span>
 <span class="badge"><img src="https://img.shields.io/badge/Powered%20By-LangChain-blueviolet?style=flat-square" alt="Powered By LangChain"></span>
    <span class="badge"><img src="https://img.shields.io/badge/Open%20Source-Yes-brightgreen?style=flat-square" alt="Open Source"></span>
    <span class="badge"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></span>

 <h2>What is ByteMyRepo?</h2>

 <p>ByteMyRepo lets you:</p>
    <ul>
        <li>Paste any <strong>public GitHub repo URL</strong></li>
        <li>Automatically <strong>clone the codebase</strong>, <strong>split it into chunks</strong>, and <strong>embed</strong> it into Pinecone</li>
        <li>Ask <strong>natural language questions</strong> about the codebase</li>
        <li>Get <strong>accurate answers with relevant code snippets</strong> via a large language model (LLM)</li>
    </ul>
    <p>It's your <strong>AI teammate</strong> who reads the code and explains it!</p>

 <h2>Features</h2>

<ul>
     <li>GitHub repo cloning</li>
        <li>Intelligent code chunking (Python/JavaScript)</li>
        <li>Vector embeddings using HuggingFace</li>
        <li>Pinecone-powered retrieval</li>
        <li>Kimi-72B (OpenRouter) for LLM responses</li>
        <li>Output cleanup to remove internal reasoning</li>
        <li>Source code context viewer</li>
        <li>Secure user-supplied API keys via sidebar</li>
        <li>🖥Beautiful, responsive UI with Streamlit</li>
        <li>Open to community contributions</li>
    </ul>

<h2>🏗️ Tech Stack</h2>

<table>
        <tr>
            <th>Layer</th>
            <th>Technology</th>
        </tr>
        <tr>
            <td>Frontend</td>
            <td>Streamlit</td>
        </tr>
        <tr>
            <td>Code Parsing</td>
            <td>Python AST, LangChain splitters</td>
        </tr>
        <tr>
            <td>Embeddings</td>
            <td><code>sentence-transformers/all-mpnet-base-v2</code></td>
        </tr>
        <tr>
            <td>Vector DB</td>
            <td>Pinecone</td>
        </tr>
        <tr>
            <td>LLM</td>
            <td>OpenRouter (Kimi 72B)</td>
        </tr>
        <tr>
            <td>Orchestration</td>
            <td>LangChain</td>
        </tr>
        <tr>
            <td>Deployment Ready</td>
            <td>✅</td>
        </tr>
    </table>

  <h2>📁 Folder Structure</h2>
    <pre>
    ByteMyRepo/
    ├── app.py                # Main Streamlit UI app
    ├── .env                  # Environment variables (not used in deployment, for local testing)
    ├── requirements.txt      # Dependencies
    ├── src/                  # Modular logic
    │   ├── __init__.py
    │   ├── clone.py          # GitHub repo cloning logic
    │   ├── chunk.py          # Code chunking logic (Python/JS)
    │   ├── vector.py         # Pinecone vector store logic
    │   └── llm.py            # OpenRouter LLM wrapper
    </pre>

 <h2>📦 Installation</h2>

 <ol>
        <li><strong>Clone this repository:</strong>
            <pre>
          git clone https://github.com/yourusername/ByteMyRepo.git
          cd ByteMyRepo
            </pre>
        </li>
        <li>Create a virtual environment (optional):
            <pre>
       python -m venv venv
     source venv/bin/activate  # Windows: venv\Scripts\activate
            </pre>
        </li>
        <li>Install dependencies:
            <pre>
     pip install -r requirements.txt
            </pre>
        </li>
        <li>Run App:
            <pre>
     streamlit run app.py
            </pre>
        </li>
    </ol>

 <h3>🔐 API Keys (required to run)</h3>
    <table>
        <tr>
            <th>API</th>
            <th>How to Get It</th>
        </tr>
        <tr>
            <td>Pinecone</td>
            <td><a href="https://app.pinecone.io/">https://app.pinecone.io/</a></td>
        </tr>
        <tr>
            <td>OpenRouter</td>
            <td><a href="https://openrouter.ai/">https://openrouter.ai/</a></td>
        </tr>
    </table>

  <h2>How It Works</h2>
    <ol>
        <li>User inputs a public GitHub repo URL</li>
        <li>The repo is cloned locally using gitpython</li>
        <li>Files are walked, filtered, and split using ast or LangChain's text splitter</li>
        <li>Chunks are embedded using HuggingFaceEmbeddings</li>
        <li>Embeddings are stored in Pinecone under a unique namespace</li>
        <li>When user enters a query, similar chunks are retrieved</li>
        <li>Retrieved code is passed with the question to the Kimi 72B LLM</li>
        <li>The AI returns a cleaned and code-supported answer</li>
    </ol>

 <h2>Contribution</h2>
    <p>We welcome contributions from everyone! 🌍</p>

  <h3>How to Contribute:</h3>
    <ol>
        <li>Fork this repo</li>
        <li>Create a branch: <code>git checkout -b new-feature</code></li>
        <li>Commit changes: <code>git commit -m "Add new feature"</code></li>
        <li>Push branch: <code>git push origin new-feature</code></li>
        <li>Open a Pull Request</li>
    </ol>

 <h3>Ideas to Contribute:</h3>
    <ul>
        <li>Add TypeScript/Java support</li>
        <li>Add multiple LLM model selection (OpenAI, Anthropic, etc.)</li>
        <li>Add authentication layer</li>
        <li>Improve UI responsiveness</li>
        <li>Add markdown export</li>
    </ul>

 <h2>📜 License</h2>
    <p>This project is licensed under the MIT License. See LICENSE for details.</p>

   <h2>Contact</h2>
    <p>Email: <a href="mailto:shameerirfan124@gmail.com">shameerirfan124@gmail.com</a></p>

   </body>
