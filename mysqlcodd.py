from mysql.connector import connect, Error



def MySQL_REG(id: str):

    try:
        with connect(
            host="localhost",
            user="burger",
            password="wede12345678900",
            database="online_move"
        ) as connection:
            command_table = f"SELECT id FROM mats_user WHERE id = {id}"
            #create_table = "CREATE TABLE mats_user(id VARCHAR(100), mat INT, ban BOOL)"
            #delete = "DROP TABLE mats_user"
            with connection.cursor() as cursor:

                cursor.execute(command_table)

                id_users = cursor.fetchall()

                if len(id_users) == 0 or id not in id_users[0]:
                    create_new_user = "INSERT INTO mats_user (id, mat, ban) VALUES(%s, %s, %s)"
                    values = [(id, 0, False)]

                    cursor.executemany(create_new_user, values)

                    connection.commit()

                    return 0, 0
                else:
                    show_user_mat = f"SELECT mat, ban FROM mats_user WHERE id = {id}"
                    cursor.execute(show_user_mat)

                    result = cursor.fetchall()
                    return result[0]

    except Error as e:
        print(e)

def MySQL_Mat(id: str):

    try:
        with connect(
            host="localhost",
            user="burger",
            password="wede12345678900",
            database="online_move"
        ) as connection:
            create_table = f"SELECT id FROM mats_user WHERE id = {id}"

            with connection.cursor() as cursor:

                cursor.execute(create_table)

                id_users = cursor.fetchall()

                if len(id_users) == 0 or id not in id_users[0]:
                    create_new_user = "INSERT INTO mats_user (id, mat, ban) VALUES(%s, %s, %s)"
                    values = [(id, 1, False)]

                    cursor.executemany(create_new_user, values)

                    connection.commit()

                    return 1, 0
                else:
                    show_user_mat = f"SELECT mat FROM mats_user WHERE id = {id}"
                    cursor.execute(show_user_mat)

                    mat = cursor.fetchall()

                    update_mat = f"UPDATE mats_user SET mat = {mat[0][0] + 1} WHERE id = {id}"
                    cursor.execute(update_mat)
                    connection.commit()

                    show_user_mat = f"SELECT mat, ban FROM mats_user WHERE id = {id}"
                    cursor.execute(show_user_mat)

                    result = cursor.fetchall()

                    return result[0][0], result[0][1]

    except Error as e:
        print(e)


def MySQL_Ban(id: str):

    try:
        with connect(
            host="localhost",
            user="burger",
            password="wede12345678900",
            database="online_move"
        ) as connection:
            create_table = f"SELECT id FROM mats_user WHERE id = {id}"

            with connection.cursor() as cursor:

                cursor.execute(create_table)

                id_users = cursor.fetchall()

                if len(id_users) == 0 or id not in id_users[0]:
                    create_new_user = "INSERT INTO mats_user (id, mat, ban) VALUES(%s, %s, %s)"
                    values = [(id, 5, True)]

                    cursor.executemany(create_new_user, values)

                    connection.commit()

                    return 5, 1
                else:
                    update_ban = f"UPDATE mats_user SET mat = 5, ban = 1 WHERE id = {id}"
                    cursor.execute(update_ban)
                    connection.commit()

                    show_user_mat = f"SELECT mat, ban FROM mats_user WHERE id = {id}"
                    cursor.execute(show_user_mat)

                    result = cursor.fetchall()

                    return result[0][0], result[0][1]

    except Error as e:
        print(e)


def MySQL_UnBan(id: str):

    try:
        with connect(
            host="localhost",
            user="burger",
            password="wede12345678900",
            database="online_move"
        ) as connection:
            create_table = f"SELECT id FROM mats_user WHERE id = {id}"

            with connection.cursor() as cursor:

                cursor.execute(create_table)

                id_users = cursor.fetchall()

                if len(id_users) == 0 or id not in id_users[0]:
                    create_new_user = "INSERT INTO mats_user (id, mat, ban) VALUES(%s, %s, %s)"
                    values = [(id, 0, False)]

                    cursor.executemany(create_new_user, values)

                    connection.commit()

                    return 0, 0
                else:
                    update_ban = f"UPDATE mats_user SET mat = 0, ban = 0 WHERE id = {id}"
                    cursor.execute(update_ban)
                    connection.commit()

                    show_user_mat = f"SELECT mat, ban FROM mats_user WHERE id = {id}"
                    cursor.execute(show_user_mat)

                    result = cursor.fetchall()

                    return result[0][0], result[0][1]

    except Error as e:
        print(e)
