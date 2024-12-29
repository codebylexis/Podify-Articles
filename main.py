
import trafilatura
import numpy as np
from tqdm import tqdm

import nltk
import os
import streamlit as st

from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE
from bark.generation import generate_text_semantic, preload_models

os.environ["SUNO_USE_SMALL_MODELS"] = "False"
from scipy.io.wavfile import write as write_wav



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


title_m = '<p style="font-size: 30px;"><b>Turn Your Favourite Articles Into Podcast 🎙️</b></p>'
st.markdown(title_m, unsafe_allow_html=True)

url = st.text_input("Drop the link of the article 🔗")
option = st.selectbox('Please select the voice 🔊 ', ('Male 👨🏻', 'Female 👩🏻'))

if option=='Female 👩🏻':
    SPEAKER = "v2/en_speaker_9"
elif option=='Male 👨🏻':
    SPEAKER = "v2/en_speaker_3"

generate_button = st.button("Generate Podcast ⚡")
if generate_button:
    if url:
        with st.spinner('AI 🤖 Generating The Podcast ⏳...'):
            preload_models()

            downloaded = trafilatura.fetch_url(url)
            text = trafilatura.extract(downloaded)

            intro = "Hello, I hope you are doing well lets start the Podcast."
            script = intro + text
            script = script.replace("\n", " ").strip()
            
            sentences = nltk.sent_tokenize(script)


            GEN_TEMP = 0.6
            silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

            pieces = []
            for sentence in tqdm(sentences):
                semantic_tokens = generate_text_semantic(
                    sentence,
                    history_prompt=SPEAKER,
                    temp=GEN_TEMP,
                    min_eos_p=0.08,  # this controls how likely the generation is to end
                )

                audio_array = semantic_to_waveform(semantic_tokens, history_prompt=SPEAKER,)
                pieces += [audio_array]

            podcast = np.concatenate(pieces)    
            print('Saving')
            write_wav("new_bark_generation_ad_9.wav", SAMPLE_RATE, podcast)
            
            # play text in notebook
            print('Done')
            st.write('Enjoy Your Podcast 🎤')
            st.audio(podcast, sample_rate=SAMPLE_RATE)
    









# download and load all models

#extract the  data
# url = "https://futurism.com/the-byte/footprints-before-humans-americas"







# print(sentences)

# SPEAKER = "v2/en_speaker_3"

# GEN_TEMP = 0.7
# silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

# pieces = []
# for sentence in tqdm(sentences):
#     semantic_tokens = generate_text_semantic(
#         sentence,
#         history_prompt=SPEAKER,
#         temp=GEN_TEMP,
#         min_eos_p=0.04,  # this controls how likely the generation is to end
#     )

#     audio_array = semantic_to_waveform(semantic_tokens, history_prompt=SPEAKER,)
#     pieces += [audio_array]

# print('Saving')
# write_wav("new_bark_generation_ad_3_2.wav", SAMPLE_RATE, np.concatenate(pieces))
  
# # play text in notebook
# print('Done')

