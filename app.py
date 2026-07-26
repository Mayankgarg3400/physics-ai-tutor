import streamlit as st

from graph import rag

st.set_page_config(
    page_title="Physics AI Tutor",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Physics AI Tutor")
st.markdown("### Ask Questions from your Physics Book")

# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant" and "docs" in message:

            st.markdown("### 📖 Sources Used")

            for doc in message["docs"]:

                page = doc.metadata["page"] + 1

                with st.expander(f"📄 Page {page}"):

                    preview = doc.page_content.strip()

                    if len(preview) > 500:
                        preview = preview[:500] + "..."

                    st.write(preview)

# -----------------------------
# User Input
# -----------------------------

question = st.chat_input("Ask your Physics question...")

if question:

    # Show user message
    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Generate Answer
    with st.chat_message("assistant"):

        with st.spinner("🔍 Searching Physics Book..."):

            result = rag.invoke(question)

            answer = result["answer"]

            docs = result["context"]

        st.markdown(answer)

        st.markdown("---")
        st.markdown("### 📖 Sources Used")

        for doc in docs:

            page = doc.metadata["page"] + 1

            with st.expander(f"📄 Page {page}"):

                preview = doc.page_content.strip()

                if len(preview) > 500:
                    preview = preview[:500] + "..."

                st.write(preview)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "docs": docs
        }
    )