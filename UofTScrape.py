import requests
import urllib
from SQL import *
from bs4 import BeautifulSoup


def ScrapeUTSC(url):
    """
    Function which will scrape the UTSC course website and store all the needed information into a database
    """
    # Connect to the main page
    response = requests.get(url)
    document = BeautifulSoup(response.text, "html.parser")

    # Database location
    database = "/Users/riceboy/RiceBoy Documents/UTSC Course Tree/UtscCourses.db"
    # Create the db connection
    connection = createConnection(database)
    # Wipe the data
    wipeData(connection)

    # Lists to hold all the values
    base = "https://utsc.calendar.utoronto.ca/list-of-courses"
    courseAlpha = []
    coursesList = []

    # Get list of courses starting with *** first letter
    alphaDoc = (document.find("div", {"id": "alpha"}))
    for link in alphaDoc.find_all('a'):
        # List that holds the URL to the different Letters for each course
        courseAlpha.append(urllib.parse.urljoin(base, link.get("href")))
        sections = urllib.parse.urljoin(base, link.get("href"))
        # Insert the sections into the database
        with connection:
            sectionID = insertSection(connection, sections)

        # Connect to the page
        alphaPage = requests.get(urllib.parse.urljoin(base, link.get("href")))
        letterDoc = BeautifulSoup(alphaPage.text, "html.parser")
        # List to store the subsect IDs
        subSecIDs = []

        # Loop to get all the subsection headers and required values
        for subHeading in letterDoc.find_all("h3", {"class": "views-accordion-list_of_courses-page-header"}):
            subSection = (subHeading.get_text().strip())
            # Insert the subsection into the db
            with connection:
                subSectionID = insertSubSection(connection, sectionID, subSection)
                # Store the IDs for the subsections
                subSecIDs.append(subSectionID)

        # Variables to use to determine when to switch to the next subdirectory ID value
        oldSection = ""
        subSectID = 0

        # Get each course section for the given Letter
        for course in letterDoc.find_all("div", {"class": "views-field views-field-field-course-title"}):
            courseURL = (urllib.parse.urljoin(base, (course.find(href=True)).get("href")))
            coursesList.append(urllib.parse.urljoin(base, (course.find(href=True)).get("href")))

            # Connect to the page and scrape the info for the course
            coursePage = requests.get(courseURL)
            courseDoc = BeautifulSoup(coursePage.text, "html.parser")
            courseName = ((courseDoc.find('h1')).get_text().strip())
            # Get the first 2 letters of course so we can determine when to switch subdirectory ID
            nextSection = courseName[:2]

            # List to hold the exclusion, preqreq information TITLES
            info = {"Course Description:": "N/A", "Prerequisite:": "N/A", "Exclusion:": "N/A", "Enrolment Limits:": "N/A", "Breadth Requirements:": "N/A"}
            titles = ["Course Description:"]
            # Fill the list with the course information that is present for the course
            for title in (courseDoc.find_all("div", {"class": "field-label"})):
                titles.append(title.get_text().strip())
            titles.append("Link:")

            # Insert the exclusion, preqreq information VALUES into the dict if present
            for detail in (courseDoc.find("div", {"class": "content clearfix"}).find_all("div", {"class": "field-item even"})):
                info[titles.pop(0)] = (detail.get_text().strip().replace("\n", " "))

            # Check if we should move to the next subsection ID *Languages and Linguistics
            if oldSection != nextSection and nextSection != "PL" and nextSection != "LG":
                # Pop off the next sub ID and set the variable to it for insertion
                subSectID = subSecIDs.pop(0)

            with connection:
                # Insert into the database
                insertCourse(connection, subSectID, sectionID, courseURL, courseName,
                             info.get("Course Description:"),
                             info.get("Prerequisite:"), info.get("Exclusion:"), info.get("Enrolment Limits:"),
                             info.get("Breadth Requirements:"))
            # Update the old section
            oldSection = nextSection

    # Close the connection
    endConnection(connection)


# Call for the scrape
ScrapeUTSC("https://utsc.calendar.utoronto.ca/list-of-courses/a")
