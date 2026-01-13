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


## Day 3 – Jobs App Initialization

**Date:** <7/1/2026>

### Objectives
- Create the core Django app for job tracking
- Integrate the app into the backend project

### Work Done
- Created `jobs` Django app using `startapp`
- Registered the app in `INSTALLED_APPS`
- Verified server stability after integration

### Outcome
- Job tracking module initialized
- Backend ready for model development

### Commit Reference
- `initialize jobs app`


## Day 4 – JobApplication Model Design

**Date:** <8/1/2026>

### Objectives
- Design the core database model for job tracking
- Implement relationships for multi-user support

### Work Done
- Designed `JobApplication` model using Django ORM
- Added fields for company, role, status, and dates
- Linked job applications to users via ForeignKey
- Created and applied database migrations
- Registered model in Django admin panel

### Outcome
- Core backend data structure established
- Database ready for API development

### Commit Reference
- `feat: added JobApplication model`


## Day 5A – User Authentication Design & Architecture

**Date:** <9/1/2026>

### Objectives
- Finalize authentication approach for the project
- Decide user model strategy before implementation
- Define security and data ownership rules
- Plan authentication flow for API-based backend

### Work Done
- Finalized JWT-based authentication strategy for API-first architecture
- Decided to use a custom Django User model for extensibility
- Planned email-based authentication instead of username-based login
- Defined strict ownership rule between users and job applications
- Planned public and protected API access flow
- Documented authentication design without writing implementation code

### Outcome
- Authentication architecture finalized
- Secure foundation established for multi-user support
- Reduced future refactoring by locking decisions early
- Backend prepared for secure API development

### Commit Reference
- `docs: Finalize authentication architecture (Day 5A)`


## Day 5B – Custom User Model Implementation

**Date:** <10/1/2026>

### Objectives
- Implement a custom Django User model
- Replace default authentication user safely
- Prepare backend for JWT-based authentication
- Ensure correct user ownership across models

### Work Done
- Created `accounts` app at project level
- Implemented custom `User` model using `AbstractUser`
- Updated `AUTH_USER_MODEL` in `settings.py`
- Updated `JobApplication` user reference to `settings.AUTH_USER_MODEL`
- Reset and regenerated migrations for consistency
- Applied migrations successfully
- Created new superuser and verified setup

### Outcome
- Custom User model successfully integrated
- Authentication foundation stabilized
- Database schema aligned with future security needs
- Project ready for JWT authentication implementation

### Commit Reference
- `feat: add custom user model and reset migrations`


## Day 6 + Day 7 – JWT Authentication & Secure Job APIs

**Date:** 11/01/2026

### Objectives

- Implement JWT-based authentication using Django REST Framework
- Secure job-related APIs so only authenticated users can access them
- Ensure users can only view and create their own job applications

### Work Done

- Installed and configured djangorestframework-simplejwt
- Added JWT authentication to global DRF settings
- Implemented login endpoint and tested token generation using Postman
- Secured job APIs using IsAuthenticated permission
- Filtered job listings by logged-in user using get_queryset()
- Automatically assigned the authenticated user during job creation via perform_create()
- Resolved integrity errors related to user and applied_date fields
- Successfully tested POST and GET job APIs with JWT tokens

### Outcome

- Job APIs are fully secured using JWT authentication
- Users can only access and manage their own job applications
- Backend prevents unauthorized access and user data leakage
- Day 6 backend functionality is production-ready

### Commit Reference
- `feat: Secured job APIs with JWT auth and user-based access control`


## Day 8 – API Validation & Business Rules

**Date:** 12/01/2026

### Objectives

- Validate job-related API inputs using Django REST Framework serializers
- Enforce business rules to maintain data integrity
- Ensure APIs reject invalid, duplicate, or unauthorized requests
- Test all validation and security scenarios using Postman

### Work Done

- Added field-level validations in JobApplicationSerializer:
- Prevented empty company_name and job_role
- Blocked future dates for applied_date
- Ensured only valid status values are accepted
- Implemented object-level validation to prevent duplicate job applications per user
- Ensured authenticated user is automatically assigned during job creation
- Verified JWT-protected endpoints using Postman with Authorization headers
- Tested multiple invalid scenarios including:
- Missing or invalid fields
- Duplicate job entries
- Unauthorized access without JWT token
- Confirmed API returns appropriate HTTP error responses (400, 401) for invalid requests

### Outcome

- Job APIs now strictly enforce validation and business rules
- Duplicate and invalid job entries are fully prevented
- API behavior is consistent, secure, and production-ready

### Commit Reference
- `feat: Added serializer validations and business rules for job APIs`