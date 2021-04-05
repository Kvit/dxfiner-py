
import streamlit as st
import numpy as np
import pandas as pd
import simple_elmo
from google.cloud import storage
import os

st.title('Dx Finder')
st.write("Find Dx codes for Pathology report")

model_fle="model/model.hdf5"
st.cache()
def DownloadModel () :
    if not os.path.exists(model_fle) :
        print('Downloading model from cloud storage, please wait..')

        # get file from google storage
        bucket = 'pp-ligolab-models'
        source="model_elmo_2/model.hdf5"

        client = storage.Client.create_anonymous_client()
        bucket = client.bucket(bucket_name=bucket, user_project=None)
        blob = storage.Blob(source, bucket)
        blob.download_to_filename(filename=model_fle, client=client)

#------------

elmo = simple_elmo.ElmoModel()
elmo.load("model")

txt_in = st.text_area("Pathology Diagnosis Report")

tensors = elmo.get_elmo_vector_average(txt_in.split('. '))
tensors