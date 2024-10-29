import requests


def get_user_data(user_id):
    # Define the API endpoint
    base_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Make a GET request to the API
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Display the user's name, email, and address
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Address: {data['address']['street']}, {data['address']['city']}")
    else:
        # Handle errors
        print("Error:", response.status_code, response.text)


# Prompt the user for a user ID
user_id = input("Enter a user ID (1-10): ")
get_user_data(user_id)
