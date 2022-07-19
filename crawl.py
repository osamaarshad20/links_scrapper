"""Links scrapper module."""

# region imports
import requests
import argparse
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import time
import threading
# endregion imports


class LinkScrapper():
    """Links scrapper class.
    """

    def __init__(self, url, number_of_threads):
        """Class constructor.

        Args:
            url (_type_): _description_
            number_of_threads (_type_): _description_
        """
        self.url = url
        self.url = 'https://stackoverflow.com/questions/15155476/check-if-url-that-belongs-to-the-same-domain-exists-in-list-with-python'
        self.links = [self.url]
        self.domain = None
        self.number_of_threads = number_of_threads

    def __remove_duplicates(self, links_list, idx):
        """Function to remove duplicates and unURL string

        Args:
            links_list (list:strings): list of links to check.
        """
        st = time.time()
        for item in links_list:
            match = re.search("(?P<url>https?://[^\s]+)", item)
            if match is not None and urlparse(match.group("url")).netloc == self.domain and match.group("url") not in self.links:
                print(f'{(match.group("url"))}')
                self.links.append((match.group("url")))

    def __chunkify(self, lst, n):
        return [lst[i::n] for i in range(n)]

    def driver_code(self):
        """Driver function.
        """
        # Make a GET request to fetch the raw HTML content
        self.domain = urlparse(self.url).netloc
        try:
            for idx, link in enumerate(self.links):
                temp = []
                html_content = requests.get(link)
                # Parse the html content
                soup = BeautifulSoup(html_content.content, 'html.parser')
                for link in soup.find_all('a', href=True):
                    temp.append(str(link.get('href')))

                list_of_chunks = self.__chunkify(temp, self.number_of_threads)
                threads = list()
                for idx, chunk in enumerate(list_of_chunks):
                    threads.append(
                        threading.Thread(target=self.__remove_duplicates, args=(), kwargs={
                            'links_list': chunk, 'idx': idx
                        }))
                # Start all threads
                for thread in threads:
                    thread.start()
                # Join all thread and wait until all completed
                for thread in threads:
                    thread.join()

        except Exception as e:
            print(f'Exception as e')


def main():
    """Main function.
    """
    st = time.time()
    # Initiate the parser
    parser = argparse.ArgumentParser()
    # Add long and short argument
    parser.add_argument("--url", "-u", help="url link")
    parser.add_argument("--number_of_threads", "-n", help="number of threads")
    # Read arguments from the command line
    args = parser.parse_args()
    # Check for arguments
    if args.url and args.number_of_threads:
        scrapper_object = LinkScrapper(args.url, int(args.number_of_threads))
        scrapper_object.driver_code()
    else:
        print(f'Url/thread number not provided')


if __name__ == "__main__":
    main()
