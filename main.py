from Viewer import Viewer


def main():
    """
    Main function
    Timestamp 1719490798.5711012
    Version 1.1

    :return:
    """
    # Visual input
    _url = quest('Enter URL', 'www.google.com')
    _secure = eval(quest('Do you require HTTPS', True))
    _views = int(quest('How many views', 5))
    _delay = int(quest('Delay between views in seconds: ', 60))

    # Create a Viewer instance for 'www.google.com' using HTTPS
    site = Viewer(url=_url, secure=_secure)

    # Presentation
    print('\n', site, 'Initiation...', sep='\n')

    # View 4 pages with a delay of 1 second between each view, and print each page content
    pages_https = site.view_pages(views=_views, delay=_delay, verbose=True)


def quest(question: str, answer):
    a = input(f"{question} (Default: {answer}): ")
    return a if a.strip() else answer


if __name__ == '__main__':
    main()
