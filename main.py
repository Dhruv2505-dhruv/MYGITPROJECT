# main.py
import helper

def main():
    birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
    try:
        days_left = helper.days_until_birthday(birthday_str)
        print(f"Your birthday is in {days_left} days!")
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()