from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
from pandas import DataFrame


class archiveData:
    def __init__(self, sectionLink):
        self.sectionLink = sectionLink
        self.fileLink = ""

    def loadFileLink(self, fileLink):
        self.fileLink = fileLink


    def to_dict(self):
        return {
            'section': self.sectionLink,
            'file': self.fileLink,

        }


class ArchiveScrape:
    #this is the collection link in archve.org
    search_url= ""

    #this is the file extension (All caps)
    file_ext = "PDF"

    the_list = []

    def __init__(self, webDriver):

        self.driver = webDriver
        self.driver.get(self.search_url)

    def scrape(self):
        input("Press Enter when all results are loaded")
        resultclass = self.driver.find_element(by=By.CLASS_NAME, value="results")
        elements = resultclass.find_elements(by=By.TAG_NAME, value='a')
        for element in elements:
            try:
                if("/details/" in  element.get_attribute("href") and "stealth" not in element.get_attribute("class")):


                    self.the_list.append(archiveData(element.get_attribute("href")))
            except:
                print("something is wrong")

        #going into each one to get links
        for item in self.the_list:
            try:
                #do something
                self.driver.get(item.sectionLink)
                time.sleep(3)

                elements = self.driver.find_elements(by=By.TAG_NAME, value='a')
                for element in elements:
                    if(self.file_ext in element.get_attribute("innerText")):
                        print("Link Found")
                        item.loadFileLink(element.get_attribute("href"))
            except:
                print("something is wrong")

        df = DataFrame([s.to_dict() for s in self.the_list])
        df.to_excel("archivedump.xlsx", sheet_name='sheet1', index=False)
        self.driver.close()
        print("All jobs are finished")





options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome('chromedriver', options=options)
archiveBot = ArchiveScrape(driver)
archiveBot.scrape()



