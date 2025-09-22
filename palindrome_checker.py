import streamlit as st

# Function to check palindrome
def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()  # remove spaces & ignore case
    return cleaned == cleaned[::-1]

# Streamlit app
def main():
    st.title("🔄 Palindrome Checker")

    # User input
    user_input = st.text_input("Enter a word or phrase:")

    if st.button("Check"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter some text.")
        else:
            if is_palindrome(user_input):
                st.success(f"✅ '{user_input}' is a Palindrome!")
            else:
                st.error(f"❌ '{user_input}' is NOT a Palindrome.")

if __name__ == "__main__":
    main()

