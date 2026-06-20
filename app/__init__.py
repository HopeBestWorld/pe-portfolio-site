import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

ABOUT_ME_TEXT = (
    "Hi there, I'm Hope! I am a software engineer and graduate student blending a "
    "technical foundation in Computer Science with a passion for Information Science at Cornell University. "
    "Whether I'm engineering software systems, optimizing machine learning pipelines, "
    "or collaborating on digital space research, I love creating technology that drives meaningful, strategic impact. "
    "When I'm not writing code, you can find me running long-distance trails, capturing snapshots behind a camera, "
    "or cheering on my favorite creators. Thanks for stopping by my corner of the internet! Let's build something amazing together!"
)

WORK_EXPERIENCES = [
    {
        "role": "Software Engineer Intern",
        "company": "UnitedHealth Group",
        "location": "Eden Prairie, MN",
        "date": "June 2025 - August 2025",
        "description": "Supported high-impact digital transformation initiatives by deploying over 7 production-grade software features to empower data-backed strategic choices."
    },
    {
        "role": "Software Engineer Intern",
        "company": "UnitedHealth Group",
        "location": "Basking Ridge, NJ",
        "date": "June 2024 - August 2024",
        "description": "Architected a HIPAA-compliant LangChain automation agent on Azure OpenAI, integrating containerization via Docker and robust OAuth 2.0 security frameworks."
    }
]

EDUCATION_HISTORY = [
    {
        "institution": "Cornell University",
        "degree": "Master of Professional Studies in Information Science",
        "location": "Ithaca, NY",
        "date": "Expected December 2026",
        "details": "Focusing on human-centered systems, advanced AI infrastructure alignment, and interactive digital design guidelines."
    },
    {
        "institution": "Cornell University",
        "degree": "B.S. in Computer Science",
        "location": "Ithaca, NY",
        "date": "Graduated May 2026",
        "details": "Academic Honors: Dean's Honor List. Coursework highlights: Machine Learning, Big Data Management, Systems Organization, Object-Oriented Programming, and Information Retrieval."
    },
    {
        "institution": "John P. Stevens High School",
        "degree": "High School Diploma",
        "location": "Edison, NJ",
        "date": "Graduated June 2022",
        "details": "AP Scholar with Distinction, National Merit Program Commended Student. Active leader as Captain of the Varsity Cross Country and Spring Track & Field teams."
    }
]

HOBBIES_LIST = [
    {
        "name": "Long-Distance Running",
        "img": "static/img/IMG_4856.jpg",  
        "description": "Running has been a core piece of my life journey! From middle school 1.5-mile races up to serving as Captain of the JPS Varsity Cross Country and Track teams, I love the endurance, clarity, and mental drive that long-distance running demands."
    },
    {
        "name": "Swimming",
        "img": "static/img/IMG_8748.jpg", 
        "description": "I love swimming! It's a great way to stay fit and clear my mind. I've been swimming competitively since I was seven years old and enjoy the discipline and camaraderie it brings."
    }
]

TRAVEL_LOCATIONS = [
    {"city": "Doha, Qatar (AI Health Hackathon)", "coords": [25.2854, 51.5310]},
    {"city": "Salvador, Brazil", "coords": [-12.9777, -38.5016]},
    {"city": "São Paulo, Brazil", "coords": [-23.5505, -46.6333]},
    {"city": "Nassau, Bahamas", "coords": [25.0475, -77.3554]},
    {"city": "Toronto, Canada", "coords": [43.6532, -79.3832]}
]

@app.route('/')
def index():
    return render_template(
        'index.html', 
        title="Hope Best", 
        about_me=ABOUT_ME_TEXT, 
        experiences=WORK_EXPERIENCES,
        education=EDUCATION_HISTORY,
        locations=TRAVEL_LOCATIONS, 
        url=os.getenv("URL")
    )
@app.route('/hobbies')
def hobbies():
    return render_template(
        'hobbies.html',
        title="Hope's Hobbies",
        hobbies=HOBBIES_LIST,
        url=os.getenv("URL")
    )