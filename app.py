import gradio as gr
import os 
import openai
from dotenv import load_dotenv
import autogen

config_whisper_small = [
    {
        "api_type": "open_ai",
        "api_base": "http:",
        "api_key": "NULL"
    }
]


load_dotenv()

def process(name, intensity):
    audio = open(filepath, "rb")
    openai.api_key = null
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=process,
    inputs=gr.Audio(type="filepath"),
    outputs="text"
)

demo.launch()