import streamlit as st
from PyPDF2 import PdfReader

st.title("PRINTING PRICE CALCULATOR ❤️")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type="pdf"
)

if uploaded_file is not None:

    pdf = PdfReader(uploaded_file)
    pages = len(pdf.pages)

    st.success(f"PDF uploaded successfully!")
    st.write(f"Number of pages: {pages}")

    paper = st.selectbox(
        "Choose paper type",
        ["80 gsm", "100 gsm"]
    )

    colour = st.selectbox(
        "Choose printing type",
        ["Colour", "Black & White"]
    )

    side = st.selectbox(
        "Choose printing side",
        ["One-sided", "Two-sided"]
    )

    if paper == "100 gsm":
        if colour == "Colour" and side == "One-sided":
            price = 0.80
        elif colour == "Colour" and side == "Two-sided":
            price = 0.90
        elif colour == "Black & White" and side == "One-sided":
            price = 0.40
        else:
            price = 0.50
    else:
        if colour == "Colour" and side == "One-sided":
            price = 0.50
        elif colour == "Colour" and side == "Two-sided":
            price = 0.60
        elif colour == "Black & White" and side == "One-sided":
            price = 0.30
        else:
            price = 0.40

    printing_price = pages * price
    st.write(f"Printing Price: RM {printing_price:.2f}")

    addon = st.selectbox(
        "Add-on",
        ["None", "Paper Clip", "Fastener"]
    )

    addon_price = 0

    if addon == "Paper Clip":
        addon_price = 0.10
    elif addon == "Fastener":
        addon_price = 0.30

    final_price = printing_price + addon_price
    st.subheader(f"Final Price: RM {final_price:.2f}")
