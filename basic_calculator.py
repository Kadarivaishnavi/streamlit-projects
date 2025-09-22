import streamlit as st

# Function to perform calculation
def calculate(num1: float, num2: float, operator: str):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero!"
        elif operator == "%":
            if num2 != 0:
                return num1 % num2
            else:
                return "Error: Modulus by zero!"
        else:
            return "Invalid operator!"
    except Exception as e:
        return f"Error: {e}"

# Streamlit app
def main():
    st.title("🧮 Basic Calculator")

    # Inputs
    num1 = st.number_input("Enter first number:", step=1.0, format="%.2f")
    num2 = st.number_input("Enter second number:", step=1.0, format="%.2f")

    operator = st.selectbox("Choose an operator:", ["+", "-", "*", "/", "%"])

    # Calculate button
    if st.button("Calculate"):
        result = calculate(num1, num2, operator)
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
