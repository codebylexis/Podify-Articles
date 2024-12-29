# "Podify Articles" - Transform Your Favorite Article Into A Podcast 
<p align="center">
<img src="https://media.wired.com/photos/6435f92f13021b2cf16d62ab/16:9/w_2400,h_1350,c_limit/AI-Podcast-GettyImages-1131242410.jpg">  
</p>
<p>In this project, I developed an advanced AI system designed to transform written articles into engaging podcasts with a natural, human-like voice. Recognizing that reading is not everyone’s preferred method of consuming information, and that it often requires a quiet and relaxed environment, this system offers a convenient alternative. It allows users to effortlessly convert their favorite articles into audio format, making it possible to gain knowledge while on the go. Whether you’re commuting, exercising, or multitasking, you can listen to these podcasts at your convenience. Additionally, for those pressed for time, the system includes an option to increase the playback speed, ensuring that users can efficiently manage their time while staying informed.
</p>
<h2>Libraries Used</h2>
<ul>
  <li>Bark</li>
  <li>Scipy</li>
  <li>NLTK</li>
  <li>Numpy</li>
  <li>Trafilatura</li>
  <li>Streamlit</li>
</ul>
<h2>Methodology</h2>
<p>The AI system I developed is structured into two key components: web scraping and podcast generation. The web scraping process, which involves extracting article content from the web, is efficiently handled using the Trafilatura library. This robust tool ensures that all relevant data is gathered and meticulously filtered. To address the model's context window limitations, the extracted content is segmented into individual sentences. This segmentation is crucial for accurate processing and seamless transformation into audio. Once the data is processed, the system assembles the sentences into a coherent and engaging podcast. Additionally, to enhance user experience, the system offers customization options, allowing users to choose between a male or female voice for their podcast, ensuring a personalized and enjoyable listening experience.
</p>
<h2>BARK</h2>
<p align="center">
<img src="https://the-decoder.com/wp-content/uploads/2023/04/dog_headphones_bark_audio_ai_midjourney.png">
</p>
<p>Bark is a transformer-based text-to-audio model created by Suno. Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. The model can also produce nonverbal communications like laughing, sighing and crying.</p>
<h2>Demo Video</h2>



https://github.com/user-attachments/assets/8b05b4c0-ef82-4726-b683-14cd1a1bbde1




<h2>Conclusion</h2>
<p>In this project, I created an AI system that transforms any article into a podcast, having a realistic human voice and engaging narration. The user only has to provide the article's URL, and the system will generate a podcast version of the article using the Bark model. Users also have the option to choose different male and female voices. </p>
