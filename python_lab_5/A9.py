season= {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Summer', 5: 'Summer', 6: 'Summer',
    7: 'Monsoon', 8: 'Monsoon', 9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

# Function to get the season based on the month number
def month(month_number):
    if 1 <= month_number <= 12:
        return season[month_number]
    else:
        return "Invalid month number"

# Example usage
month_number = int(input("Enter the month number (1-12): "))
season = month(month_number)
print(f"month {month_number} is {season}.")
