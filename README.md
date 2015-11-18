Here is a nice Flask tutorial that I went off of for the board page:
http://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972

### Working with the database
We are going to use MySQL and Python for this terminal based project.

To setup mysql and use the file in src/database.py do the following:
```
sudo apt-get install mysql
sudo apt-get install mysql.connector

Start up mysql and create a new user so we don't have to worry about sharing sensitive passwords
```
mysql -u root -p

mysql> CREATE USER 'tempuser'@'localhost' IDENTIFIED BY 'password';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'tempuser'@'localhost'
    ->      WITH GRANT OPTION;

Now close the session and launch mysql again, but with the following:
```
mysql -u tempuser -p

Let's set up the database on your localhost
```
CREATE DATABASE project_brian_test;

use project_brian_test;

Now we can create tables. Go to the template directory. Copy and paste the tables into the mysql session.
Learn more about sql in w3schools.
