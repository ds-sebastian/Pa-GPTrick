#%%

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import re
#from time import sleep
from tqdm import tqdm
#%%

headless = True

#def __init__(self, headless=True):

#Chrome Options
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
if headless == True:
    options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--incognito")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#Chrome Driver
driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install(), options=options)


#%%
#Open transcripts
driver.get("https://spongebob.fandom.com/wiki/List_of_transcripts")

#%%
#Get all link <a> tags 
elems = driver.find_elements(By.LINK_TEXT,  "View transcript")
print(f'Found {len(elems)} transcript pages')


#%%
#Get all links
links = []
for elem in tqdm(elems, desc="Processing transcript links..."):
    link = elem.get_attribute('href')
    links.append(link)

#save links
with open("links.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(links))

#%%
#Open and save transcripts
try:
    transcripts = []

    for link in tqdm(links, desc="Links"):

        driver.get(link) #navigate to transcript page

        episode = re.search('wiki/(.*)/transcript', link).group(1) #episode name

        elems = driver.find_elements(By.TAG_NAME,"li") #quotes are all lists
        quotes = []
        for q in elems:
            if ":" in q.text:
                quotes.append(str(q.text))

        #Append master list
        transcript = "\n".join(quotes)
        transcripts.append(transcript)

        #Save individual transcripts
        with open('transcripts/'+episode+'.txt', 'w', encoding="utf-8") as f:
            f.write(transcript)

except Exception as e:
    print(e)
    driver.quit()

# %%
with open("spongebob_anthology.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(transcripts))
