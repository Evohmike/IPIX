# [IPIX](https://ipix.herokuapp.com/)
### Simple watch gallery web application that showcase different types of watches,their location of origin and categories. 
### September 28th, 2018
#### By **[Evoh Mike](https://github.com/Evohmike)**

## Description
[IPIX]((https://ipix.herokuapp.com)) is a watch gallery web application to showcase very luxarious,fashionable and designer watches. Users get to view watches updated by the site admin. Users can see watches based on the location of origin, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. The search functionality will search watches based on the categories. 

## Specs
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View watches | Click on the watch you like | Displays the watch in a modal with the name, description |
| Search category | Enter the category in the search input | Displays all watches in the queried category |
| Copy link to clipboard | Click on the copy button | copies the link to the clipboard |
| View watch based on location | Click on the locations in the Menu | Displays all watches in that location |


## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
`git clone https://github.com/Evohmike/IPIX.git && cd IPIX`

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
```bash
virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
```

### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements.txt`

### Create the Database
```bash
psql
CREATE DATABASE ipix;
```
### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'ipix'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True
```
### Run initial Migration
```bash
python3.6 manage.py makemigrations album
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Known bugs
No known bugs. If you find any please feel free to contact me.

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

## Support and contact details
Contact me on evohmike@gmail.com for any comments, reviews or advice.

### License
Copyright (c) 
##### **[Evoh mike] (https://github.com/Evohmike/IPIX/blob/master/LICENSE)**