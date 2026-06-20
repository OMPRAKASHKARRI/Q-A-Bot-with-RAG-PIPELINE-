import streamlit as st

from query import retrieve_context
from generator import generate_answer


st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)

# ======================
# Sidebar
# ======================

with st.sidebar:

    st.title("⚙️ System Info")

    st.metric(
        "Documents Loaded",
        "5"
    )

    st.metric(
        "Vector DB",
        "ChromaDB"
    )

    st.info(
        """
**Embedding Model**
all-MiniLM-L6-v2

**LLM**
Llama 3.3 70B (Groq)

**Retrieval**
Top-K Similarity Search
"""
    )

    st.markdown("---")

    st.success(
        "Knowledge Base Loaded Successfully ✅"
    )

# ======================
# Main Header
# ======================

st.title("📚 AI Knowledge Assistant")

st.caption(
    "A Retrieval-Augmented Generation (RAG) system that answers questions from your custom document knowledge base."
)

st.markdown("---")

# ======================
# Metrics Row
# ======================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Documents",
        "5"
    )

with col2:
    st.metric(
        "Chunks",
        "33"
    )

with col3:
    st.metric(
        "LLM",
        "Llama 3.3"
    )

st.markdown("---")

# ======================
# Sample Questions
# ======================

st.info(
    """
### 💡 Sample Questions

• What is Artificial Intelligence?

• What is supervised learning?

• What are the benefits of cloud computing?

• What are common cybersecurity threats?

• How is Data Science used in healthcare?

• Who won FIFA World Cup 2022? 
"""
)

st.markdown("---")

# ======================
# Question Input
# ======================

question = st.text_input(
    "💬 Enter your question:"
)

if st.button("🚀 Ask Question"):

    if question.strip():

        with st.spinner(
            "Searching documents and generating answer..."
        ):

            contexts, citations = retrieve_context(
                question
            )

            answer = generate_answer(
                question,
                contexts,
                citations
            )

        st.markdown("---")

        st.subheader("🤖 Answer")

        with st.container(border=True):
            st.markdown(answer)

        st.markdown("---")

        st.subheader("📄 Retrieved Chunks")

        for context in contexts:

            with st.expander(
                f"📄 {context['source']} | Page {context['page']}"
            ):

                st.markdown(
                    f"**Source:** {context['source']}"
                )

                st.markdown(
                    f"**Page:** {context['page']}"
                )

                st.markdown("---")

                st.write(
                    context["text"]
                )

st.markdown("---")

st.caption(
    "Built using Streamlit • ChromaDB • SentenceTransformers • Groq Llama 3.3"
)