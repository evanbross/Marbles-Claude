"""
Marble Collection Manager - Project Setup Script
Creates complete directory structure and all necessary files
"""

import os
import json

# Base project directory
BASE_DIR = r"f:\evan-f\projects\marbles-claude"

# Project structure
PROJECT_STRUCTURE = {
    "backend": {
        "app": {
            "__init__.py": "",
            "config.py": "",
            "models.py": "",
            "routes.py": "",
            "database.py": "",
            "ai_service.py": ""
        },
        "migrations": {},
        "tests": {
            "__init__.py": "",
            "test_api.py": ""
        },
        "uploads": {},
        "requirements.txt": "",
        "main.py": "",
        ".env.example": "",
        "README.md": ""
    },
    "frontend": {
        "public": {
            "index.html": ""
        },
        "src": {
            "components": {
                "MarbleCard.jsx": "",
                "MarbleForm.jsx": "",
                "BulkAddForm.jsx": "",
                "ArtistForm.jsx": "",
                "SearchFilters.jsx": "",
                "AIStyleIdentifier.jsx": ""
            },
            "pages": {
                "MarblesPage.jsx": "",
                "ArtistsPage.jsx": ""
            },
            "services": {
                "api.js": ""
            },
            "utils": {
                "helpers.js": ""
            },
            "App.jsx": "",
            "index.js": "",
            "index.css": ""
        },
        "package.json": "",
        "tailwind.config.js": "",
        "README.md": ""
    },
    "database": {
        "schema.sql": "",
        "seed_data.sql": "",
        "README.md": ""
    },
    "docs": {
        "API.md": "",
        "SETUP.md": "",
        "USER_GUIDE.md": ""
    },
    ".gitignore": "",
    "README.md": "",
    "docker-compose.yml": ""
}

def create_directory_structure(base_path, structure, current_path=""):
    """Recursively create directory structure"""
    for name, content in structure.items():
        full_path = os.path.join(base_path, current_path, name)
        
        if isinstance(content, dict):
            # It's a directory
            os.makedirs(full_path, exist_ok=True)
            print(f"Created directory: {full_path}")
            create_directory_structure(base_path, content, os.path.join(current_path, name))
        else:
            # It's a file
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created file: {full_path}")

