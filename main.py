# ============================================================================
# PROJECT: Personal Information Manager
# AUTHOR: Python Internship Developer
# DESCRIPTION: A beginner-friendly program to collect, store, and display
#              personal information with validation and age calculation
# ============================================================================

# Import sys module to handle Unicode encoding on Windows
import sys
import io

# Fix Unicode encoding for Windows terminal
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Display Welcome Message
print("\n" + "="*60)
print("  WELCOME TO PERSONAL INFORMATION MANAGER".center(60))
print("="*60 + "\n")

# ============================================================================
# SECTION 1: STATIC PERSONAL INFORMATION
# ============================================================================
# These are hardcoded values that don't change during program execution
name = "Alex Johnson"
age = 22
city = "New York"
hobby = "Photography"

# ============================================================================
# SECTION 2: COLLECT USER INPUT WITH VALIDATION
# ============================================================================
# These variables will store user input with validation for empty strings

# Get favorite food from user (keep asking until non-empty input)
while True:
    favorite_food = input("What is your favorite food? ").strip()
    if favorite_food:  # Check if input is not empty
        break
    print(" Please enter a valid food name (cannot be empty).\n")

# Get favorite color from user (keep asking until non-empty input)
while True:
    favorite_color = input("What is your favorite color? ").strip()
    if favorite_color:  # Check if input is not empty
        break
    print(" Please enter a valid color (cannot be empty).\n")

# ============================================================================
# SECTION 3: CALCULATE AGE IN MONTHS
# ============================================================================
# Convert age from years to months by multiplying by 12
age_in_months = age * 12

# ============================================================================
# SECTION 4: DISPLAY ALL INFORMATION WITH FORMATTING
# ============================================================================
# Use f-strings to format the output nicely with separators

print("\n" + "="*60)
print("  YOUR PERSONAL INFORMATION PROFILE".center(60))
print("="*60 + "\n")

# Display static information
print(f" Name:              {name}")
print(f" Age:               {age} years ({age_in_months} months)")
print(f"  City:              {city}")
print(f" Hobby:             {hobby}")

print("\n" + "-"*60 + "\n")

# Display user-provided information
print(f"  Favorite Food:     {favorite_food.title()}")
print(f" Favorite Color:    {favorite_color.title()}")

# ============================================================================
# SECTION 5: SUMMARY DISPLAY
# ============================================================================
# Create a formatted summary string using f-strings

summary = f"""
{'-'*60}
 SUMMARY 
{'-'*60}
Name: {name}
Lives in: {city}
Personal Interest: {hobby}
Loves eating: {favorite_food}
Prefers color: {favorite_color}
Current Age: {age} years (approximately {age_in_months} months)
{'-'*60}
"""

print(summary)

# ============================================================================
# SECTION 6: GOODBYE MESSAGE
# ============================================================================
print("="*60)
print("  THANK YOU FOR USING PERSONAL INFORMATION MANAGER!".center(60))
print("  GOODBYE! 👋".center(60))
print("="*60 + "\n")
