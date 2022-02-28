import psycopg2
from psycopg2 import Error


# def show_users_group_db():
#     5. Проверить, что в базе данных пользователь добавлен в группу
# def test_one():
#     connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
#     mycursor = connection.cursor()
#     mycursor.execute("SELECT id FROM auth_user WHERE username='user_one'")
#     x = mycursor.fetchall()
#     for i in x:
#         return i
#
#     mycursor.execute("SELECT user_id FROM auth_user_groups")
#     y = mycursor.fetchall()
#     for j in y:
#         return j
#
#     assert x in y
#
# connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
# mycursor = connection.cursor()
# mycursor.execute("SELECT * FROM auth_user_groups")
# group = mycursor.fetchall()
# for groupname in group:
#     print(groupname)
# #
# #
# mycursor.execute("SELECT * FROM auth_group")
# group = mycursor.fetchall()
# for groupname in group:
#     print(groupname)


# mycursor.execute("SELECT * FROM auth_user")
# group = mycursor.fetchall()
# for groupname in group:
#     print(groupname)
# #
# mycursor.execute("""SELECT table_name
# FROM information_schema.tables
# WHERE table_schema='public'
# AND table_type='BASE TABLE'""")
# group = mycursor.fetchall()
# for i in group:
#     print(i)

def test_one():
    connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
    mycursor = connection.cursor()
    mycursor.execute("SELECT id FROM auth_user")  # all users id
    x = mycursor.fetchall()
    # print(x)
    # for i in x:
    #     print(i)

    mycursor.execute("SELECT user_id FROM auth_user_groups")  # user id from group
    y = mycursor.fetchall()
    # print(y)
    # for j in y:
    #     print(j)
    result = []
    for i in x:
        for j in y:
            if i == j:
                result.append(j)
    print(result)
    assert y == result



