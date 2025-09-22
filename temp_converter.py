import streamlit as st

# Function to convert temperatures
def convert_temperature(value: float, unit: str) -> float:
    if unit == "Celsius":
        return (value * 9 / 5) + 32   # Celsius → Fahrenheit
    elif unit == "Fahrenheit":
        return (value - 32) * 5 / 9   # Fahrenheit → Celsius
    else:
        return None


# Streamlit App
def main():
    st.title("🌡️ Temperature Converter")

    # Input temperature value
    temp_value = st.number_input("Enter temperature value:", step=0.1)

    # Select unit
    unit = st.radio("Select the unit of measurement:", ["Celsius", "Fahrenheit"])

    # Convert button
    if st.button("Convert"):
        converted = convert_temperature(temp_value, unit)

        if converted is not None:
            if unit == "Celsius":
                st.success(f"{temp_value:.2f} °C = {converted:.2f} °F")
            elif unit == "Fahrenheit":
                st.success(f"{temp_value:.2f} °F = {converted:.2f} °C")
        else:
            st.error("Something went wrong. Please try again.")


if __name__ == "__main__":
    main()
