# Build streamlit UI
import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content
)
from parse import parse_content

st.title("Scrapezilla")

url = st.text_input("Enter a Website's URL")

if st.button("Scrape Site"):
    st.write("Scraping the website")

    results = scrape_website(url)
    body_content = extract_body_content(results)
    cleaned_content = clean_body_content(body_content)
   
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what information you'd like to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

        dom_chunks = split_dom_content(st.session_state.dom_content)