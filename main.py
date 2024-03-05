# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Installing required Libraries
libraries = ["selenium","pandas","numpy"]

import importlib
import subprocess
import time

def check_library(library_name):
    for i in range(len(libraries)):
        try:
            importlib.import_module(library_name[i])
        except ImportError:
            print(f"{library_name[i]} is being installed...")
            subprocess.run(["pip", "install", library_name[i]])
        print(f"{library_name[i]} is installed.")
        
def store_CSV(Que,Ans):
    df = pd.DataFrame({'Questions': Que, 'Answers': Ans})
    df.to_csv('survey_data.csv', index=False)
    
    
check_library(libraries)


#Importing Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


#Fetching information from webpage
driver = webdriver.Chrome()
driver.get("https://www.wahl-o-mat.de/bundestagswahl2021/app/main_app.html")

#Find Begin button and start the Survey
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "button--big")))
button.click()


# Extract and print the content of each <p> element
Total_questions = len(driver.find_elements(By.CSS_SELECTOR,'li.glide__slide'))
Valid_Answers = [0,1,-1]
Que = []
Ans = []

# for i in range(Total_questions):
for i in range(4):
    time.sleep(4)
    active_instance = driver.find_element(By.CSS_SELECTOR,'li.glide__slide.is-active.glide__slide--active')
    paragraphs = active_instance.find_element(By.CSS_SELECTOR,'p.theses__text')
    print(paragraphs.text)
    Que.append(paragraphs.text)
    
    
    #Buttons for answers
    button = WebDriverWait(active_instance, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "button.theses-btn")))
    answer = int(input("Your Answer : "))
    
    while(answer not in Valid_Answers):
        print("Invalid answer... Try Again...\n(Possible asnwer is")
        print("1 : I agree\n0 : Neutral\n-1 : I don't agree")
        answer = int(input("Your Answer : "))
    else:
        if(answer == 0):
            button[1].click()
        elif(answer == 1):
            button[0].click()
        else:
            button[2].click()
        Ans.append(answer)

store_CSV(Que,Ans)