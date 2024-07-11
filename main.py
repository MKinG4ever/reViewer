from Viewer import Viewer


def main():
    """
    Main function
    Timestamp 1719490798.5711012
    Version 1.2

    :return:
    """
    # Visual input
    _url = quest('Enter full URL', 'https://www.google.com')
    _views = int(quest('How many views', 15))
    _delay = int(quest('Delay between views in seconds: ', 60))

    # Create a Viewer instance for 'www.google.com' using HTTPS
    site = Viewer(url=_url)

    # Presentation
    print('\n', site, '[:] Initiation...\n', sep='\n')

    # View 4 pages with a delay of 1 second between each view, and print each page content
    pages_https = site.view_pages(views=_views, delay=_delay, verbose=True)


def quest(question: str, answer):
    a = input(f"{question} (Default: {answer}): ")
    return a if a.strip() else answer


if __name__ == '__main__':
    main()
