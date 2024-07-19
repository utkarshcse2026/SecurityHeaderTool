import requests

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        required_headers = [
            'Content-Security-Policy',
            'X-XSS-Protection',
            'Strict-Transport-Security',
            'X-Frame-Options',
            'X-Content-Type-Options',
            'Referrer-Policy'
        ]

        missing_headers = []
        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)

        if missing_headers:
            print("Security headers missing or misconfigured:")
            for header in missing_headers:
                print(f"- {header}")
        else:
            print("All required security headers are present and correctly configured.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Main function to test the tool
if __name__ == "__main__":
    target_url = input("Enter the URL to test: ")
    check_security_headers(target_url)
