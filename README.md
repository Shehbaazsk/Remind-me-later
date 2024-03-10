Remind-Me-Later 
==============================
## Installation

    Python 3.x is required. If you don't have Python 3.x or higher, download the appropriate package and install:

* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/Shehbaazsk/Remind-me-later.git .
    ```

* #### Dependencies
    1. Create and fire up your virtual environment:
        ```bash
            $ python3 -m venv venv
            $ source venv/bin/activate
        ```
    2. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    3. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```

