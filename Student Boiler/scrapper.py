from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"  

browser = webdriver.Edge()  
browser.get(START_URL)

time.sleep(2)  

stars_data = []  


def scrape():
    for i in range(0, 5):
        print(f'Scraping page {i+1} ...')

        soup = BeautifulSoup(browser.page_source, "html.parser")
         

    
        for star in soup.find_all("div", class_="hds-content-item"):

            
            star_info = []

            star_info.append(star.find_all("h3", class_="heading-22").text.strip())
        
            
            information_to_extract = ["Light-Years From Earth", "star Mass", 
                                      "Stellar Magnitude", "Discovery Date"]

            
            for info_name in information_to_extract:
            
                
                try:


                    
                    star_info.append(star.select_one(f'span:-soup-contains("{info_name}")'))

                
                except:
                    
                    
                    star_info.append("unknown")
                    
            
            stars_data.append(star_info)
        
        
        try:
        
            
            time.sleep(2)
            
            
            next_button = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="primary"]/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/nav/button[8]')))


            
            browser.execute_script("arguments[0].scrollIntoView();",next_button)
            
            
            time.sleep(2)
            
    
            next_button.click()
        
        
        except:
        
            
            print(f'error')
            break
            


scrape()


headers = ["name", "light_years_from_earth", "star_mass", "stellar_magnitude", "discovery_date"]

star_df = pd.DataFrame(stars_data, columns=headers)


star_df.to_csv("STARS.csv", index=True, index_label="id")


