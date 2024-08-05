# Limitless-Sight

Thank you for taking the time to read this post.

What started as a spark of curiosity led us to create something truly meaningful: Limitless Sight. 

At the beginning of our final year, as we brainstormed ideas for our engineering project, our focus was on creating something that would genuinely make a difference. Instead of following the well-trodden path, we chose to address a need that could bring positive change to society, specifically for visually impaired individuals.

The idea started with some creative sparks from my teammates, but it wasn’t until a discussion with Nitin and a personal incident involving my uncle that we landed on the theme of aiding the visually impaired. We didn’t want to reinvent the wheel but rather focus on how we could use existing technology in a creative, meaningful way.

Limitless Sight was born, with the tag-line “Hear the unseen, feel the unimagined...” from a simple, yet powerful idea: to help visually impaired individuals "see" the world around them through sound. 

# Product video:
https://github.com/user-attachments/assets/e46b8998-2ba7-4678-86cb-717f6b1225c3

# The Impact:

    • Enhanced Independence: Empowering users to independently understand their surroundings.
    • Emotional Enrichment: Audio narratives provide both information and emotional depth. 
    • Broadened Engagement: Facilitates deeper interaction with content and experiences that are traditionally visual, enhancing overall inclusivity. 
    • Mental Well-being: Offering content that evokes positive emotions and supports mental health.
    • Inspiration for Innovation: Showcasing the potential of technology to address real-world challenges creatively.


# Demo Output

https://github.com/user-attachments/assets/68789303-5f0f-46dc-bd40-eca9296d2b19

# How It Works:

Limitless Sight harnesses the power of generative AI to create an immersive auditory experience. We used Google Gemini for converting images into text descriptions, focusing on clarity and accuracy to paint a vivid picture, allowing listener to imagine their surroundings.  
Facebook MusicGen then adds a layer of emotional depth by generating mood-synchronized background music. Finally, Eleven Labs converts the narrative into speech,  merging it seamlessly with the background music to produce a complete audio experience that is both informative and immersive.
We demonstrated our prototype using an ESP32 cam connected via Wi-Fi, with data processing happening on my laptop, which we presented as a microprocessor and the final output-“a combination of narrative and music” was delivered through a Bluetooth neckband.
With precision and persistence, we provided an on-the-go solution for users.

# Dependences:
This are the dependencies that were present in my conda environment.

    gradio_client
    librosa
    elevenlabs
    pandas
    pydub
    altair==5.2.0
    annotated-types==0.6.0
    anyio==4.3.0
    asttokens 
    attrs==23.2.0
    audioread==3.0.1
    blinker==1.7.0
    cachetools==5.3.2
    certifi==2023.11.17
    cffi==1.16.0
    charset-normalizer==3.3.2
    click==8.1.7
    colorama 
    comm 
    comtypes==1.2.1
    debugpy 
    decorator
    elevenlabs==1.2.1
    exceptiongroup 
    executing 
    filelock==3.14.0
    fsspec==2024.3.1
    gitdb==4.0.11
    GitPython==3.1.41
    google-ai-generativelanguage==0.4.0
    google-api-core==2.16.1
    google-auth==2.27.0
    google-generativeai==0.3.2
    googleapis-common-protos==1.62.0
    gradio_client==0.16.2
    grpcio==1.60.0
    grpcio-status==1.60.0
    h11==0.14.0
    httpcore==1.0.5
    httpx==0.27.0
    huggingface-hub==0.23.0
    idna==3.6
    importlib-metadata
    ipykernel 
    ipython 
    jedi 
    Jinja2==3.1.3
    joblib==1.4.2
    jsonschema==4.21.1
    jsonschema-specifications==2023.12.1
    jupyter_client
    jupyter_core
    lazy_loader==0.4
    librosa==0.10.2
    llvmlite==0.42.0
    markdown-it-py==3.0.0
    MarkupSafe==2.1.4
    matplotlib-inline
    mdurl==0.1.2
    msgpack==1.0.8
    nest_asyncio 
    numba==0.59.1
    numpy==1.26.3
    opencv-python==4.9.0.80
    packaging 
    pandas==2.2.0
    parso 
    pickleshare 
    pillow==10.2.0
    platformdirs
    pooch==1.8.1
    prompt-toolkit 
    proto-plus==1.23.0
    protobuf==4.25.2
    psutil
    pure-eval 
    pyarrow==15.0.0
    pyasn1==0.5.1
    pyasn1-modules==0.3.0
    PyAudio==0.2.14
    pycparser==2.22
    pydantic==2.7.1
    pydantic_core==2.18.2
    pydeck==0.8.1b0
    pydub==0.25.1
    Pygments 
    pypiwin32==223
    python-dateutil
    python-dotenv==1.0.1
    pyttsx3==2.90
    pytz==2023.4
    pywin32==306
    PyYAML==6.0.1
    pyzmq 
    referencing==0.33.0
    requests==2.31.0
    rich==13.7.0
    rpds-py==0.17.1
    rsa==4.9
    scikit-learn==1.4.2
    scipy==1.13.0
    setuptools==69.0.3
    six 
    smmap==5.0.1
    sniffio==1.3.1
    soundfile==0.12.1
    soxr==0.3.7
    SpeechRecognition==3.10.1
    stack-data 
    streamlit==1.30.0
    tenacity==8.2.3
    threadpoolctl==3.5.0
    toml==0.10.2
    toolz==0.12.1
    tornado 
    tqdm==4.66.1
    traitlets 
    typing_extensions 
    tzdata==2023.4
    tzlocal==5.2
    urllib3==2.2.0
    validators==0.22.0
    watchdog==3.0.0
    wcwidth
    websockets==11.0.3
    wheel==0.42.0
    zipp 

# Gratitude:
A big thank you to Google Gemini, Facebook MusicGen, and Eleven Labs for their exceptional APIs that made this project possible.
I’m especially grateful to Archana Ma’am for her belief and support, and to David Sir for giving us the initial confidence boost.
A special mention to Vaishnav K for his unwavering support and invaluable contributions, which were instrumental in bringing this project to life. My deepest thanks to Swathi Ambujakshan Am for the crucial advice to stay calm and focused, helping us overcome challenges and stay on track.
A heartfelt thanks to my entire team, mentors, and everyone who helped make this vision a reality.


# In sum:
Limitless Sight is more than just a project; Limitless Sight represents the fusion of creativity and technology to make a meaningful impact. We hope our project inspires further innovation and contributes to a more inclusive world.

Thank you for your support, and enjoy the demo and product videos!


Best regards,
Team Limitless Sight
