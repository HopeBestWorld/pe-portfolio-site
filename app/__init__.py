import os
import re
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    db = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    db = MySQLDatabase(
        os.getenv("MYSQL_DB"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

db.connect()
db.create_tables([TimelinePost])

@app.before_request
def before_request():
    """Connect to the database before every request."""
    if db.is_closed():
        db.connect()

@app.teardown_request
def _db_close(exc):
    """Close the database connection after every request, even if an error occurred."""
    # Skip closing during tests: closing drops the in-memory SQLite tables,
    # breaking any test that makes more than one request.
    if os.getenv("TESTING") == "true":
        return
    if not db.is_closed():
        db.close()

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

NAV_BAR_ITEMS = [
    {"title": "Home", "endpoint": "index"},
    {"title": "Hobbies", "endpoint": "hobbies"},
    {"title": "Timeline", "endpoint": "timeline"}
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
        nav=NAV_BAR_ITEMS,
        url=os.getenv("URL")
    )

@app.route('/hobbies')
def hobbies():
    return render_template(
        'hobbies.html',
        title="Hope's Hobbies",
        hobbies=HOBBIES_LIST,
        nav=NAV_BAR_ITEMS,
        url=os.getenv("URL")
    )

@app.route('/timeline')
def timeline():
    posts = [
        model_to_dict(p)
        for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
    ]
    return render_template('timeline.html', title="Timeline", timeline_posts=posts, nav=NAV_BAR_ITEMS)

# Create POST /api/timeline_post (Add a post)
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    # Reject missing name instead of raising a KeyError
    name = request.form.get('name')
    if not name:
        return "Invalid name", 400

    # Reject missing or malformed email addresses
    email = request.form.get('email')
    if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return "Invalid email", 400

    # Reject missing or empty content
    content = request.form.get('content')
    if not content:
        return "Invalid content", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

# Create GET /api/timeline_post (Retrieve all posts)
@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

# Bonus: Create DELETE /api/timeline_post (Delete a specific post by ID)
@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    post_id = request.form.get('id')
    if not post_id:
        return {"error": "Missing 'id' parameter"}, 400

    try:
        post = TimelinePost.get_by_id(post_id)
        post.delete_instance()
        return {"message": f"Successfully deleted post with id {post_id}"}, 200
    except DoesNotExist:  # <-- Change TimelinePost.DoesNotExist to just DoesNotExist
        return {"error": "Post not found"}, 404

