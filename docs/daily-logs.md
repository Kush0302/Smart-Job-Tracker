# Daily Development Log

## Day 1 – Project Initialization & Setup

**Date:** <4/1/2026>

### Objectives
- Initialize project repository
- Set up backend development environment
- Prepare scalable project structure

### Work Done
- Created a new GitHub repository with clean commit history
- Added `.gitignore` for Python, Django, and environment files
- Created project `README.md`
- Set up Python virtual environment
- Installed base dependencies (Django, DRF, python-dotenv)
- Designed scalable backend folder structure using `src` pattern
- Initialized Django project using `django-admin startproject`
- Verified Django setup

### Outcome
- Clean, professional backend foundation ready for feature development

### Commit Reference
- `feat: initialize Django project with clean backend structure`


## Day 2 – Environment Security & DRF Configuration

**Date:** <5/1/2026>

### Objectives
- Secure sensitive configuration data
- Configure Django REST Framework (DRF)
- Verify backend stability and API readiness

### Work Done
- Created `.env` file at project root for environment variables
- Moved sensitive data (SECRET_KEY, DEBUG) from `settings.py` to `.env`
- Configured `python-dotenv` to load environment variables
- Verified that `.env` is excluded via `.gitignore`
- Installed and verified Django REST Framework
- Added `rest_framework` to `INSTALLED_APPS`
- Configured basic DRF permissions for development
- Successfully ran Django development server and verified setup via browser

### Outcome
- Backend secured against accidental secret leakage
- API-ready Django project configured
- Stable development environment confirmed

### Commit Reference
- `Configured environment variables and Django REST Framework`