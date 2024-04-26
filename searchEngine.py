import pandas as pd
import streamlit as st

# Load data
import pandas as pd

file_path = r"C:\Users\ADMIN\Downloads\Search-Engine_final.csv"

try:
    df = pd.read_csv(file_path)
    # Further processing of the dataframe
except pd.errors.EmptyDataError:
    print("The file is empty or contains no columns.")
except FileNotFoundError:
    print("The file does not exist at the specified path.")
except Exception as e:
    print("An error occurred:", e)

# Define Streamlit app
def main():
    st.set_page_config(page_title="Movie Subtitle - Search Engine", layout="wide")
    
    # Title box
    st.markdown(
        """
        <div style='background-color: #2ecc71; padding: 30px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);'>
            <h1 style='color: black; text-align: center;'>Movie Subtitle - Search Engine</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Search form
    search_text = st.text_input("Enter Movie or Series Name")

    # Search functionality
    if st.button("Search"):
        if search_text:
            results = df[df['webseries'].str.contains(search_text, case=False, na=False)]['webseries'].tolist()

            # Display search results
            if results:
                st.markdown(f"## Search Results for '{search_text}'")
                for result in results:
                    st.write(result)
                    st.write(f"[Download from OpenSubtitles (View Subtitle Page)](https://www.opensubtitles.org/en/subtitles/{result})", unsafe_allow_html=True)
            else:
                st.warning(f"No results found for '{search_text}'")
        else:
            st.warning("Please enter a search query.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
