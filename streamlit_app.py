import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


def get_main_prompt(prompt, event, target_consumer):
    prompt = (
        f"Your role is an {target_consumer}.\n"
        f"Your write very short commercials for product_name."
        f" Use the idea of brand_name\"\n\n"
        
        f"For the Event '{event}' You need to  follow instruction" 
        f" delimited by triple backticks ```{prompt} in style of {target_consumer}``` in the following form:\n"
         "1. Product description\n"
        f"2. Slogan. Dont use brand_name in slogan! Never put dot '.' in the end of slogan!\n"
        "3. Background Image description. Like: \'Your background will be an image of a weathered, rustic American flag. This image should fill the entire canvas. The flag should be rich in color but slightly faded, hinting at both vibrancy and tradition.\'"

        f"""\n\nAs answer give JSON:
        {{
            "1": <Product description>,
            "2": <Slogan>
            "3": <Background Image description>
            "4": <event>
        }}"""
    )
    return prompt

def generate_assets(main_prompt):
    a = "Introducing SNICKERS, the game changer of the candy world. Unwrap the thrill of rich, decadent milk chocolate perfectly layered with smooth caramel and delicious nougat, all cradling a savory mix of satisfying roasted peanuts. A powerhouse of energy and flavor, it's the perfect companion for those Super Bowl nail-biter moments. Give your taste buds the rush of a touchdown with every bite of SNICKERS."
    b = "SNICKERS, tackling hunger one play at a time"
    c = "Your background will be a panoramic view of a fully crowded football stadium, the stage set under the evening sky, stadium lights illuminating the cheering crowd. A large jumbotron displaying an electrifying moment from the Super Bowl game. The thrill in the atmosphere should be palpable."
    return a,b,c

def get_image(image_text):
    url = "https://cdn.discordapp.com/attachments/1112826917276635156/1186395568629612635/JamesE.Willis_Your_background_will_be_a_panoramic_view_of_a_ful_bfca07d6-f4e9-4cac-b87c-f6920740e363.png?ex=659317f9&is=6580a2f9&hm=725e1118db13cbb98ce3bbd9717f2629c5114d4645c77220efc52c57c3389401&"
    return url

# Streamlit UI components
st.title("AI Advertise")

target_consumer = st.selectbox("Target Consumer", ["Adult", "Adult Male", "Adult Female", "Child"])
event = st.selectbox("Event", ["Super Bowl", "Every Day", "Mothers Day", "Valentine's Day"])
user_prompt = st.text_input("Prompt")
generate_text_btn = st.button("Generate Text")

# Placeholder for text, slogan, and image fields
text_placeholder = st.empty()
slogan_placeholder = st.empty()
image_text_placeholder = st.empty()

text, slogan, image_text = "", "", ""

if st.session_state.get('generate_text_btn') != True:
    st.session_state['generate_text_btn'] = generate_text_btn

if st.session_state['generate_text_btn']:
    main_prompt = get_main_prompt(user_prompt, event, target_consumer)
    text, slogan, image_text = generate_assets(main_prompt)
    text = text_placeholder.text_input("Text", text)
    slogan = slogan_placeholder.text_input("Slogan", slogan)
    image_text = image_text_placeholder.text_input("Image", image_text)

    generate_image_btn = st.button("Generate Image")

    if st.session_state.get('generate_image_btn') != True:
        st.session_state['generate_image_btn'] = generate_image_btn

    if generate_image_btn:
        print("HA:", image_text)
        image_url = get_image(image_text)
        st.image(image_url)