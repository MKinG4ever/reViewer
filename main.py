from Viewer import Viewer


def main():
    # Visual input
    _url = input('Enter URL (Ex: www.google.com): ')
    _views = int(input('How many views: '))
    _delay = 2  # seconds

    # Create a Viewer instance for 'www.google.com' using HTTPS
    site = Viewer(url=_url, secure=True)

    # View 4 pages with a delay of 1 second between each view, and print each page content
    pages_https = site.view_pages(views=_views, delay=_delay, verbose=True)


if __name__ == '__main__':
    main()
