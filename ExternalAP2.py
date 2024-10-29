import requests
# Define the base URL of the AP
base_url = "https://jsonplaceholder.typicode.com"
# Function to get a list of users from the API
def get_users():
    response = requests.get(f"{base_url}/users")
    if response.status_code == 200:
        users = response.json()
        return users
    else:
        return None
# Call the function to get the list of users
users = get_users()
if users:
    for user in users:
      print(f"User ID: {user['id']}")
      print(f"Name: {user['name']}")
      print(f"Email: {user['email']}")
      print("\n")
else:
    print("Failed to retrieve user data from the API.")
