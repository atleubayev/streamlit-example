import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))


def get_main_prompt(prompt, event, target_consumer):
    # Mock implementation - replace with your actual logic
    # return f"Main prompt based on: {prompt}"
    # def get_prompt(product_name, brand_name, target_consumer, prompt, event):
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
    # Mock implementation - replace with your actual logic
    # return "Text based on prompt", "Slogan based on prompt", "Image text based on prompt"
    a = "Introducing SNICKERS, the game changer of the candy world. Unwrap the thrill of rich, decadent milk chocolate perfectly layered with smooth caramel and delicious nougat, all cradling a savory mix of satisfying roasted peanuts. A powerhouse of energy and flavor, it's the perfect companion for those Super Bowl nail-biter moments. Give your taste buds the rush of a touchdown with every bite of SNICKERS."
    b = "SNICKERS, tackling hunger one play at a time"
    c = "Your background will be a panoramic view of a fully crowded football stadium, the stage set under the evening sky, stadium lights illuminating the cheering crowd. A large jumbotron displaying an electrifying moment from the Super Bowl game. The thrill in the atmosphere should be palpable."
    return a,b,c

def get_image(image_text):
    # Mock implementation - replace with your actual logic
    # return "https://example.com/image.jpg"  # Replace with actual image URL generation logic
    url = "https://cdn.discordapp.com/attachments/1112826917276635156/1186395568629612635/JamesE.Willis_Your_background_will_be_a_panoramic_view_of_a_ful_bfca07d6-f4e9-4cac-b87c-f6920740e363.png?ex=659317f9&is=6580a2f9&hm=725e1118db13cbb98ce3bbd9717f2629c5114d4645c77220efc52c57c3389401&"
    return url

# Streamlit UI components
st.title("Image Generation App")

target_consumer = st.selectbox("Target Consumer", ["Adult", "Adult Male", "Adult Female", "Child"])
event = st.selectbox("Event", ["Super Bowl", "Every Day", "Mothers Day", "Valentine's Day"])
user_prompt = st.text_input("Prompt")
generate_text_btn = st.button("Generate Text")

# Placeholder for text, slogan, and image fields
text_placeholder = st.empty()
slogan_placeholder = st.empty()
image_text_placeholder = st.empty()

if generate_text_btn:
    main_prompt = get_main_prompt(user_prompt, event, target_consumer)
    text, slogan, image_text = generate_assets(main_prompt)
    text = text_placeholder.text_input("Text", text)
    slogan = slogan_placeholder.text_input("Slogan", slogan)
    image_text = image_text_placeholder.text_input("Image", image_text)

    generate_image_btn = st.button("Generate Image")

    if generate_image_btn:
        image_url = get_image(image_text)
        st.image(image_url)