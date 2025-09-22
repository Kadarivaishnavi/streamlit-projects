import streamlit as st

# Function to reverse a string
def reverse_string(input_str: str) -> str:
    return input_str[::-1]

# Streamlit app
def main():
    st.title("🔄 String Reversal App")

    # Input from user
    user_input = st.text_input("Enter a string to reverse:")

    # Button to trigger reversal
    if st.button("Reverse"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a valid string.")
        else:
            reversed_str = reverse_string(user_input)
            st.success(f"Reversed String: **{reversed_str}**")

if __name__ == "__main__":
    main()
