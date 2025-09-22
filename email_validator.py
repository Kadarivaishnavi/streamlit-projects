import streamlit as st
import re

# Function to validate email
def is_valid_email(email: str) -> bool:
    # Basic pattern: something@something.domain
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Streamlit app
def main():
    st.title("📧 Email Validator")

    # Input field
    email_input = st.text_input("Enter an email address:")

    if st.button("Validate"):
        if email_input.strip() == "":
            st.warning("⚠️ Please enter an email address.")
        else:
            if is_valid_email(email_input):
                st.success(f"✅ '{email_input}' is a valid email address!")
            else:
                st.error(f"❌ '{email_input}' is NOT a valid email address.")

if __name__ == "__main__":
    main()
