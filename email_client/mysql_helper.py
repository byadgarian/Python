# MySQL Helper Module



# Import librarires
import mysql.connector


# Show columns function
def show_columns(table_name):
    # Define variables
    results = list()

    # Generate SQL command
    command = "SHOW COLUMNS FROM " + table_name

    # Execute SQL command and handdle errors
    try:
        connection = mysql.connector.connect(user = '***', password = '***', host = '***', port = '***', database = '***', 
                                             ssl_ca = '***', ssl_cert = '***', ssl_key = '***')
        cursor = connection.cursor()
        cursor.execute(command)
        results = cursor.fetchall()
    except mysql.connector.Error as mysql_error:
        mysql_status = False
        mysql_message = 'MySQL Error: ' + str(mysql_error)
        return mysql_status, mysql_message, results
    cursor.close()
    connection.close()

    # Return status, message, and retrieved data
    mysql_status = True
    mysql_message = ''
    return mysql_status, mysql_message, results


# Select function
def mysql_select(table_name, requested_attributes, provided_atrributes):
    # Define variables
    results = list()

    # Generate SQL command
    command = "SELECT "
    for attribute in requested_attributes:
        command += attribute + ', '
    command = command[:-2]
    command += " FROM ipc." + table_name
    if len(provided_atrributes.keys()) != 0:
        command += " WHERE "
        for key, value in provided_atrributes.items():
            command += key + " = '" + value + "' AND "
        command = command[:-5]

    # Execute SQL command and handdle errors
    try:
        connection = mysql.connector.connect(user = '***', password = '***', host = '***', port = '***', database = '***', 
                                             ssl_ca = '***', ssl_cert = '***', ssl_key = '***')
        cursor = connection.cursor()
        cursor.execute(command)
        results = cursor.fetchall()
    except mysql.connector.Error as mysql_error:
        mysql_status = False
        mysql_message = 'MySQL Error: ' + str(mysql_error)
        return mysql_status, mysql_message, results
    cursor.close()
    connection.close()

    # Return status, message, and retrieved data
    mysql_status = True
    mysql_message = ''
    return mysql_status, mysql_message, results