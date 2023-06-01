# Library-book-management-
It is a Library management backend APIs written in Django-Rest-Framework. I contains bulk create, update, delete features. It also contains APIs for auto-complete for searching student or book. It includes connection request features like Facebook and also has APIs for Friend suggestion.

## Steps to run this project locally:


1. download & Install python==3.7 in your system. use https://www.python.org/
2. Now download & insall postgresql in your system. use https://www.postgresql.org/
3. now setup your postgresql and create and start a server and add your password to .env file's password field.
    I have used xyz for example. create a database with name as "The Page Turners"
4. open vscode and open this project folder. 
5. open vscode terminala and create a virtual environment using: virtualenv env
6. activate virtual env by using: env/scripts/activate
7. make sure you are in the project directory now install all the requirements. for this use command: pip install -r requirements.txt
8. after successfull installation of all the requirements type django-admin to see whether or not djnago have been installed 
9. now make database tables into database, use command: python manage.py makemigrations
10. now migrate all the migrations to database, use command: python manage.py migrate
11. once all the migrations are complete. Now create a superuser to accessing django-admin-panel. for this use comand: python manage.py createsuperuser
12. add all the required info and create superuser. 
13. now run the project by using command: python manage.py runserver . django server will start on your loacalhost using default 8000 port number.
14. for accessing admin panel go to url in your browser: loacalhost:8000/admin/
15. for using the APIs use postman and for details about APIs prefer documentation I have made. For this go to url: https://documenter.getpostman.com/view/26583578/2s93kz659W
