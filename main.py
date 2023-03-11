from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="sportmount_db",
        user=input("Имя пользователя: "),
        password=getpass("Пароль: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)

create_students_table_query = """
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    gender CHAR(1) NOT NULL
)
"""

insert_students_query = """
INSERT INTO students VALUES (1, 'Ryan', 'M');
INSERT INTO students VALUES (2, 'Joanna', 'F');
"""

with connection.cursor() as cursor:
    cursor.execute(create_students_table_query)
    cursor.execute(insert_movies_query)
    connection.commit()
