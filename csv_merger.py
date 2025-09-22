import streamlit as st
import pandas as pd
import os

# Function to merge CSV files
def merge_csv(files):
    dataframes = []
    for file in files:
        df = pd.read_csv(file)
        dataframes.append(df)
    merged_df = pd.concat(dataframes, ignore_index=True)
    return merged_df


# Streamlit App
def main():
    st.title("🤖 Task Automation: CSV File Merger")

    st.write("Upload multiple CSV files and automatically merge them into one dataset.")

    uploaded_files = st.file_uploader("Upload CSV files", type=["csv"], accept_multiple_files=True)

    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded successfully ✅")

        if st.button("Merge Files"):
            merged_df = merge_csv(uploaded_files)

            st.subheader("🔹 Merged Data Preview")
            st.dataframe(merged_df.head())

            # Save merged CSV
            output_file = "merged_output.csv"
            merged_df.to_csv(output_file, index=False)

            with open(output_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download Merged CSV",
                    data=f,
                    file_name="merged_output.csv",
                    mime="text/csv"
                )


if __name__ == "__main__":
    main()
