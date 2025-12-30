# Personal Information Manager - Week 1 Internship Project

##  Project Description

Personal Information Manager is a beginner-friendly Python program designed to demonstrate fundamental programming concepts. The application collects personal information from users, stores both static and dynamic data, performs calculations, and displays formatted output.

### Purpose
This project teaches:
- **Variables and Data Types**: Storing different types of information
- **User Input/Output**: Interacting with users via console
- **Input Validation**: Ensuring data quality with loops
- **String Formatting**: Using f-strings for professional output
- **Basic Calculations**: Converting years to months
- **Control Flow**: Using while loops for validation

---

## Features

 **Static Information Storage**: Name, age, city, and hobby are predefined
 **Dynamic User Input**: Collects favorite food and favorite color from user
 **Input Validation**: Uses while loops to ensure no empty inputs
 **Age Calculation**: Converts age from years to months
 **Professional Formatting**: Uses f-strings and separators for clean output
 **String Methods**: Capitalizes user input with `.title()` method
 **Welcome & Goodbye Messages**: Program starts and ends with friendly messages
 **Error Handling**: Re-prompts user if input is invalid (empty)

---

##  How to Run the Program

### Prerequisites
- Python 3.x installed on your system
- VS Code or any Python IDE

### Steps to Execute

1. **Navigate to the project directory**
   ```bash
   cd week1-personal-info
   ```

2. **Run the program**
   ```bash
   python personal_info.py
   ```

3. **Follow the prompts**
   - Enter your favorite food when asked
   - Enter your favorite color when asked
   - View your complete information profile

---

##  Sample Output

```
============================================================
  WELCOME TO PERSONAL INFORMATION MANAGER
============================================================

What is your favorite food? Pizza
What is your favorite color? Blue

============================================================
  YOUR PERSONAL INFORMATION PROFILE
============================================================

 Name:              Alex Johnson
 Age:               22 years (264 months)
  City:              New York
 Hobby:             Photography

------------------------------------------------------------

  Favorite Food:     Pizza

 Favorite Color:    Blue

------------------------------------------------------------
 SUMMARY 
------------------------------------------------------------
Name: Alex Johnson
Lives in: New York
Personal Interest: Photography
Loves eating: Pizza
Prefers color: Blue
Current Age: 22 years (approximately 264 months)
------------------------------------------------------------

============================================================
  THANK YOU FOR USING PERSONAL INFORMATION MANAGER!
  GOODBYE! 
============================================================
```

---

##  What I Learned

### 1. **Variables and Data Types**
   - Storing strings (text), integers (numbers)
   - Understanding variable naming conventions

### 2. **Input and Output**
   - Using `input()` to collect user data
   - Using `print()` to display information
   - `.strip()` method to remove extra whitespace

### 3. **Input Validation**
   - While loops to validate user input
   - Conditional statements (if/else)
   - Re-prompting users for correct input

### 4. **String Formatting**
   - F-strings for dynamic text insertion
   - `.title()` method to capitalize words
   - Creating formatted displays with separators

### 5. **Basic Arithmetic**
   - Simple multiplication (age × 12 = months)
   - Understanding real-world calculations

### 6. **User Experience**
   - Welcome and goodbye messages
   - Clear visual separators for readability
   - Emoji use for better presentation
   - Error messages for invalid input

---

## 🎓 Code Explanation

### Section 1: Static Information
```python
name = "Alex Johnson"
age = 22
```
Variables that contain predefined information about a person.

### Section 2: User Input with Validation
```python
while True:
    favorite_food = input("What is your favorite food? ").strip()
    if favorite_food:
        break
    print(" Please enter a valid food name (cannot be empty).\n")
```
Uses a while loop to keep asking until the user provides non-empty input.

### Section 3: Age Calculation
```python
age_in_months = age * 12
```
Simple multiplication to convert years to months.

### Section 4: Formatted Output
```python
print(f" Name:              {name}")
```
F-strings allow embedding variables directly in text.

---

##  Challenges & Solutions

### Challenge 1: Handling Empty Input
**Problem**: User might press Enter without typing anything
**Solution**: Used `while True` loop with `.strip()` to remove whitespace and validation

### Challenge 2: Maintaining User Experience
**Problem**: Raw output looks unprofessional
**Solution**: Added separators, emojis, and formatted headers for better readability

### Challenge 3: Case Sensitivity of User Input
**Problem**: User might enter "pizza" or "PIZZA"
**Solution**: Used `.title()` method to standardize capitalization

### Challenge 4: Calculating Age in Months
**Problem**: Need to convert user age to months
**Solution**: Simple arithmetic multiplication (age * 12)

---

##  Project Structure

```
week1-personal-info/
│── personal_info.py       # Main program
│── README.md              # Project documentation
│── test_inputs.txt        # Sample test inputs
└── .gitignore             # Git ignore file
```

---

##  Testing

Test the program with the inputs from `test_inputs.txt`:

1. Run the program
2. When prompted for "favorite food", enter: `Pizza`
3. When prompted for "favorite color", enter: `Blue`
4. Verify the output matches the Sample Output section

---

##  Internship Takeaways

This Week 1 project successfully demonstrates:
-  Basic Python syntax and structure
-  Variable declaration and usage
-  User interaction through console I/O
-  Input validation patterns
-  String manipulation and formatting
-  Basic arithmetic operations
-  Control flow with loops and conditionals
-  Professional code documentation

---

**Created**: Week 1 of Python Internship  
**Level**: Beginner  
**Duration**: Single session  
**Status**:  Complete
