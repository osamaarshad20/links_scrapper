## Installation

* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can
  get python [here](https://www.python.org").

* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/theherd8/links_scrapper
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd links_scrapper
        ```
    2. Create a python virtual env using the below command.
        ```bash
            $ python3 -m venv test_env   
        ```
    3. Activate that enviorment a python virtual env using the below command.
        ```bash
            $ source test_env/bin/activate  
        ```
    4. Install all the dependancies using the following command form requirements.txt.
        ```bash
            $ pip install -r requirements.txt  
        ```
    5. Now, yuu are ready to hit the bash script using the following command
        ```bash
            $ bash crawl.sh [url to crawl e.g 'https://stackoverflow.com/questions/15155476/check-if-url-that-belongs-to-the-same-domain-exists-in-list-with-python'] [number of process e.g 10]
        ```
    