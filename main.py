import streamlit as st
import requests
from PIL import ImageDraw
from PIL import Image
import io
import json
st.title("顔認識アプリ")

subscription_key = "6e58bef13f3e456687a77e9188c9f665"
assert subscription_key
face_api_url = 'https://20210126-takai.cognitiveservices.azure.com//face/v1.0/detect'



uploaded_file = st.file_uploader("Choose an Image...", type="jpg")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue()  # バイナリ取得

    headers = {
        "Content-Type": "application/octet-stream",
        "Ocp-Apim-Subscription-key": subscription_key
    }
    params = {
        "returnFaceId": "true",
        "returnFaceAttributes": "age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion"
    }

    res = requests.post(face_api_url, params=params, headers=headers, data=binary_img)

    results = res.json()

    for result in results:
        rect = result["faceRectangle"]
        age = result["faceAttributes"]["age"]
        gender = result["faceAttributes"]["gender"]
        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect["left"], rect["top"]), (rect["left"] + rect["width"], rect["top"] + rect["height"])],
                       fill=None, outline="green", width=5)
        draw.text((rect["left"], rect["top"]), str(age), (0, 255, 255))
        draw.text((rect["left"], rect["top"] - 10), str(gender), (0, 255, 255))
    st.image(img, caption="Uploaded Image", use_column_width=True)

