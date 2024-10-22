# Function to display the main menu
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

# Function to get user input and return a list of floats
def get_user_input():
    user_input = input()  # Read input from user
    input_list = user_input.split(",")  # Split input string by commas
    float_list = [float(num) for num in input_list]  # Convert strings to floats
    return float_list

# Function to calculate average temperature
def calc_average_temperature(temp_list):
    return sum(temp_list) / len(temp_list)  # Calculate and return average

# Function to find minimum and maximum temperature
def calc_min_max_temperature(temp_list):
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    return [min_temp, max_temp]  # Return min and max as a list

# Function to calculate the median temperature
def calc_median_temperature(temp_list):
    sorted_list = sorted(temp_list)  # Sort the list
    n = len(sorted_list)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2  # Even number of elements
    else:
        return sorted_list[mid]  # Odd number of elements

# Main function
def main():
    display_main_menu()  # Show the prompt
    temp_list = get_user_input()  # Get the list of temperatures from the user
    
    # Calculate average, min, max, and median
    average = calc_average_temperature(temp_list)
    print(f"Average Temperature: {average:.2f}")
    
    min_max = calc_min_max_temperature(temp_list)
    print(f"Min Temperature: {min_max[0]:.2f}, Max Temperature: {min_max[1]:.2f}")
    
    median = calc_median_temperature(temp_list)
    print(f"Median Temperature: {median:.2f}")

if __name__ == "__main__":
    main()
