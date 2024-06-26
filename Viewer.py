import urllib.request
import random
import time


class Viewer:
    """
    Simple page viewer class with 'urllib.request' module.
    # Features: save the page

    This class provides functionality to fetch and display the content of a web page.
    It can handle both HTTP and HTTPS protocols.
    """

    def __init__(self, url: str = 'www.example.com', secure: bool = False):
        """
        Initializes the Viewer instance with a URL and protocol type.

        :param url: The web service address (default is 'www.example.com').
        :param secure: A boolean indicating whether to use HTTPS (True) or HTTP (False) (default is False).
        """
        self.url = url
        self.secure = secure
        self.user_agent = self._generate_user_agent()
    
    @property
    def version(self):
        """
        Return the version of the Viewer.

        :return: A string representing the version.
        """
        return "v1.0"

    @staticmethod
    def _generate_user_agent() -> str:
        """
        Generates a random User-Agent string for the request.

        :return: The generated User-Agent string.
        """
        browsers = ['chrome', 'firefox', 'ie', 'safari']
        browser = random.choice(browsers)
        versions = {
            'chrome': ['91.0.4472.124', '90.0.4430.93', '89.0.4389.82', '88.0.4324.150'],
            'firefox': ['89.0', '88.0', '87.0', '86.0', '85.0'],
            'ie': ['11.0', '10.0', '9.0'],
            'safari': ['14.0.3', '14.0', '13.1']
        }
        os_types = ['windows', 'mac', 'linux']
        os_type = random.choice(os_types)

        if browser in versions:
            version = random.choice(versions[browser])
        else:
            version = random.choice(list(versions.values())[0])

        if browser == 'chrome':
            return f"Mozilla/5.0 ({os_type}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36"
        elif browser == 'firefox':
            return f"Mozilla/5.0 ({os_type}; rv:{version}) Gecko/20100101 Firefox/{version}"
        elif browser == 'ie':
            return f"Mozilla/5.0 (Windows NT {os_type}; Win64; x64; Trident/7.0; rv:{version}.0) like Gecko"
        elif browser == 'safari':
            return f"Mozilla/5.0 ({os_type}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{version} Safari/537.36"
        else:
            return f"Mozilla/5.0 ({os_type}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36"

    @staticmethod
    def _make_request(url: str, user_agent: str) -> str:
        """
        Makes an HTTP request to fetch the content of the web page.

        :param url: The URL of the web page.
        :param user_agent: The User-Agent string to use for the request.
        :return: The content of the web page as a string.
        """
        try:
            # Construct the request with headers
            request = urllib.request.Request(url, headers={'User-Agent': user_agent})

            # Open the URL and read the response
            with urllib.request.urlopen(request) as response:
                # Read the response data and decode it to a string
                page_content = response.read().decode("utf-8")
                return page_content[:500]  # Return first 500 characters of the page content for preview

        except Exception as e:
            # Handle URL errors
            print("Error:", e, sep='\n')  # Print in console
            return f"Error: {e}"  # return Exception

    def view_page(self) -> str:
        """
        Fetches and displays the content of the web page specified in the URL.

        Constructs the URL using the specified protocol (HTTP or HTTPS), sets a custom User-Agent,
        and returns the first 500 characters of the fetched page content.

        :return: The content of the web page as a string or an error message.
        """
        protocol = "https" if self.secure else "http"  # 'http://' or 'https://'
        full_url = f"{protocol}://{self.url}"

        # Make the HTTP request with the generated User-Agent
        page_preview = self._make_request(full_url, self.user_agent)
        return page_preview

    def view_pages(self, views: int, delay: int, verbose=True) -> list:
        """
        Fetches and displays multiple pages with a delay between each view.

        :param views: Number of pages to view.
        :param delay: Delay (in seconds) between each page view.
        :param verbose: If True, print each page's content to console.
        :return: List of page content strings or error messages.
        """
        pages = []  # Storage
        for i in range(views):
            # Fetch the page content
            page_content = self.view_page()
            pages.append(page_content)

            # Print page content if verbose is True
            if verbose:
                print(f"[{i + 1}:] {page_content}")

            # Introduce a delay between each page view
            time.sleep(delay)

        return pages
