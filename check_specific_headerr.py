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
    header_name = "Referrer-Policy"  # Specify the header to check
    with open("urls.txt", "r") as file:
        urls = [line.strip() for line in file.readlines() if line.strip()]

    check_specific_header(urls, header_name)
