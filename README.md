# django-file-uploader
File uploader built in Django

Creating venv
python3 -m venv < your virtualenv name >

Activating venv
source < your virtualenv name >/bin/activate

Installing requirments
pip install -r requirments.txt

Initiate project
django-admin startproject < your project name > .

Create app
./manage.py startapp < you app name >

Launch tests
./manage.py test csv_upload/

Launch
./manage.py runserver

Upload document path
url : /document/upload/

Get document by numdos
url : document/get/<str:numdos>/
