### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import pyttsx3
engine = pyttsx3.init()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

### loading Google Gemini Pro Vision API 
def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check for successfull file upload
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        #This is the format required by Google Gemini Pro
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    


st.set_page_config(page_title="Gemini Health App")

st.header("Wellness Hub By Mohammed Younis")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

on = st.toggle('Activate Text to Speech')
submit1=st.button("Tell me the total calories and how much I need to run to burn them")
submit2=st.button("Check if the meal contains all the daily value needed nutritions and what is missing?")
submit3=st.button("How can this meal be improved to contain all the necessary nutritions?")
submit4=st.button("How can a bodybuilder get the needed healthy meals for muscle growth")
submit5=st.button("Can you give me a healthy smoothie recipe using items in the image?")
submit6=st.button("Not sure what to cook today? take a picture of your fridge and let me help you enter what type of food you feel like eating in the box below")
submit7=st.button("Can you give a cooking plan for one week?")
Additional=st.text_input("Additional Questions?")
input_prompt1="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
and then give me the sum of all calories, along with how long I need to run to burn these calories.

"""
input_prompt2="""
You are an expert in nutritionist where you need to see the food items from the image
               and check if the meal contains all the daily value needed nutritions, and  check what nutritions are missing from the meal?
"""



input_prompt3="""
You are an expert in nutritionist where you need to see the food items from the image
               and check how we can improve this meal to contain all the necessary needed nutritions?
"""
input_prompt4="""
You are an expert in nutritionist and body building where you need to see the food items from the image
               and check how can a bodybuilder get the needed healthy meals for muscle growth
"""

input_prompt5="""
You are an expert in nutritionist where you need to see the food items from the image and provide a recipe for a smoothie than can be made 
                using the items in the image. can you please try avoid putting rice and potatoes in the recipe.

"""
input_prompt6="""
You are an expert in nutritionist where you need to see the food items from the image
and use the items in the image to come up with a lunch recipe.

"""

input_prompt7="""
You are an expert in nutritionist where you need to see the food items from the image
and use the items in the image to come up with lunch cooking plan for one week

"""

## If submit button is clicked
if submit1:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt1,image_data,Additional)#,input
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()
elif submit2:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt2,image_data,Additional)
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()
elif submit3:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt3,image_data,Additional)
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()
elif submit4:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt4,image_data,Additional)
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()
elif submit5:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt5,image_data,Additional)
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()
elif submit6:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt6,image_data,Additional)
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()
elif submit7:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt7,image_data,Additional)
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()
elif Additional:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(Additional,image_data,Additional)
    st.subheader("The Response is")
    st.write(response)
    if on:
            engine.say(response)
            engine.runAndWait()