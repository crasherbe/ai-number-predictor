import streamlit as st

def load_css():

    st.markdown(
    """
    <style>

    .main {
        background-color:#0f172a;
        color:white;
    }

    .title{
        font-size:42px;
        text-align:center;
        font-weight:bold;
        color:#22d3ee;
    }

    .card{
        background:#1e293b;
        padding:20px;
        border-radius:12px;
        text-align:center;
        font-size:24px;
        margin:6px;
    }

    </style>
    """,
    unsafe_allow_html=True
    )
