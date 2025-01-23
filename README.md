# Game Review CLI Application

A command-line interface application for managing and browsing video game reviews. This application allows users to browse games, manage reviews, and track their gaming experiences.

## Features

- Browse games alphabetically
- View games by genre
- Sort games by average rating
- Browse reviews by genre
- Manage game reviews
- Full CRUD operations for games and reviews

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd rarcli
```

2. Set up a Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install pipenv
pipenv install
```

## Requirements

- Python 3.8.13
- Dependencies:
  - ipdb
  - faker
  - pytest (7.1.3)

## Usage

1. Activate your virtual environment:
```bash
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

2. Run the application:
```bash
python lib/cli.py
```

3. Use the interactive menu to:
   - Browse games and reviews
   - Manage your game library
   - Add, update, or delete reviews
   - View game statistics

## Database Schema

The application uses SQLite to store game and review data with the following structure:

### Games
- id (Primary Key)
- title
- year
- genre
- multiplayer
- description

### Reviews
- Connected to games through relationships
- Stores user reviews and ratings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

