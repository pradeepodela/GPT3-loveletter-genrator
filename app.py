import streamlit as st
import openai
openai.api_key = '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'
def generate_email( userPrompt ="Write me a professionally sounding email", start="Dear"):
        """Returns a generated an email using GPT3 with a certain prompt and starting sentence"""

        response = openai.Completion.create(
        engine="davinci",
        prompt=userPrompt + "\n\n" + start,
        temperature=0.71,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.36,
        presence_penalty=0.75
        )
        return response.get("choices")[0]['text']
st.title("Love leter  Generator App")


with st.form(key="form"):
    prompt = 'write a convencing love letter to your crush '
    start = st.text_input("Begin writing the first few or several words of your love letter:")
    st.text("(Example: Baby i love you nothing in this world can describe how much i love you)")

    slider = st.slider("How many characters do you want your  Love Lette to be? ", min_value=64, max_value=750)
    st.text("(A typical  Love Lette is usually 100-500 characters)")

    submit_button = st.form_submit_button(label='Generate Love Letter')

    if submit_button:
        with st.spinner("Generating.."):
            output = generate_email(prompt, start)
        st.markdown("#  Output:")
        st.subheader(start + output)
