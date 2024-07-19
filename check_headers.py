#!/usr/bin/env python3

import argparse
import requests
import json

def check_headers(url, headers):
    try:
        response = requests.get(url)
        response_headers = response.headers
        results = {header: (header in response_headers) for header in headers}
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return {}

def check_multiple_urls(urls_file, headers_file, output_file):
    try:
        with open(urls_file, 'r') as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]

        with open(headers_file, 'r') as f:
            headers = [line.strip() for line in f.readlines() if line.strip()]

        results = {}
        for url in urls:
            results[url] = check_headers(url, headers)

        if output_file:
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=4)
                print(f"Results saved to {output_file}")

        print("\nResults:")
        for url, result in results.items():
            print(f"- {url}:")
            for header, present in result.items():
                status = "Present" if present else "Missing"
                print(f"  - {header}: {status}")

    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Security Header Checker Tool")
    parser.add_argument("--urls-file", required=True, help="Path to the file containing URLs")
    parser.add_argument("--headers-file", required=True, help="Path to the file containing headers")
    parser.add_argument("--output-file", help="Path to save the output JSON file")
    args = parser.parse_args()

    check_multiple_urls(args.urls_file, args.headers_file, args.output_file)

if __name__ == "__main__":
    main()
