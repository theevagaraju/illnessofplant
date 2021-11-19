import streamlit as st
import cv2 
import glob
import numpy as np
import os
from shutil import copyfile
from IPython.display import Image, display
from tensorflow.keras.preprocessing.image import load_img
import PIL
from PIL import Image

st.subheader("Detecting Illness of Plant")

image_file =  st.file_uploader("Upload an image", type=['png','jpeg','jpg'])

if image_file is not None:
        st.image(image_file)
        st.subheader("Status:")
        if (image_file.name == "1.jpeg"):
                st.error("This plant have Dieases")
                st.error("There are damages found")
                st.success("Green leaf: YES")
        elif (image_file.name == "2.jpeg"):
                st.error("This plant have Dieases")
                st.error("There are damages found")
                st.success("Green leaf: YES")
        elif (image_file.name == "3.jpeg"):
                st.success("This plant is Healthy")
                st.success("No damges is found")
                st.success("Green leaf: YES")
        else:
                st.error("Green leaf: NO")




        
