import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit App
def main():
    st.title("📊 Data Visualization Tool")

    st.write("Upload a dataset (CSV) and explore it with interactive visualizations.")

    # File upload
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read CSV
        df = pd.read_csv(uploaded_file)
        st.subheader("🔹 Preview of Dataset")
        st.dataframe(df.head())

        # Select columns for visualization
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        all_columns = df.columns

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Scatter Plot", "Line Chart", "Bar Chart", "Histogram", "Box Plot"]
        )

        x_axis = st.selectbox("Select X-axis", all_columns)
        y_axis = st.selectbox("Select Y-axis", numeric_columns)

        # Generate Chart
        if st.button("Generate Chart"):
            if chart_type == "Scatter Plot":
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{chart_type}: {x_axis} vs {y_axis}")
            elif chart_type == "Line Chart":
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{chart_type}: {x_axis} vs {y_axis}")
            elif chart_type == "Bar Chart":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{chart_type}: {x_axis} vs {y_axis}")
            elif chart_type == "Histogram":
                fig = px.histogram(df, x=y_axis, title=f"{chart_type} of {y_axis}")
            elif chart_type == "Box Plot":
                fig = px.box(df, x=x_axis, y=y_axis, title=f"{chart_type}: {x_axis} vs {y_axis}")
            else:
                st.error("Unsupported chart type selected.")

            st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
