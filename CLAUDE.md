# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Art Glass Marble Collection Manager - A full-stack web application for cataloging and managing art glass marble collections with AI-powered style identification using OpenAI's vision API.

**Stack:**
- Backend: Python Flask REST API
- Frontend: React with Tailwind CSS
- Database: MySQL 8.0
- AI: OpenAI GPT-4o for marble style identification

## Development Commands

### Initial Setup

1. **Database setup** (prerequisite for all other operations):
   ```bash
   mysql -u root -p < database/schema.sql
   mysql -u root -p < database/seed_data.sql
   ```

2. **Backend setup**:
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env with your DB credentials and OpenAI API key
   pip install -r requirements.txt
   ```

3. **Frontend setup**:
   ```bash
   cd frontend
   npm install
   ```

### Running the Application

- **Backend** (runs on port 5000):
  ```bash
  cd backend
  python main.py
  ```

- **Frontend** (runs on port 3000):
  ```bash
  cd frontend
  npm start
  ```

- **Using Docker Compose** (recommended):
  ```bash
  docker-compose up
  ```

### Testing

- **Backend tests**:
  ```bash
  cd backend
  pytest
  ```

- **Frontend tests**:
  ```bash
  cd frontend
  npm test
  ```

### Build

- **Frontend production build**:
  ```bash
  cd frontend
  npm run build
  ```

## Architecture

### Database Schema

The application uses a relational MySQL database with four main tables:

- **marbles** - Core table storing marble records with columns for size, price, purchase date, description, image URL, and AI-identified style fields
- **artists** - Artist information (name, bio, website)
- **styles** - Marble style categories (Latticino, Lutz, Swirl, Onionskin, etc.)
- **vendors** - Purchase sources/vendors

Foreign key relationships: `marbles.artist_id -> artists.id`, `marbles.style_id -> styles.id`, `marbles.vendor_id -> vendors.id` (all with ON DELETE SET NULL)

### Backend Architecture

**Entry point:** `backend/main.py` - Initializes Flask app, CORS, and registers routes

**Core modules:**
- `app/config.py` - Environment-based configuration (DB credentials, OpenAI API key, upload settings)
- `app/database.py` - Database connection management using mysql-connector-python
- `app/models.py` - Plain Python classes (Marble, Artist) with `to_dict()` methods for JSON serialization
- `app/routes.py` - Flask route handlers for REST API endpoints (currently commented out in main.py - needs to be implemented)
- `app/ai_service.py` - OpenAI integration for marble style identification using GPT-4o vision API

**AI Style Identification Flow:**
1. Client sends base64-encoded image to `/api/identify-style`
2. `ai_service.py` calls OpenAI with image + prompt describing common marble styles
3. Returns JSON: `{"style": "...", "confidence": 0-100, "description": "..."}`

### Frontend Architecture

**Entry point:** `frontend/src/index.js` -> `App.jsx`

**API Layer:** `services/api.js` - Axios-based API client with organized endpoints:
- `marblesAPI` - CRUD operations, bulk create
- `artistsAPI` - List and create artists
- `stylesAPI` - List marble styles
- `vendorsAPI` - List and create vendors
- `aiAPI` - AI style identification

**Component Structure:**
- **Pages:** `MarblesPage.jsx`, `ArtistsPage.jsx` - Top-level page components
- **Forms:** `MarbleForm.jsx`, `BulkAddForm.jsx`, `ArtistForm.jsx` - Data entry
- **Display:** `MarbleCard.jsx`, `SearchFilters.jsx` - Data presentation and filtering
- **AI:** `AIStyleIdentifier.jsx` - Image upload and AI style identification UI

API requests target `http://localhost:5000/api` (configured in `api.js`)

## Configuration Notes

- Backend requires `.env` file based on `.env.example` with DB credentials and OpenAI API key
- Docker Compose provides full environment with MySQL, backend, and frontend containers
- Database credentials in docker-compose.yml: user=marbleuser, password=marblepass, db=marble_collection
- File uploads stored in `backend/uploads/` directory (configurable via UPLOAD_FOLDER env var)
- Max upload size: 16MB (MAX_CONTENT_LENGTH)

## Known Issues

- `backend/app/routes.py` exists but is empty (placeholder file) - routes need to be implemented
- `backend/main.py:21` imports `register_routes` which is commented out but then called uncommented, causing import error
- Several README files in subdirectories are placeholder files (backend/README.md, frontend/README.md, docs/*.md)
- No Dockerfiles exist yet for backend/frontend despite docker-compose.yml referencing them
