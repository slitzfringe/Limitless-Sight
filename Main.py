import cv2
import google.generativeai as genai
from dotenv import load_dotenv
import pyttsx3
import time
import os
import speech_recognition as sr



from elevenlabs import Voice, VoiceSettings, save
from elevenlabs.client import ElevenLabs

import librosa

import shutil

from gradio_client import Client

from elevenlabs.client import ElevenLabs
import pandas as pd

from pydub import AudioSegment

from pydub.playback import play

import pygame
pygame.init()

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

client = ElevenLabs(
  api_key = "ELEVEN_LABS_API_KEY", # Defaults to ELEVEN_API_KEY
)

# lisa_voice = os.getenv("VOICE_ID")

client_bgm = Client("https://facebook-musicgen.hf.space/")

# ESP32 (Camera) Feed
url = 'URL_OF_ESP32'


# Prompt for Image to Story
input_prompt = """
Write a descriptive narrative story for this image to assist visually impaired individuals in understanding their surroundings.
The narrative should accurately convey the objects, people, and activities present in the scene without resorting to fictional characters or unnecessary embellishments.
Focus on providing clear, concise descriptions that allow the reader to visualize the environment and understand the context effectively.

Try to add poems or any other related artist/literature works whenever required  to make the lister feel blissful.

mood: Happy
tone: Happy

Don't explicitly mention that you are narrating keep it like they are seeing.

Try to incorporate the output within 2000 words.

"""

# speech_note = ""

extro = r".\Extro.mp3"
intro = r".\Intro.mp3"


def play_audio(audio_file):
  """
  Plays the provided audio file (WAV or MP3) using pygame.

  Args:
      audio_file (str): Path to the audio file.
  """
  # Load the audio
  sound = pygame.mixer.Sound(audio_file)

  # Play the audio
  sound.play()

  

  # Wait for the audio to finish playing (optional)
  while pygame.mixer.get_busy():
      pygame.time.wait(100)
  return 0



def get_gemini_response(input, image):

    '''
    Returns the response from Gemini api on prompting!
    '''

    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0]])
    return response.text



def capture_and_generate_story(input_prompt):
    """
    Captures an image from the webcam, generates a story.
    """
    
    # Open the default webcam
    cap = cv2.VideoCapture(0)  
    
    # Esp32 cam
    # cap = cv2.VideoCapture(url)  

    for i in range(10):
        # Capture a frame
        ret, frame = cap.read()
    
        if not ret:
            print("Error capturing frame")
        else:
            break

    filename_d = r".\image_new_flipped.jpg"
    filename = r".\Input.jpg"

    # Write the frame to a JPEG file
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(filename, frame)
    cv2.imwrite(filename_d, frame)

    # Show the frame for user confirmation (optional)
    # cv2.imshow('Capture', frame)
    # time.sleep(5000)
    

    # Encode the frame as JPEG bytes and prepare image data
    image_data = [
        {
           "mime_type": "image/jpeg",
           "data": cv2.imencode(".jpg", frame)[1].tobytes()
        }
    ]

        # Release the webcam and generate the story
    cap.release()
    cv2.destroyAllWindows()

    story = get_gemini_response(input_prompt, image_data)

    print()
    print(story)
    print("\n\nStory Generated! Proceeding....")
    return story



def trigger_function(text):

    '''Logging the user activites.'''
    # print("Limitless Sight activated!")
    print("User: ", text)

    speech_note = capture_and_generate_story(input_prompt)
    return speech_note



