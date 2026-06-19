import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Personable and professional introduction profile details
ABOUT_ME_TEXT = (
    "Hi there, I'm Hope! I am a software engineer and graduate student blending a "
    "technical foundation in Computer Science with a passion for Information Science at Cornell University. "
    "Whether I'm engineering software systems, optimizing machine learning pipelines, "
    "or collaborating on digital space research, I love creating technology that drives meaningful, strategic impact. "
    "When I'm not writing code, you can find me running long-distance trails, capturing snapshots behind a camera, "
    "or cheering on my favorite creators. Thanks for stopping by my corner of the internet! Let's build something amazing together!"
)

@app.route('/')
def index():
    return render_template(
        'index.html', 
        title="Hope Best", 
        about_me=ABOUT_ME_TEXT, 
        url=os.getenv("URL")
    )