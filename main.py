import requests
import time
import datetime

def print_colored_timestamp():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\033[34m[{now}]\033[0m")

def make_get_requests(user_ids, bearer_tokens):
    print_colored_timestamp()

    pass

    if len(user_ids) != len(bearer_tokens):
        print("Error: The number of user_ids does not match the number of bearer tokens.")
        return

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,es;q=0.9',
        'Authorization': '',  # Will be set dynamically for each request
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'api.securitylabs.xyz',
        'Origin': 'https://node.securitylabs.xyz',
        'Pragma': 'no-cache',
        'Referer': 'https://node.securitylabs.xyz/',
        'Sec-CH-UA': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    for user_id, token in zip(user_ids, bearer_tokens):
        headers['Authorization'] = f'Bearer {token}'  # Set the bearer token dynamically
        try:
            endpoint = f"https://api.securitylabs.xyz/v1/users/earn/{user_id}"
            response = requests.get(endpoint, headers=headers)

            # Assuming the response is JSON
            data = response.json()

            print(f"\nProcessing User ID: {user_id}")

            # Check if the response contains error information
            if 'statusCode' in data and data['statusCode'] == 400:
                print(f"Error message: {data['message']}")
            else:
                # Handle success response
                print(f"Tokens to award: {data.get('tokensToAward', 'N/A')}")
                print(f"Dip Init Mine Time: {data.get('dipInitMineTime', 'N/A')}")
                print(f"Dip Init Mine Amount: {data.get('dipInitMineAmount', 'N/A')}")
                print(f"Dip Init Referred Count: {data.get('dipInitReferredCount', 'N/A')}")

        except requests.exceptions.RequestException as e:
            print(f"Error for endpoint: {endpoint}")
            print(f"Exception: {e}")

# Example usage
user_ids = [
    "user_id_1",
    "user_id_2"
]

bearer_tokens = [
    "bearer_token_1",
    "bearer_token_2"
]

while True:
    make_get_requests(user_ids, bearer_tokens)
    time.sleep(43200)  # Wait for 12 hours (43200 seconds)
