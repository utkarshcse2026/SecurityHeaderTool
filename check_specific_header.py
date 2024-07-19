import requests

def check_specific_header(urls, header_name):
    for url in urls:
        try:
            response = requests.get(url)
            headers = response.headers

            if header_name in headers:
                print(f"{url}: {header_name} header is present")
            else:
                print(f"{url}: {header_name} header is missing")

        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

# Main function to test the tool
if __name__ == "__main__":
    # Accept input from the user
    header_name = input("Enter the header name to check (e.g., Referrer-Policy): ")
    urls_input = input("Enter URLs separated by spaces: ")

    # Split input URLs into a list
    urls = urls_input.split()

    # Call the function to check the specified header for each URL
    check_specific_header(urls, header_name)
