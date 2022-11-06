# Distyce, a classroom like no other.

## What is it?

Distyce is an academy in which its users can learn through different files whenever they want and upload an evaluation to get their certificate, do you want to acquire more knowledge and skills? Distyce is your classroom.

## Functions:

### What can I do?

Users can:
- Sign up
- See the catalog
- Filter the catalog
- Check a course

Students can:
- Log in
- Change password
- Reset password
- See the catalog
- Filter the catalog
- Check a course
- Send evaluations

Admins can:
- Log in
- Change password
- Reset password
- See the catalog
- Filter the catalog
- Check a course
- Edit a course
- Delete a course

### What will I be able to do?

In future patches more functions will be added to Distyce!
- Students will have a profile to check their progress
- Evaluations will be sent to our teachers mails
- More files extensions will be used in courses!

## Technologies:

- Python
- Django
- Virtual Environment
- HTML
- CSS
- JS
- SQLite
- Pillow
- Whitenoise
- Bootstrap
- Fontawesome
- Gmail SMTP Server

## Instructions:

1. Enter the following instructions to update your system:
```
sudo apt-get update
sudo apt-get upgrade
```

2. Install Python3:
```
sudo apt-get install python3-dev
```

3. Install pip for python3:
```
sudo apt install python3-pip
```

4. Navigate to the folder containing the downloaded project using the "cd" command and the respective route.

5. Install virtualenv through pip3:
```
pip3 install venv
```

6. Create a virtual environment for your local project:
```
python3 -m venv venv
```

7. Install all needed dependencies and requirements for the project:
```
pip3 install -r requirements.txt
```

8. Activate your virtual environment:
```
source venv/bin/activate
```

9. Make migrations in the project using the command:
```
python3 manage.py migrate
```

10. Create a super user that will be the first admin of the site:
```
python3 manage.py createsuperuser
```

11. Run your project:
```
python3 manage.py runserver
```

12. Open your browser and search for the following address: 127.0.0.1:8000/