def listen_for_trigger():

    '''
    Input from the Mic is taken, Triggered at 'Describe'. 
    '''

    r = sr.Recognizer()
    # my_mic = sr.Microphone(device_index = device_number)
    my_mic = sr.Microphone()
    

     
    with my_mic as source:
        print("Listening for 'Describe'...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        if "describe" in text.lower():
            speech_note = trigger_function(text.lower())

            print(execute_pipeline(speech_note))

        if "thankyou" in text.lower():
            th_text = "\n\nThank you for using Limitless Sight!!!"
            # text_to_speech(th_text)
            print(th_text)   
            play_audio(extro)
            exit()



    except sr.UnknownValueError:
        print("\n\nSorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("\n\nCould not request results from Google Speech Recognition service; {0}".format(e))



def text_to_Speech(speech_note):

  r"""
  Text is converted to speech and saved at \Speech\Speech.wav
  """
  
  
  save_path = r".\Speech.mp3"

  
  # client = ElevenLabs(
  #   api_key = apikey, # Defaults to ELEVEN_API_KEY
  #   )


  audio_stream = client.generate(
    text = speech_note,
    stream = True,
    voice = Voice(
      voice_id = "VVOICE_ID", 
      settings = VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
      ),
    )


  save(audio_stream, save_path)

  print("\n\nSpeech.mp3 saved at " + save_path + "\n\n proceeding...")

  return save_path






def get_duration(audio_path):

    r"""
    returns the duration of the audio_clip in seconds.
    example of audio_path: '.\text_to_audio.wav' 
    
    """
    
    # Load the audio file with a specific sampling rate
    audio_data, sample_rate = librosa.load(audio_path, sr=25)

    # Calculate the duration of the audio file
    duration = librosa.get_duration(y=audio_data, sr=sample_rate)

    print("\n\nDuration of the audio file:", duration, "seconds")

    return duration




def copy_a_to_b(source_path, destination_path = r'.\music_files\Music'):

    r"""
    Copies source file to destination.
    Default Destination: Music (musicGen) ['C.\music_files\Music']
    """

    shutil.copy2(source_path, destination_path)





def get_bgm(prompt, file_path=None):

    """
    Generates bgm of 15 seconds based on the prompt.
    Thanks to MusicGen...
    example of prompt = "pads, lo-fi, chillout, flute, harp, ambient"
    """

    # client_bgm = Client("https://facebook-musicgen.hf.space/")
    result = client_bgm.predict(
        prompt,	# str  in 'Describe your music' Textbox component
        file_path,	# str (filepath or URL to file) in 'File' Audio component
        prompt_sample_rate = 25,
        progress = True,        
        fn_index=0
    )
    
    print("\n\nBGM generated: ", result)
    return result[1]




def find_voice_id(name):

  """
  This function is used to find the voice_id with 'name'
  """

  # client = ElevenLabs(
  #   api_key = apikey, # Defaults to ELEVEN_API_KEY
  # )

  response = client.voices.get_all()
  # audio = client.generate(text="Hello there!", voice=response.voices[0])


  voices = response.voices
 
  df = pd.DataFrame(voices)
  f_df = df[df[1].apply(lambda x: x[1] == name)]
  x = tuple(f_df[0])

  return x[0][1]



def music_prompt_from_text(Speech_note):

    '''
    Generates music_prompt according to the speech_note.
    '''

    music_prompt = '''" music_tags = ["hip hop", "trap", "soul", "rnb", "synth", "songstarters", "melody", "keys", "chords", "guitar", "vocals", "dancehall", "melodic stack", "piano", "electric", "layered", "music", "drill", "lo-fi hip hop", "cinematic", "pop", "resampled", "afropop & afrobeats", "strings", "leads", "dark", "african", "acoustic", "brass & woodwinds", "live sounds", "reggaeton", "boom bap", "pads", "electric piano", "fx", "downtempo", "wet", "electric guitar", "lo-fi", "caribbean", "chops", "chillout", "riffs", "percussion", "electronic", "bass", "choir", "arp", "uk drill", "female", "plucks", "future bass", "processed", "future soul", "ensemble", "mallets", "hooks", "uk", "flute", "phrases", "drums", "atmospheres", "jazz", "emo", "gospel", "male", "reverse", "latin american", "trap edm", "latin", "bells", "pitched", "ambient", "tonal", "distorted", "moombahton", "vinyl", "orchestral", "dry", "psychedelic", "edm", "funk", "neo soul", "classical", "harmony", "adlib", "trumpet", "high", "horns", "electronica", "violin", "808", "synthwave", "ngoni", "house", "drones", "progressive house", "g-funk", "hats", "trip hop", "baile funk", "filtered", "doo wop", "tambourine", "kora", "stabs", "textures", "claps", "grooves", "clean", "analog", "harp", "ambience", "smooth", "acapella", "blues", "saxophone", "organ", "soft", "tremolo", "chillwave", "reverb", "electric bass", "low", "moog", "wah", "wobble", "indie pop", "modular", "sub", "indie dance", "glide", "k-pop", "afrobeat", "mid", "balafon", "bitcrushed", "phaser", "middle eastern", "zither", "shakers", "delay", "tech house", "disco", "experimental", "celesta", "cello", "drum and bass", "trance", "rock", "rhythm", "whistle", "sidechained", "saw", "breakbeat", "techno", "brazilian", "music box", "glitch", "clarinet"] 

    Assume your a musician, now with story try and pick 6 most important tag and output it in this fashion "pads, lo-fi, chillout, flute, harp, ambient"

    please display only the tags
    '''

    input = "story = " + Speech_note + "\n\n" + music_prompt
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input])

    print("\n\nmusic_tag =",response.text)
    return response.text




def combine_audios(speech_path, bgm_path):

    r'''
    Combines the Speech & Bgm
    Exported to '.\Final\final_fade_length1.wav'.
    '''


    # Load audio files
    speech = AudioSegment.from_mp3(speech_path)
    bgm = AudioSegment.from_wav(bgm_path)

    
    # Adjust the volume of the background music to be 10 dB less than the speech
    bgm = bgm - 23
    speech = speech - 10

    # Add silence of 3 seconds at the start and end of the BGM
    silence = AudioSegment.silent(duration=3000)  # duration in milliseconds
    speech = silence + speech + silence

    # If the BGM is shorter than the speech, loop it until it matches the length of the speech
    bgm = bgm * (len(speech) // len(bgm) + 1)
    bgm = bgm[:len(speech)]

    # Add fade-in and fade-out
    bgm = bgm.fade_in(4000).fade_out(4000)

    # Combine the speech and BGM
    combined = speech.overlay(bgm)

    # Save the result
    final_path = r'.\Final\final_fade_length1.wav'
    combined.export(final_path, format='wav')

    print("\n\n" + r"Export Completed!, Find at "+ final_path + "\n") 
    
    return final_path



def play_music(final_path):
    
    '''
    Outputs audio through Speaker.
    Use earphones for better experience!!
    '''
    
    audio = AudioSegment.from_wav(final_path).set_channels(1)
    

    
    # Play the audio file
    play(audio)

    return "Cycle Succesfully Completed!"





def execute_pipeline(speech_note):
    # Convert Image to text --> speech_note is global variable and is containing story from capture_and_generate_story()


    # Convert text to speech
    speech_path = text_to_Speech(speech_note)  # saved at \Speech

    # Get music tags from gemini based on speech_note
    music_tag = music_prompt_from_text(speech_note)

    # Creating music of 15 seconds interdependentely
    music1 = get_bgm(music_tag)
    music2 = get_bgm(music_tag, file_path = music1)  

    # Replacing bgms to \Music
    copy_a_to_b(music2)

    # Combining speech and bgm
    final_audio = combine_audios(speech_path, music2)

    # Use earphones for better experience!!
    out = play_audio(final_audio)

    return "Successfully executed"




# Execution

play_audio(intro)
while True:
    listen_for_trigger()



