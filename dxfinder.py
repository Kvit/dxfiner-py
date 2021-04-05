
import streamlit as st
import numpy as np
import pandas as pd
import simple_elmo

st.title('Dx Finder')
st.write("Find Dx codes for Pathology report")

elmo = simple_elmo.ElmoModel()
elmo.load("model")

txt_in = st.text_area("Pathology Diagnosis Report")

tensors = elmo.get_elmo_vector_average(txt_in.split('. '))
tensors