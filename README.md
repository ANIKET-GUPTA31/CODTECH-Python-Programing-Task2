# CODTECH-Python-Programing-Task2
# Student Grade Tracker

ID :-CT08DS5359,  
DOMAIN:- PYTHON PROGRAMMING,     
DURATION :- JULY TO AUGUST 2024

## Overview

The **Student Grade Tracker** is a Python application designed to manage student grades efficiently. It allows users to add grades for different subjects, calculate average grades, convert averages to letter grades, and compute the GPA. The application provides a user-friendly interface to interact with these functionalities.

## Features

- **Add Grades**: Input grades for multiple subjects.
- **Display Grades**: View grades by subject.
- **Display Summary**: Calculate and display the overall average grade, letter grade, and GPA.
- **Error Handling**: Validate input to ensure grades are between 0 and 100.

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/student-grade-tracker.git
   cd student-grade-tracker
   ```

2. **Run the Application**:
   ```sh
   python grade_tracker.py
   ```

3. **Interact with the Application**:
   - **Add Grade**: Select option `1` and input subject names and grades.
   - **Display Grades**: Select option `2` to view grades by subject.
   - **Display Summary**: Select option `3` to view the overall average grade, letter grade, and GPA.
   - **Exit**: Select option `4` to exit the program.

## Code Explanation

- **GradeManager Class**:
  - `add_grade(subject, grade)`: Adds a grade for a given subject.
  - `calculate_average()`: Calculates the average of all grades.
  - `get_letter_grade(average)`: Converts the average grade to a letter grade.
  - `get_gpa(average)`: Converts the average grade to a GPA.
  - `display_grades()`: Displays grades by subject.
  - `display_summary()`: Displays overall average grade, letter grade, and GPA.

- **Main Function**:
  - Provides a menu-driven interface for users to interact with the `GradeManager` class.

## Example

```plaintext
Menu:
1. Add Grade
2. Display Grades
3. Display Summary
4. Exit
Enter your choice: 1
How many subjects do you have: 2
Enter subject name 1: Mathematics
Enter grade (0-100): 85
Enter subject name 2: Science
Enter grade (0-100): 92
```

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

CODTECH PYTHON PROGRAMING TASK1 (STUDENT GRADE TRACKER)
