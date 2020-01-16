from SQL import *
import re
import json


def prereqTree(course):
    """
    This function is designed to look through the database and find all the prereqs for the desired course
    """
    # Dictionary to store all the info
    pre = {"name": course,
           "image_url": "https://seethefullpicture.ca/wp-content/uploads/2019/06/Alcon_SeeTheFullPicture_Website_1901x11252.jpg",
           "children": [{"name": "BOB",
                         "image_url": "https://seethefullpicture.ca/wp-content/uploads/2019/06/Alcon_SeeTheFullPicture_Website_1901x11252.jpg"},
                        {"name": "JUSTIN",
                         "image_url": "https://seethefullpicture.ca/wp-content/uploads/2019/06/Alcon_SeeTheFullPicture_Website_1901x11252.jpg"}]}
    # Create the db connection
    connection = createConnection()
    # Get the prereqs for the course
    prereqsD = getPrereqs(course, connection)
    # String return var
    stringTree = course + "\n"

    # Run a loop to go through all the prereqs for the C level course
    for prereqsC in prereqsD:
        if not isinstance(prereqsC, list):
            # Add in the prereqs and course into the dictionary
            preC = getPrereqs(prereqsC, connection)
            spot = prereqsD.index(prereqsC)
            stringTree += "\t" + prereqsC + "\n"
            # Inner loop to check prereqs for the B level courses
            for prereqsB in preC:
                # Check so we loop over every other item and not over the new items we added in
                if not isinstance(prereqsB, list):
                    # Add in the prereqs and course into the dictionary
                    preB = getPrereqs(prereqsB, connection)
                    spotB = preC.index(prereqsB)
                    stringTree += "\t\t" + prereqsB + "\n"
                    # Inner loop to check prereqs for the A level courses
                    for prereqsA in preB:
                        # Check so we loop over every other item and not over the new items we added in
                        if not isinstance(prereqsA, list):
                            # Add in the prereqs and course into the dictionary
                            preA = getPrereqs(prereqsA, connection)
                            spotA = preB.index(prereqsA)
                            stringTree += "\t\t\t" + prereqsA + "\n"
                            if len(preA) > 0:
                                for courseA in preA:
                                    stringTree += "\t\t\t\t" + courseA + "\n"
                            preB.insert(spotA + 1, preA)

                    preC.insert(spotB + 1, preB)
            prereqsD.insert(spot + 1, preC)

    # End the connection
    endConnection(connection)
    # Return the list
    return json.dumps(pre, indent=4, separators=(',', ': '))


def prereqData(course):
    """
    This function is designed to look through the database and find all the prereqs for the desired course
    """
    # Dictionary to store all the info
    pre = {"name": course,
           "image_url": "https://seethefullpicture.ca/wp-content/uploads/2019/06/Alcon_SeeTheFullPicture_Website_1901x11252.jpg",
           "children": []}
    # Create the db connection
    connection = createConnection()
    # Get the prereqs for the course
    prereqsD = getPrereqs(course, connection)


def getPrereqs(course, connection):
    # Search for the prereqs
    with connection:
        returnItem = searchPre(connection, course)
    # Add in the prereqs and course into the dictionary
    listOfPre = re.findall(r'[A-Z]{4}[0-9]{2}[A-Z][0-9]', returnItem)
    # Parse the prereqs into a better format
    prereqList = returnItem.replace("'", "").replace(",", "").split("and")
    finalPrereqList = []
    # Loop through the list
    for pre in prereqList:
        if pre.count("]") == 2 and pre.index("or") != -1:
            finalPrereqList[-1] += pre
        else:
            finalPrereqList.append(pre)

    return listOfPre


def parsePrereqs(prereqs):
    """
    This function is designed to parse the prerequisites
    """


# print(prereqTree("CSCA08H3"))


def courseInfo(course):
    info = {}
    # Create the db connection
    connection = createConnection()

    with connection:
        courseInformation = getInformation(connection, course)

    # End the connection
    endConnection(connection)

    # Format the string return
    info["desc"] = courseInformation[0][5]
    info["pre"] = courseInformation[0][6]
    info["ex"] = courseInformation[0][7]
    info["limit"] = courseInformation[0][8]
    info["breadth"] = courseInformation[0][9]

    # Return JSON string
    return json.dumps(info, indent=4, separators=(',', ': '))


