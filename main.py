# Build streamlit UI
import streamlit as st

st.title("Scrapezilla")

url = st.text_input("Enter a Website's URL")

if st.button("Scrape Site"):
    st.write("Scraping the website....")