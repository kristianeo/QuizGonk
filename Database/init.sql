DROP DATABASE IF EXISTS QuizzerQuestions;
CREATE DATABASE QuizzerQuestions;

use QuizzerQuestions;

CREATE TABLE games (
    gameID INT PRIMARY KEY AUTO_INCREMENT
);

-- question table, where correct_answer correlates to index of the correct answer in questions.json.
CREATE TABLE questions (
    questionID  INT AUTO_INCREMENT,
    gameID INT NOT NULL,
    question NVARCHAR(255),
    correct_answer INT NOT NULL,
    PRIMARY KEY (questionID),
    FOREIGN KEY (gameID) REFERENCES games (gameID)
);

CREATE TABLE options (
    optionsID INT AUTO_INCREMENT,
    questionID INTEGER NOT NULL,
    option_text VARCHAR(255),
    option_index INT NOT NULL,
    PRIMARY KEY (optionsID),
    FOREIGN KEY (questionID) REFERENCES questions(questionID)
);