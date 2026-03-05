import streamlit as st
from generator import generate_candidates
from predictor import predict
from ui import load_css

load_css()

st.markdown('<div class="title">AI Number Predictor</div>',unsafe_allow_html=True)

st.write("Masukkan riwayat angka (maks 10)")

history = st.text_area(
"Contoh:\n5831\n2749\n1103"
)

game = st.selectbox(
"Jenis permainan",
["2D","3D","4D","5D"]
)

length = int(game[0])

if st.button("Analisa & Generate"):

    results = history.split("\n")

    results = [x.strip() for x in results if x.strip()]

    candidates = generate_candidates(length)

    top = predict(results,candidates)

    st.subheader("20 Kandidat Terbaik")

    cols = st.columns(4)

    i=0

    for num,score in top:

        cols[i%4].markdown(
        f'<div class="card">{num}</div>',
        unsafe_allow_html=True
        )

        i+=1
