import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape website
def scrape_website(url: str):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise error for bad status
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract titles, links, and paragraphs as examples
        titles = [t.get_text().strip() for t in soup.find_all("h1")]
        links = [a["href"] for a in soup.find_all("a", href=True)]
        paragraphs = [p.get_text().strip() for p in soup.find_all("p")]

        return titles, links, paragraphs

    except Exception as e:
        return [], [], [f"Error: {str(e)}"]


# Streamlit App
def main():
    st.title("🌐 Web Scraper using BeautifulSoup")

    url = st.text_input("Enter a website URL (e.g., https://example.com):")

    if st.button("Scrape Website"):
        if url.strip() == "":
            st.warning("⚠️ Please enter a valid URL.")
        else:
            with st.spinner("Scraping in progress..."):
                titles, links, paragraphs = scrape_website(url)

            st.subheader("🔹 Titles Found")
            if titles:
                for t in titles:
                    st.write(f"- {t}")
            else:
                st.write("No titles found.")

            st.subheader("🔹 Links Found")
            if links:
                for l in links[:20]:  # Show only first 20 links
                    st.write(f"- {l}")
            else:
                st.write("No links found.")

            st.subheader("🔹 Paragraphs Found")
            if paragraphs:
                for p in paragraphs[:5]:  # Show only first 5 paragraphs
                    st.write(f"- {p}")
            else:
                st.write("No paragraphs found.")


if __name__ == "__main__":
    main()



