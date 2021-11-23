# Simple-Tkinter-Based-Python-GUI-Application
Its is Python application that demonstrates how Tkinter GUI and MySql database connector works. This tested for Windows platform only.
## Running this application
Follow these steps to run the application successfully
1) Install MySql server if you haven't already
2) Install Python 3 if you haven't already
3) Open your cmd/powershell and execute this command `pip install mysql-connector-python` to install Python MySql driver
4) Next excute this command `pip install tkinter` to install tkinter GUI library
5) Now open the `app.py` file and change these details as per your MySql installation:
  `cur = con.connect(
        host='localhost',
        user='root',
        password=''
    )`
6) That's it now run the `main.py` file, enter some data, click the button and verify the data in your database.
