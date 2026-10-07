# Beab Girma — Portfolio

A multi-page, trilingual portfolio website built with Django. Content is served in **English, French, and Amharic**, with language switching handled server-side and persisted per session.

## Features

- **Trilingual content (EN / FR / AM)**: switch languages with `?lang=en|fr|am`; the choice is stored in the session and carried across pages.
- **Translated project data**: project descriptions are stored per language at the model level, not just in the UI strings.
- **Multi-page layout**: Home, About & Journey, Projects, Experiences & Skills, and Touches & Rhythm.
- **Dark, minimalist UI**: glassmorphism cards, gradient accents, and a responsive bento-grid layout, built with vanilla HTML, CSS, and JavaScript.

## Tech Stack

| Layer     | Technology                                  |
|-----------|---------------------------------------------|
| Backend   | Python 3.13, Django 6.0                     |
| Frontend  | Django Template Language, HTML, CSS, JS     |
| Database  | SQLite (development)                        |

## Project Structure

```
beab-portofolio/
├── config/               Project settings, root URL configuration, WSGI/ASGI entry points
├── core/                 Page views, templates, translation dictionary, Project model
│   └── templates/core/   Page templates (index, projects, ...)
├── portofolio_engine/    Content models (perspectives and their translations) and service layer
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.13+
- Git

### Installation

```bash
git clone https://github.com/beabgirma/beab-portfolio.git
cd beab-portfolio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/.

### Environment Variables

| Variable            | Purpose                                   | Default (development only) |
|---------------------|-------------------------------------------|----------------------------|
| `DJANGO_SECRET_KEY` | Cryptographic signing key                 | Insecure placeholder       |

Generate a production key with:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## How Language Switching Works

1. A request arrives with an optional `?lang=` query parameter.
2. If the value is a supported language, it is saved to `request.session['lang']`.
3. Otherwise, the session value is used, falling back to English.
4. The view passes the matching translation dictionary to the template as `t`, so templates render strings with `{{ t.key }}`.

## Roadmap

- [ ] Touches & Rhythm page (music and its parallels to software design)
- [ ] Experiences & Skills page (internship, seminar delegation, tech stack)
- [ ] Project detail cards with tech tags and GitHub / live demo links
- [ ] Shared `base.html` template and a static stylesheet
- [ ] Language context processor with English fallback for missing keys
- [ ] Test suite with `pytest-django`
- [ ] Production deployment with CI/CD

## Author

**Beab Girma Yifrashewa**, Computer Science, University of British Columbia Okanagan
