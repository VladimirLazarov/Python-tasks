def calculate_total_time(swimming_time, cycling_time, running_time):
    
    # logical error: multiplying instead of adding the times
    return swimming_time * cycling_time * running_time

def determine_award(total_time):
 
    if total_time <= 100:
        return "Provincial Colour"
    elif total_time <= 105:
        return "Provincial Half Colour"
    elif total_time <= 110:
        return "Provincial Scroll"
    else:
        return "No Award"

def main():
    try:
        swimming_time = float(input("Enter swimming time (in minutes): "))
        cycling_time = float(input("Enter cycling time (in minutes): "))
        running_time = float(input("Enter running time (in minutes): "))

        total_time = calculate_total_time(swimming_time, cycling_time, running_time)

        print(f"\nTotal time taken to complete the triathlon: {total_time} minutes")
        award = determine_award(total_time)
        print(f"Award: {award}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values for time.")

if __name__ == "__main__":
    main()