TODO:
- Add process
- Add reflections
- Update requirements.txt

# QuizGonk

A terminal-based quiz application built with Python and Blessed, featuring an interactive text-based interface for testing knowledge across various topics.

The first version of the quiz with terminal inputs is available as V1.0 on GitHub.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Additional Imports](#additional-imports)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Navigation Guide](#navigation-guide)
- [Authors](#authors)
- [Process](#process)
- [Reflections](#reflections)
- [Sources](#sources)

## Features

- **Interactive Terminal UI**: Beautiful Blessed-based interface with ascii-art and key navigation
- **Multiple Quiz Modes**: Choose from specific game categories or take a mixed quiz with random questions
- **Review System**: Review of incorrect answers with correct/incorrect indicators

## Technologies Used

- **Python 3.9+**
- **MySQL**: Database for storing quiz data.
- **PyMySQL**: MySQL connector for Python.
- **python-dotenv**: Environment variable management.
- **Blessed**: Practical library for making terminal apps.

## Additional Imports
- **os(os.environ)**: Used to return a dictionary of environmental variables.
- **pathlib**: Used to access path to reach the .json file.
- **time**: Timer used for a smooth credits screen.
- **string**: Used to access ascii-letters to use for options.

## Prerequisites

Before running this application, make sure you have the following installed:

- **Python 3.9 or higher**
- **MySQL Server** (or access to a MySQL database)
- **Git** (for cloning the repository)
- **uv** (recommended) or **pip** (for package management)

## Installation

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

## Environment Setup

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

## Database Setup

1. **Create the database**:
   - Log into your MySQL shell
   - Run the initialization script:
     ```sql
     SOURCE Database/init.sql
     ```

2. **Import quiz data**:
   - The application includes a script to import games and questions
   - This runs automatically on every startup, importing games from JSON.

## Usage

### Running the Application

```bash
# Using uv (if installed)
uv run python main.py

# Or directly with Python
python main.py
```

## Navigation Guide

- **Main Menu**:
  - Choose from specific games, mixed game, or quit

- **Quiz Mode**:
  - Choose answers using key arrow navigation and enter key
  - Questions advance automatically

- **Results Screen**:
  - View your score and accuracy percentage
  - Choose to review incorrect answers or return to main menu

- **Review Screen**:
  - Use key arrows to loop through wrongly answered questions
  - Your answers are highlighted in red, while correct answers are green
  - Press 'm' to return to main menu
  - Press 'q' or 'x' to quit


## Authors
   Kristiane Olsen  [GitHub](https://github.com/KristianeO)


   Thomas Eikhaugen [GitHub](https://github.com/Eikhaugen)


## Process

### Planning 1:
Before we started, we mapped out the different functions we needed for the game to run:
- init.sql
- import_games.py
- main_menu.py
- quizzer.py
- results.py
- review.py

After writing said codes, we added a view handler to store variables and functions needed for the program to run. We changed the code in the files listed above to implement the view handler. This eliminated the need of using global variables, and made it easier for the functions to reference each other. 

When the game was running smoothly, we checked for bugs and fixed some minor issues.

### Testing 1:
After testing the program many times ourselves, we could not find any bugs.

We had a friend test the quiz, who discovered one error: When choosing a new game after previously finishing one, the game would load out the previous gave. This was a quick fix by reloading all the game data at the start of each game loop.

### Planning 2:
We wanted to implement a library to make the terminal experience more fun. We agreed that Thomas was going to look into the Curses library, while Kristiane was going to look into tkinter as an option.

After lots of research, we decided not to implement tkinter. It was difficult to get the code running properly in the different frames, and we decided that using tkinter was not the best use of our time.

While researching the Curses library, an option occurred: Blessed. It seemed a bit easier to implement, and it runs better on Windows compared to Curses. Thomas had changed the main menu using Blessed, with a great result. We decided to use Blessed, and changed the program to use this library. 

### Testing 2:
-coming soon....

## Reflections
- (Remove) For contributions and reflection each team member should write one
paragraph describing their role in the project.
This should be followed by a second paragraph describing any particular
technical challenges they individually encountered, and how they overcame
them.

### Kristiane:

#### Contributions:
To start, I wrote init.sql to get the basic layout of the database, then import_games.py to load the .json data into the database.
Then I wrote quizzer.py, originally with MySql to load the data from the database. Later this was moved to the view handler, and i rewrote quizzer.py to use the view handler.
I wrote the initial results screen which is seen in version 1.
I made some minor changes in the view handler to work with the code.

When implementing blessed for version 2, I rewrote review.py. I also made some minor changes in the different views for a clean esthetic through the game.
Finally I added a credits screen which is shown before the program quits. 

#### Reflection:
It has been a great learning opportunity for me to work with someone who has programmed a game earlier,
and working on different parts of the same code has been a valuable experience for me.
I have learned to use Git, which has made the process very smooth.

The first challenge was understanding and learning to use the view handler. 
Since the main menu already had been edited to use it before I edited quizzer.py, I used it as a template and as I implemented it quickly understood the logic behind it.

The second challenge was implementing Blessed. Again, the main menu had been edited, so I also used this as a template. 
The logic behind the review screen is a bit different from the main menu, but I figured out through trial and error how to best use it.

Otherwise, in general another challenge has been iteration. 
A lot of my code has iterations through multiple for loops, but this was also solved through trial and error.

### Thomas:

## Sources
[Stack Overflow - Share Streamlit can't find pkl file](https://stackoverflow.com/questions/69768380/share-streamlit-cant-find-pkl-file)
[Stack Overflow - Enumerate with letters instead of numbers [duplicate]](https://stackoverflow.com/questions/63875471/enumerate-with-letters-instead-of-numbers)
