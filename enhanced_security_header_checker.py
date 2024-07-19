import requests
import argparse

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # Implement logic to check specific security headers
        # Example: Check for Referrer-Policy header
        if 'Referrer-Policy' in headers:
            return "Referrer-Policy header is present."
        else:
            return "Referrer-Policy header is missing."

        # Implement checks for other security headers...

    except requests.exceptions.RequestException as e:
        return f"Error accessing {url}: {e}"

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Enhanced Security Header Checker Tool")
    parser.add_argument("url", help="URL to check for security headers")
    parser.add_argument("--output-file", help="Path to save the output file")
    args = parser.parse_args()

    # Perform security header checks
    result = check_security_headers(args.url)

    if args.output_file:
        # Write result to output file
        with open(args.output_file, "w") as output_file:
            output_file.write(result)
            print(f"Results saved to: {args.output_file}")
    else:
        # Print result to console
        print(result)

if __name__ == "__main__":
    main()
