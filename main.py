from Viewer import viewer


def main():
    # Visual input
    url = input('Enter URL (Ex: www.google.com): ')
    views = int(input('How many views: '))

    # Number of page/site views
    for i in range(views):
        # Representation
        print(f"[{i + 1}]: ", end='')
        viewer(url, secure=False)


if __name__ == '__main__':
    main()