def courseDirectory():
    finalDir = []
    mainDir = {}
    subDir = {}
    courses = {}
    idCounter = 1
    # Create the db connection
    connection = createConnection()
    # Get the main directory to start
    directory = getDirectory(connection, 0, "")
    # Run a loop to get the sub directory
    for x in directory:
        mainDir['id'] = idCounter
        mainDir['name'] = x[1][-1]
        mainDir['children'] = []
        idCounter += 1

        subDirectory = getDirectory(connection, 1, x[0])
        # Run a loop to get the courses for each sub directory
        for y in subDirectory:
            subDir['id'] = idCounter
            subDir['name'] = y[1]
            subDir['children'] = []
            idCounter += 1

            coursesDir = getDirectory(connection, 3, y[0])
            # Add the courses
            for z in coursesDir:
                courses['id'] = idCounter
                courses['name'] = z[0]
                idCounter += 1
                subDir['children'].append(courses)
                courses = {}

            mainDir['children'].append(subDir)
            subDir = {}

        finalDir.append(mainDir)
        mainDir = {}

    # End the connection
    endConnection(connection)

    # with open('data.json', 'w', encoding='utf-8') as f:
    # json.dump(finalDir, f, ensure_ascii=False, indent=4, separators=(',', ': '))

    return json.dumps(finalDir, indent=4, separators=(',', ': '))


def getAllCourses():
    """
    This method will return a list of all the courses
    """
    # Create the db connection
    connection = createConnection()
    # Get the list of all the courses
    directory = getDirectory(connection, 2, "")
    # Create the list of dictionaries with the courses
    courses = []
    for course in directory:
        code = re.findall(r'[A-Z]{4}[0-9]{2}[A-Z][0-9]', str(course))
        item = {"value": code[0], "text": course[0]}
        courses.append(item)

    # End the connection
    endConnection(connection)

    return json.dumps(courses, indent=4, separators=(',', ': '))


def test():
    """
    This function is designed to look through the database and find all the prereqs for the desired course
    """
    # Create the db connection
    connection = createConnection()
    # Get the prereqs for the course
    prereqsD = searchPre(connection, "ANTD05H3")
    breakdown = []
    for item in prereqsD.replace(".", "").replace(",", "").replace("'", "").split("] "):
        if "and" in item[0:3]:
            breakdown.append(item[0:3])
            breakdown.append(item[5:])
        elif "or" in item[0:2]:
            breakdown.append(item[0:2])
            breakdown.append(item[4:])
        else:
            breakdown.append(item)

    if breakdown[0][0] == "[":
        breakdown[0] = breakdown[0][2:]
    print(breakdown)


def generatePrereqCode():
    # Create the db connection
    connection = createConnection()
    # Get the prereq columns
    prereqCols = getPrereqColumn(connection)
    # Loop through each row and generate the codes
    for prereq in prereqCols:
        # If no prereqs
        if prereq[1] == "N/A":
            updatePrereqCode(connection, ("0", prereq[0]))
        elif len(prereq[1]) == 8:
            # Find the course ID and insert it
            updatePrereqCode(connection, (getCourseID(connection, prereq[1]), prereq[0]))
        # Simple case with just AND or OR (no brackets or anything)
        elif (not bool(re.search(r'[\]\[(),.]', prereq[1]))) and re.search(r'[A-Z]{4}[0-9]{2}[A-Z][0-9]', prereq[1]):
            code = ""
            # IF to see if dealing with & or |
            if prereq[1].count("and") > 0 and prereq[1].count("or") == 0:
                courses = prereq[1].split(" and ")
                for course in courses:
                    code += getCourseID(connection, course.strip()) + "&"
            elif prereq[1].count("or") > 0 and prereq[1].count("and") == 0:
                courses = prereq[1].split(" or ")
                for course in courses:
                    code += getCourseID(connection, course.strip()) + "|"
            # ELSE CASE WHEN YOU HAVE AND&OR NEED TO FINISH FORMATTER FIRST THOUGH TO REMOVE [] WHEN UNNECESSARY
            # Insert the code
            updatePrereqCode(connection, (code[:-1], prereq[0]))
        # "Any #.0 Credits" case
        elif re.match(r'[Any\s\d.\d\sCredits.?]', prereq[1]) and len(prereq[1]) <= 16:
            # Insert the code
            updatePrereqCode(connection, (prereq[1], prereq[0]))
        # Case where there is no course specified (just plain text)
        elif not bool(re.search(r'[A-Z]{4}[0-9]{2}[A-Z][0-9]', prereq[1])):
            updatePrereqCode(connection, (prereq[1].replace('[', '').replace(']', ''), prereq[0]))
        # Co-op case just put 0
        elif bool(re.search(r'COP[A-Z][0-9]{2}[A-Z][0-9]', prereq[1])):
            # Insert the code
            updatePrereqCode(connection, ("0", prereq[0]))
        else:
            # Insert the code
            updatePrereqCode(connection, ("-", prereq[0]))

    # End the connection
    endConnection(connection)


