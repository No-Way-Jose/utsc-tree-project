import sqlite3
from sqlite3 import Error


def createConnection(database):
    """
    Create a database connection to the SQLite database
    """
    connection = None
    # Try connecting to the database
    try:
        connection = sqlite3.connect(database)
    except Error as e:
        print(e)
    # Return the connection if available
    return connection


def endConnection(connection):
    """
    Function to close the connection when done
    """
    connection.close()


def wipeData(connection):
    """
    Function that will wipe the database and all tables
    """
    # Clear the Main Directory
    sql = 'DELETE FROM MainDirectory'
    cur = connection.cursor()
    cur.execute(sql)
    # Clear the Sub Directory
    sql = 'DELETE FROM SubDirectory'
    cur = connection.cursor()
    cur.execute(sql)
    # Clear the Course Directory
    sql = 'DELETE FROM CourseDirectory'
    cur = connection.cursor()
    cur.execute(sql)
    # Clear the sequence data
    sql = 'DELETE FROM sqlite_sequence'
    cur = connection.cursor()
    cur.execute(sql)

    connection.commit()


def insertSection(connection, value):
    """
    This function will insert course page for each Letter in the main directory
    """
    # Create the command template
    sql = ''' INSERT INTO MainDirectory(Sections) VALUES(?) '''
    cur = connection.cursor()
    # Execute the insert
    cur.execute(sql, [value])
    # Return the ID
    return cur.lastrowid


def insertSubSection(connection, mainID, value):
    """
    This function will insert each subsection for each letter into the sub directory
    """
    # Create the command template
    sql = ''' INSERT INTO SubDirectory(MainID, SubSections) VALUES(?,?) '''
    cur = connection.cursor()
    # Execute the insert
    cur.execute(sql, [mainID, value])
    # Return the ID
    return cur.lastrowid


def insertCourse(connection, subID, mainID, courseURL, name, desc, pre, exc, limit, breadth):
    """
    This function will store all the course information into the course directory
    """
    # Create the command template
    sql = ''' INSERT INTO CourseDirectory(SubID, MainID, CourseURL, Name, Description, Prerequisite, Exclusion, StudentLimit, Breadth) VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = connection.cursor()
    # Execute the insert
    cur.execute(sql, [subID, mainID, courseURL, name, desc, pre, exc, limit, breadth])
    # Return the ID
    return cur.lastrowid


def searchPre(connection, course):
    """
    This function will return the prereqs for the searched course
    """
    # Create the command template
    sql = ''' SELECT Prerequisite FROM CourseDirectory WHERE name LIKE ? '''
    cur = connection.cursor()
    # Execute the insert
    cur.execute(sql, ["%"+course+"%"])
    prereqs = cur.fetchone()
    # Return the ID
    return str(prereqs).strip('()')


def getDirectory(connection, modifier, param):
    """
    This function will return the columns requested
    """
    # Create the command template
    cur = connection.cursor()
    if modifier == 0:
        # Execute the command
        cur.execute('''SELECT ID, Sections FROM MainDirectory''')
    elif modifier == 1:
        cur.execute('''SELECT ID, SubSections FROM SubDirectory WHERE MainID=? ''', (param, ))
    elif modifier == 2:
        cur.execute('''SELECT Name FROM CourseDirectory''')
    else:
        cur.execute('''SELECT Name FROM CourseDirectory WHERE SubID=? ''', (param, ))
    directory = cur.fetchall()
    # Return the dir
    return directory


def getInformation(connection, course):
    """
    This function will return all the information related to the course
    """
    # Create the command template
    cur = connection.cursor()
    # Execute the command
    cur.execute(''' SELECT * FROM CourseDirectory WHERE name =?''', (course, ))
    information = cur.fetchall()
    # Return the info
    return information
