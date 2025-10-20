# Art Glass Marble Collection Manager

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
