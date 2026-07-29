# Personal Portfolio & Journey Timeline Site 

Welcome to my personal portfolio and journey timeline web application! Built during the Meta Production Engineering Fellowship, this project showcases my professional background, education, hobbies, travel experiences, and an interactive timeline API.

The site is fully containerized using **Docker Compose** and deployed on a Linux VPS with **Nginx** reverse proxying, **Let's Encrypt SSL/HTTPS** encryption, and custom API **rate limiting**.

---

## Tech Stack & Infrastructure

* **Backend & Web Framework:** Python 3, Flask, Jinja2 Templates, Peewee ORM
* **Database:** MariaDB (Production in Docker), SQLite (Local Testing / Automated CI)
* **Containerization & Orchestration:** Docker, Docker Compose
* **Reverse Proxy & Security:** Nginx, Certbot (Automated SSL/HTTPS), Nginx Rate Limiting
* **Testing:** Unittest, Shell scripting (`run_test.sh`)
* **Deployment & CI/CD:** Automated bash deployment script (`redeploy-site.sh`)

---

## Key Features

* **Dynamic Portfolio Pages:** Multi-page layout covering Work Experience, Education, Hobbies, and Travel Maps rendered via Jinja2.
* **Interactive Timeline API:** RESTful endpoint (`/api/timeline_post`) supporting `POST`, `GET`, and `DELETE` methods for creating and viewing updates.
* **Automated SSL/HTTPS:** Nginx reverse proxy integrated with `jonasal/nginx-certbot` for automatic Let's Encrypt certificate issuance and HTTP-to-HTTPS redirects.
* **Rate-Limited Endpoints:** Nginx rate limiting (`1r/m`) enforced on `POST /api/timeline_post` to protect against spam and abuse.
* **Database Persistence:** Named Docker volume (`mydatabase`) ensuring zero data loss across container restarts and OS reboots.

---

## Local Development Setup

### 1. Prerequisites
* Python 3.9+
* Pip & Virtualenv

### 2. Environment Setup
Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/HopeBestWorld/pe-portfolio-site.git
cd pe-portfolio-site

python3 -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt