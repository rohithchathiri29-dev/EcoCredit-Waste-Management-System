# EcoCredit-Waste-Management-System
Python-based waste management system developed for CS50P. Features include secure login, password validation, waste deposit tracking, EcoCredit calculation, CSV file handling, exception handling, and pytest testing for important functions.
#### Video Demo: https://youtu.be/XhTIgKryrLU?si=1IVzy6ydWPMKSnoF

#### Description:

EcoCredit Waste Management System is a Python-based terminal application developed as my final project for CS50’s Introduction to Programming with Python.

The main purpose of this project is to encourage proper waste disposal and recycling by rewarding users with EcoCredits based on the type and weight of waste they deposit.

This project was inspired by real-world waste management problems and the idea of creating a simple recycling reward system that motivates people to dispose of waste responsibly.

The application allows users to create an account, log in securely, deposit waste materials, and check their EcoCredit balance.

The entire project is terminal-based and developed using Python. User information and waste details are stored using CSV files. The system includes secure account creation with password validation using regular expressions. Passwords must contain uppercase letters, lowercase letters, numbers, and special characters to improve security.

After logging in, users can:

- Deposit waste
- Earn EcoCredits
- Check their credit balance
- Log out of the system

The waste deposit feature is the core functionality of the project. Waste data is stored in `waste_data.csv`, which contains waste item codes, waste names, and credit values.

The user enters the waste item code and the weight of the waste material in grams. The program then calculates the total credits earned and updates the user’s balance in `users.csv`.

Credits are calculated using:

Credits = Weight × Credit Per Gram

The project also includes several validation and security features such as:

- Empty input checking
- Positive weight validation
- Maximum deposit limit of 3kg per item
- Three login attempts
- Exception handling for invalid files and inputs

## Files in the Project

```text
EcoCredit/
│
├── project.py
├── test_project.py
├── users.csv
├── README.md
├── requirements.txt
│
└── data/
    └── waste_data.csv
```

- `project.py` contains the main application code.
- `test_project.py` contains pytest test functions.
- `users.csv` stores usernames, passwords, and EcoCredit balances.
- `waste_data.csv` stores waste item information and credit values.
- `requirements.txt` contains the required libraries for the project.

## Design Choices

Initially, I planned to use separate files for different waste categories. Later, I combined all waste data into a single CSV file to make the system simpler and easier to manage.

I chose a terminal-based interface instead of a graphical user interface because it allowed me to focus more on Python programming concepts and application logic.

I used CSV files instead of databases because the project is designed for learning purposes and does not require a complex database system.

Exception handling and input validation were added to improve reliability and prevent the program from crashing due to invalid inputs or missing files.

## What I Learned

While building this project, I improved my understanding of:

- Python programming
- Functions and modular programming
- File handling using CSV files
- Regular expressions
- Exception handling
- Testing using pytest
- Menu-driven applications

This project also helped me understand how programming can be used to solve real-world environmental problems.

## Author

Rohith Chathiri