def write_file(base_path, relative_path, content):
    """Write content to a specific file"""
    full_path = os.path.join(base_path, relative_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {full_path}")

# File contents
FILES_CONTENT = {
    "backend/requirements.txt": """flask==3.0.0
flask-cors==4.0.0
mysql-connector-python==8.2.0
python-dotenv==1.0.0
openai==1.3.0
Pillow==10.1.0
pytest==7.4.3
""",
    
    "backend/.env.example": """# Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=marble_collection

# OpenAI API Key for AI Style Identification
OPENAI_API_KEY=your_openai_api_key_here

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your_secret_key_here

# Upload Configuration
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216
""",

    "backend/main.py": """from flask import Flask
from flask_cors import CORS
from app.routes import register_routes
from app.database import init_db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH', 16777216))

CORS(app)

# Initialize database
init_db()

# Register routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
""",

    "backend/app/config.py": """import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_CONFIG = {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', 'marble_collection')
    }
    
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
""",

    "backend/app/database.py": """import mysql.connector
from mysql.connector import Error
from app.config import Config

def get_db_connection():
    try:
        connection = mysql.connector.connect(**Config.DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if conn:
        print("Database connection successful!")
        conn.close()
    else:
        print("Failed to connect to database")
""",

    "backend/app/models.py": """# Database models and utility functions

class Marble:
    def __init__(self, id=None, name=None, artist_id=None, style_id=None, 
                 size_mm=None, price=None, purchase_date=None, vendor_id=None,
                 description=None, image_url=None, ai_identified_style=None,
                 ai_confidence=None):
        self.id = id
        self.name = name
        self.artist_id = artist_id
        self.style_id = style_id
        self.size_mm = size_mm
        self.price = price
        self.purchase_date = purchase_date
        self.vendor_id = vendor_id
        self.description = description
        self.image_url = image_url
        self.ai_identified_style = ai_identified_style
        self.ai_confidence = ai_confidence
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist_id': self.artist_id,
            'style_id': self.style_id,
            'size_mm': self.size_mm,
            'price': self.price,
            'purchase_date': str(self.purchase_date) if self.purchase_date else None,
            'vendor_id': self.vendor_id,
            'description': self.description,
            'image_url': self.image_url,
            'ai_identified_style': self.ai_identified_style,
            'ai_confidence': self.ai_confidence
        }

class Artist:
    def __init__(self, id=None, name=None, bio=None, website=None):
        self.id = id
        self.name = name
        self.bio = bio
        self.website = website
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'bio': self.bio,
            'website': self.website
        }
""",

    "backend/app/ai_service.py": """from openai import OpenAI
from app.config import Config
import json

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def identify_marble_style(image_data):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": '''Analyze this glass marble image and identify its style. 
                            Common styles include: Latticino, Lutz, Swirl, Onionskin, Mica, 
                            End of Day, Cat's Eye, Clambroth, Sulphide, Contemporary Art.
                            Respond with JSON: {"style": "style_name", "confidence": 0-100, 
                            "description": "brief description"}'''
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        return {"error": str(e)}
""",

    "database/schema.sql": """-- Art Glass Marble Collection Database Schema

CREATE DATABASE IF NOT EXISTS marble_collection;
USE marble_collection;

-- Artists table
CREATE TABLE artists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Styles table
CREATE TABLE styles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vendors/Sources table
CREATE TABLE vendors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Marbles table
CREATE TABLE marbles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    artist_id INT,
    style_id INT,
    size_mm DECIMAL(5,2) NOT NULL,
    price DECIMAL(10,2),
    purchase_date DATE,
    vendor_id INT,
    description TEXT,
    image_url VARCHAR(500),
    ai_identified_style VARCHAR(100),
    ai_confidence DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE SET NULL,
    FOREIGN KEY (style_id) REFERENCES styles(id) ON DELETE SET NULL,
    FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE SET NULL
);

-- Indexes for faster searches
CREATE INDEX idx_artist ON marbles(artist_id);
CREATE INDEX idx_style ON marbles(style_id);
CREATE INDEX idx_size ON marbles(size_mm);
CREATE INDEX idx_price ON marbles(price);
""",

    "database/seed_data.sql": """USE marble_collection;

-- Insert common marble styles
INSERT INTO styles (name, description) VALUES
('Latticino', 'Features twisted white threads in a clear or colored base'),
('Lutz', 'Contains goldstone (copper aventurine) flakes'),
('Swirl', 'Features swirling colored bands'),
('Onionskin', 'Layered surface with stretched and folded colors'),
('Mica', 'Contains flecks of mica for sparkle'),
('End of Day', 'Made from leftover glass with multiple colors'),
('Cat\\'s Eye', 'Features vanes radiating from center'),
('Clambroth', 'Opaque with a milky, mottled appearance'),
('Sulphide', 'Contains a figure encased in clear glass'),
('Contemporary Art', 'Modern artistic marbles');

-- Sample artists
INSERT INTO artists (name, bio, website) VALUES
('Unknown', 'Artist information not available', NULL),
('Handmade', 'Various handmade marble artists', NULL);

-- Sample vendors
INSERT INTO vendors (name, location) VALUES
('Local Marble Shop', 'Main Street'),
('Online Marketplace', 'Internet'),
('Marble Convention', 'Various Locations');
""",

    "frontend/package.json": """{
  "name": "marble-collection-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1",
    "axios": "^1.6.0",
    "lucide-react": "^0.263.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "tailwindcss": "^3.3.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.31"
  }
}
""",

    "frontend/tailwind.config.js": """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
""",

    "frontend/src/index.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
""",

    "frontend/src/services/api.js": """import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const marblesAPI = {
  getAll: (filters = {}) => api.get('/marbles', { params: filters }),
  getById: (id) => api.get(`/marbles/${id}`),
  create: (data) => api.post('/marbles', data),
  createBulk: (marbles) => api.post('/marbles/bulk', { marbles }),
  update: (id, data) => api.put(`/marbles/${id}`, data),
  delete: (id) => api.delete(`/marbles/${id}`),
};

export const artistsAPI = {
  getAll: () => api.get('/artists'),
  create: (data) => api.post('/artists', data),
};

export const stylesAPI = {
  getAll: () => api.get('/styles'),
};

export const vendorsAPI = {
  getAll: () => api.get('/vendors'),
  create: (data) => api.post('/vendors', data),
};

export const aiAPI = {
  identifyStyle: (imageData) => api.post('/identify-style', { image: imageData }),
};

export default api;
""",

    ".gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv
*.egg-info/
dist/
build/

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# React
/build
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

# Environment
.env

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Uploads
uploads/*
!uploads/.gitkeep

# Database
*.db
*.sqlite

# Logs
*.log

# OS
.DS_Store
Thumbs.db
""",

    "README.md": """# Art Glass Marble Collection Manager

A comprehensive web application for cataloging and managing art glass marble collections with AI-powered style identification.

## Features

- 📊 Organize marbles by style, artist, size, price, and vendor
- 🤖 AI-powered marble style identification
- 🔍 Advanced search and filtering
- ➕ Single and bulk marble entry
- 👨‍🎨 Artist management
- 💾 MySQL database storage
- 🎨 Modern React frontend with Tailwind CSS
- 🐍 Python Flask backend

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- MySQL 8.0+
- OpenAI API key (for AI features)

### Installation

1. Set up the database:
   ```bash
   mysql -u root -p < database/schema.sql
   mysql -u root -p < database/seed_data.sql
   ```

2. Configure backend:
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env with your credentials
   pip install -r requirements.txt
   ```

3. Start backend:
   ```bash
   python main.py
   ```

4. Configure frontend:
   ```bash
   cd frontend
   npm install
   ```

5. Start frontend:
   ```bash
   npm start
   ```

Visit http://localhost:3000 to use the application.

## Documentation

- [Setup Guide](docs/SETUP.md)
- [API Documentation](docs/API.md)
- [User Guide](docs/USER_GUIDE.md)

## License

MIT License
""",

    "docker-compose.yml": """version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: marble_mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: marble_collection
      MYSQL_USER: marbleuser
      MYSQL_PASSWORD: marblepass
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./database/schema.sql:/docker-entrypoint-initdb.d/1-schema.sql
      - ./database/seed_data.sql:/docker-entrypoint-initdb.d/2-seed.sql

  backend:
    build: ./backend
    container_name: marble_backend
    ports:
      - "5000:5000"
    environment:
      DB_HOST: mysql
      DB_USER: marbleuser
      DB_PASSWORD: marblepass
      DB_NAME: marble_collection
    depends_on:
      - mysql
    volumes:
      - ./backend:/app
      - ./backend/uploads:/app/uploads

  frontend:
    build: ./frontend
    container_name: marble_frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
    volumes:
      - ./frontend:/app
      - /app/node_modules

volumes:
  mysql_data:
"""
}

def main():
    print("=" * 60)
    print("MARBLE COLLECTION MANAGER - PROJECT SETUP")
    print("=" * 60)
    print()
    
    # Create base directory
    os.makedirs(BASE_DIR, exist_ok=True)
    print(f"Base directory: {BASE_DIR}")
    print()
    
    # Create directory structure
    print("Creating directory structure...")
    create_directory_structure(BASE_DIR, PROJECT_STRUCTURE)
    print()
    
    # Write file contents
    print("Writing file contents...")
    for file_path, content in FILES_CONTENT.items():
        write_file(BASE_DIR, file_path, content)
    print()
    
    # Create empty marker files for upload directories
    write_file(BASE_DIR, "backend/uploads/.gitkeep", "")
    
    print("=" * 60)
    print("✅ PROJECT SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Install MySQL and create the database:")
    print(f"   mysql -u root -p < {os.path.join(BASE_DIR, 'database', 'schema.sql')}")
    print()
    print("2. Set up backend:")
    print(f"   cd {os.path.join(BASE_DIR, 'backend')}")
    print("   pip install -r requirements.txt")
    print("   cp .env.example .env")
    print("   # Edit .env with your credentials")
    print("   python main.py")
    print()
    print("3. Set up frontend:")
    print(f"   cd {os.path.join(BASE_DIR, 'frontend')}")
    print("   npm install")
    print("   npm start")
    print()
    print("4. Access the application at http://localhost:3000")
    print()

if __name__ == "__main__":
    main()