def removeOld():
    """
    This function will remove all the courses that no longer exist
    """
    # Create the db connection
    connection = createConnection()
    # Get the prereq columns
    prereqCols = getPrereqColumn(connection)
    # Lop through the list and start updating
    for prereq in prereqCols:
        temp = ""
        flag = False
        temp = prereq[1]
        # Check to see if there are any courses that no longer exist
        counter = temp.count("/(")
        if counter > 0:
            flag = True
            # Run a loop to start splicing/removing
            while counter > 0:
                oldIndex = temp.index("/(")
                newPrereq = temp[:oldIndex] + temp[oldIndex+12:]
                temp = newPrereq
                counter -= 1
        # Additional check if necessary
        extraCounter = temp.count("(")
        if extraCounter > 0:
            flag = True
            # Run a loop to start splicing/removing
            while extraCounter > 0:
                oldIndex = temp.index("(")
                newPrereq = temp[:oldIndex] + temp[oldIndex + 11:]
                temp = newPrereq
                extraCounter -= 1
        if flag:
            # Update with the new prereq
            updatePrereq(connection, (temp, prereq[0]))


def formatter():
    # Create the db connection
    connection = createConnection()
    # Get the prereq columns
    prereqCols = getPrereqColumn(connection)
    # Lop through the list and start updating
    for prereq in prereqCols:
        temp = prereq[1]
        flag = False
        # Make sure everything is formatted properly
        courses = re.findall(r'[A-Z]{4}[0-9]{2}[A-Z][0-9]', temp)
        if len(courses) == 1 and len(temp) <= 20:
            temp = temp[:8]
            flag = True
        # Get rid of 'or equivalent'
        equivCounter = temp.count("or equivalent")
        if equivCounter > 0:
            flag = True
            index = temp.index("or equivalent")
            while equivCounter > 0:
                # Remove it
                temp = temp[:index] + temp[index+14:]
                equivCounter -= 1
            # Special case
            if prereq[0] == 671:
                # Remove it
                temp = temp[:len(prereq[1])-14]

        if flag:
            # Update the prereq
            updatePrereq(connection, (temp, prereq[0]))


# REMOVE THIS WHEN DONE
def specialCases():
    # Create the db connection
    connection = createConnection()
    # Get the prereq columns
    special = getSpecialCases(connection, "-")
    for case in special:
        print(case)


#removeOld()
#formatter()
#generatePrereqCode()
#specialCases()

def unlockedCourses(prereq):
    """
    This function will return a formatted list of all the courses that has the selected course as a prereq
    """
    # Create the db connection
    connection = createConnection()
    # Get the unlocked courses
    unlocked = getUnlocked(connection, prereq)
    # Loop through the return
    result = {"A": [], "B": [], "C": [], "D": []}
    for course in unlocked:
        item = (str(course).replace("'", "").replace(",", "").replace("(", "").replace(")", ""))
        result[item[3]].append(item)

    print(result)


unlockedCourses("IDSA01H3")
