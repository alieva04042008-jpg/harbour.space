"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"


def main() -> None:
    # TODO: implement GET request and print HTML response
    response = requests.get(URL, verify = False)
    response.raise_for_status()
    print(response.status_code, response.headers["Content-Type"], response.text, end = "\n")
    if "text/html" in response.headers["Content-Type"]:
        return "Content type is text/html"
    else:
        return "Unexpected content type"
    

if __name__ == "__main__":
    main()
