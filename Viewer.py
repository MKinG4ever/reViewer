import urllib.request


def viewer(url='www.example.com', secure=False):
    """
    Simple page viewer function
    # Feature: save the page

    :param url: the web service address
    :param secure: whether to use https or http
    """

    # URL to fetch data from
    _url = f"http://{url}" if not secure else f"https://{url}"

    # Define a custom User-Agent string
    user_agent = "Custom-User-Agent"

    # Create a request object with the custom User-Agent header
    request = urllib.request.Request(_url, headers={'User-Agent': user_agent})

    # page
    page = str()

    try:
        # Open the URL and read the response
        with urllib.request.urlopen(request) as response:

            # Read the response data
            page = response.read().decode("utf-8")
            print(page[:100], '...')

    except Exception as e:
        # Handle URL errors
        print("Error:", e, sep='\n')
