import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="LegalEase AI", page_icon="⚖️")
st.title("⚖️ LegalEase - AI Powered Legal Doc Generator")
st.write("Gemini AI moolama legal documents generate pannalam")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

# Document Type
doc_type = st.selectbox("Document Type Enna?", 
    ["Rental Agreement", "NDA", "Employment Contract", "Service Agreement", "Affidavit"])

# Inputs
party1 = st.text_input("Party 1 Name")
party2 = st.text_input("Party 2 Name")
details = st.text_area("Full Details Sollunga (e.g., Rent amount, duration, place)")

if st.button("Generate Document"):
    if not api_key:
        st.error("API Key podunga da!")
    elif not details:
        st.error("Details fill pannunga!")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            You are a legal expert. Create a professional {doc_type} in India format.
            Party 1: {party1}
            Party 2: {party2}
            Details: {details}
            Make it professional, with clauses, terms and conditions.
            Add disclaimer at end.
            """
            
            with st.spinner("Generating..."):
                response = model.generate_content(prompt)
                st.success("Document Ready!")
                st.markdown(response.text)
                
                # Download button
                st.download_button("Download as TXT", response.text, file_name=f"{doc_type}.txt")
                
        except Exception as e:
            st.error(f"Error: {e}")

st.sidebar.info("Get API Key from aistudio.google.com/app/apikey")
