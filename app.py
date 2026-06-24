import streamlit as st
import requests

st.title("AI App Compiler")

prompt = st.text_area(
    "Enter your app idea"
)

if st.button("Generate"):

    try:

        res = requests.post(
            "http://127.0.0.1:8000/generate",
            json={
                "prompt": prompt
            }
        )

        st.write(
            "Status Code:",
            res.status_code
        )

        try:

            data = res.json()

            st.json(data)

        except Exception:

            st.error(
                "Backend did not return JSON"
            )

            st.text(res.text)

    except Exception as e:

        st.error(
            f"Connection Error: {e}"
        )