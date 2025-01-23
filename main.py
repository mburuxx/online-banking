import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_content

# App title with emoji
st.title("🕷️ Scrapezilla")

# Description
st.markdown(
    """
    Welcome to **Scrapezilla**, your go-to app for extracting and parsing website content!  
    Follow these steps:
    1. Enter the URL of the website you want to scrape.
    2. View and explore the extracted DOM content.
    3. Describe what you want to parse, and let Scrapezilla handle the rest.
    """
)

# Input for website URL
with st.container():
    url = st.text_input("🔗 Enter Website URL", placeholder="e.g., https://example.com")
    st.caption("Ensure the URL starts with `http` or `https`.")

if st.button("🚀 Scrape Site"):
    if url:
        with st.spinner("Scraping the website..."):
            results = scrape_website(url)
            body_content = extract_body_content(results)
            cleaned_content = clean_body_content(body_content)
            st.session_state.dom_content = cleaned_content

        st.success("Website content scraped successfully!")
        with st.expander("📝 View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
    else:
        st.error("Please enter a valid URL before scraping.")

# Parsing Section
if "dom_content" in st.session_state:
    st.markdown("### ✂️ Parse the Content")
    parse_description = st.text_area(
        "🔍 What information would you like to extract?",
        placeholder="Describe the information, e.g., extract all hyperlinks or headings, create tables etc ..."
    )

    if st.button("🧠 Parse Content"):
        if parse_description:
            with st.spinner("Parsing the content..."):
                dom_chunks = split_dom_content(st.session_state.dom_content)
                results = parse_content(dom_chunks, parse_description)

            st.success("Parsing completed!")
            st.markdown("### 🛠️ Parsed Results")
            st.write(results)
        else:
            st.error("Please provide a description of what you want to parse.")

# Footer with centered GitHub icon
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://github.com/mburuxx" target="_blank">
            <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png" alt="GitHub">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

