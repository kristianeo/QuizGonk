# 🧠 QuizGonk

A terminal-based quiz application built with Python and curses, featuring an interactive text-based interface for testing knowledge across various topics.

## 📚 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## ✨ Features

- **Interactive Terminal UI**: Beautiful curses-based interface with box drawings and arrow key navigation
- **Multiple Quiz Modes**: Choose from specific game categories or take a mixed quiz with random questions
- **Review System**: Detailed review of incorrect answers with correct/incorrect indicators

## 🛠️ Technologies Used

- **Python 3.9+**
- **MySQL**: Database for storing quiz data
- **PyMySQL**: MySQL connector for Python
- **python-dotenv**: Environment variable management

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- **Python 3.9 or higher**
- **MySQL Server** (or access to a MySQL database)
- **Git** (for cloning the repository)
- **uv** (recommended) or **pip** (for package management)

## 📦 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kristianeo/QuizGonk.git
   cd QuizGonk
   ```

2. **Install Python Dependencies**:

   Choose one of the following methods:

   **With uv (recommended)**:
   ```bash
   uv pip install -r requirements.txt
   ```

   **With pip**:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Environment Setup

1. **Copy the environment template**:
   ```bash
   cp .env.example .env
   ```

2. **Configure your database credentials in `.env`**:
   ```env
   DB_ADDRESS=localhost
   PYTHON_DB_USER=your_mysql_username
   PYTHON_USER_PASSWORD=your_mysql_password
   DB_NAME=QuizzerQuestions
   ```

## 🗄️ Database Setup

1. **Create the database**:
   - Log into your MySQL shell
   - Run the initialization script:
     ```sql
     SOURCE Database/init.sql
     ```

2. **Import quiz data** (optional):
   - The application includes a script to import games and questions
   - This runs automatically on first startup

## 🚀 Usage

### Running the Application

```bash
# Using uv (if installed)
uv run python main.py

# Or directly with Python
python main.py
```

### Navigation Guide

- **Main Menu**:
  - Use ↑/↓ arrow keys to select quiz options
  - Press Enter to confirm selection
  - Choose from specific games, mixed quiz, or quit

- **Quiz Mode**:
  - Use ↑/↓ arrows to highlight answer choices
  - Press Enter to submit your answer
  - Questions advance automatically

- **Results Screen**:
  - View your score and accuracy percentage
  - Choose to review incorrect answers or return to main menu

- **Review Screen**:
  - Press 'n' for next question, 'p' for previous
  - Press 'm' to return to main menu
  - Correct answers are marked with "<--- Correct"
  - Your answers are marked with "<--- You answered"


## 📁 Project Structure

```
QuizGonk/
├── main.py                 # Application entry point
├── view_handler.py         # Main application logic and state management
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .env.example           # Environment template
├── Database/
│   ├── init.sql           # Database schema
│   ├── import_games.py    # Data import script
│   └── questions.json     # Quiz data (optional)
└── Views/
    ├── main_menu.py       # Main menu interface
    ├── quizzer.py         # Quiz gameplay logic
    ├── results.py         # Results display
    └── review.py          # Answer review system
```


---

**Authors**: Kristiane & Thomas

**Sources**: [Stack Overflow - Share Streamlit can't find pkl file](https://stackoverflow.com/questions/69768380/share-streamlit-cant-find-pkl-file)
