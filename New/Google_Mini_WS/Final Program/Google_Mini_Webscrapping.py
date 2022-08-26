#Project Webscrapping Finale_20 Nov 2020 ~ 20 Dec 2020
#Manual of Use
#0. Set the path you keep this entire folder according to your own path
#1. Enter Keywords on item that you would like to find at 0.Keywords_Data
#2. Enter no. of Pages to crawl
#3. Enter Name of the final output data (Just name withoud csv extension)

import pandas as pd
import time
import csv
import requests
import re
import os
import glob
import sys
import random
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#Selangor Postcode
# Selangor_Postcode = ["68000", "43650", "43600", "42300", "42700", "44300", "48100", "68100", "43700", "45600", "45607", "45620", "45700", "43200", "43207", "63000", "43100", "42600", "42610", "45800", "45209", "45200"
#                     ,"45400", "43500", "43900", "43400", "48200", "43300", "40594", "40800", "40802", "40804", "40806", "40808", "40505", "40150", "40160", "40170", "40460", "40470", "40000", "40810", "40200", "40680"
#                     ,"40500", "40648", "40548", "40550", "40676", "40596", "40564", "40582", "40590", "40608", "40551", "40590", "40626", "40664", "40660", "40517", "40632", "40592", "40576", "40578", "40604", "40400"
#                     ,"40100", "40300", "47650", "47500", "47600", "47200", "45100", "45300", "47000", "43950", "45500", "42800", "42500", "48000", "48020", "48300", "48050", "48010", "44200", "42940", "42920", "42960"
#                     ,"47100", "47120", "47150", "47130", "47110", "47170", "47180", "47160", "47140", "47190", "47400", "46978", "47301", "47300", "47800", "46150", "47410", "46050", "47810", "47820", "47830", "47308"
#                     ,"46506", "46662", "46551", "46564", "46598", "46549", "46667", "46000", "46200", "46300", "46350", "46400", "46100", "47800", "48050", "42000", "45000", "44000", "44010", "44020", "44110", "64000"
#                     ,"43000", "42200", "44100", "41200", "41150", "41050", "41100", "41300", "41586", "42100", "41400"]


#Remove All CSV file in Google Data, Website Data, Final Data
def remove_csv():
    files_in_directory = os.listdir(directory)
    filtered_files = [file for file in files_in_directory if file.endswith(".csv")]
    for file in filtered_files:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)

#To trick the browser to think that human are accessing the website (instead of robot)
#headers = {
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:84.0) Gecko/20181208 Chrome/55.0',
#}
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:84.0) Gecko/20181208 Chrome/55.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

for i in range(1,6):
    #Pick a random user agent
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent}
#Main Path
print(r"Main Folder eg : C:\Users\Administrator\Desktop\Webscrapping_Finale\Webscrapping_Finale")
Folder_Path = input("Enter the path of main folder : ")
Main_Path = Folder_Path.replace("\\", "\\")

directory = f"{Main_Path}\\1.Google_Data"
remove_csv()

directory = f"{Main_Path}\\2.Website_Data"
remove_csv()

directory = f"{Main_Path}\\3.Scrap_Data"
remove_csv()

directory = f"{Main_Path}\\4.Final_Data"
remove_csv()

directory = f"{Main_Path}\\4.Final_Data\\BeforeClean_RemoveDirectory"
remove_csv()

#CSV file location to be combine
os.chdir(f"{Main_Path}\\3.Scrap_Data")

#Page to Crawl
#user_input_maxpage = int(input("Enter Max No. of pages you want crawl(integer) : "))
final_output_csv = input("Final Output File (csv) name : ")
#Maximum_Data = int(input("Enter Maximum repetitions allowed before filtering(integer) : ")) 

#Start Page 
#Start_Page = input("Enter Your Google Search Start Page(integer) : ")

#Path to Webdriver
Path = f"{Main_Path}\\Webdriver\\chromedriver.exe"

#CSV file to be combined for final output
FO_Path = f"{Main_Path}\\4.Final_Data"
FO_Path_WithoutFilter = f"{Main_Path}\\4.Final_Data\\BeforeClean_RemoveDirectory"
BC_Path = f"{Main_Path}\\3.Scrap_Data"

#1.0 Read Keywords from Keyword.csv
data_keywords = pd.read_csv(f"{Main_Path}\\0.Company_Data\\Company.csv",encoding= 'ISO-8859-1')
read_keywords = data_keywords['Company_Name']

for keyword in read_keywords:
    x = 0
    now = datetime.now()
    DetailsDT = now.strftime("%d/%m/%Y %H:%M:%S")
    driver = webdriver.Chrome(executable_path = Path)
    #2.0 Automate the Search Process
    driver.get("https://www.google.com/")
    searchbox = driver.find_element_by_xpath("//input[@name='q']")
    searchbox.send_keys(f"{keyword}")
    searchbox.send_keys(Keys.RETURN)  
    time.sleep(10)    

    #3.0 Scrapped Main Link & Save inside different Google File
    with open(f"{Main_Path}\\1.Google_Data\\Google_{keyword}.csv", mode='w') as Page:      
        G_Page = csv.writer(Page)
        G_Page.writerow(["Current_Page","Current_URL"]) 
        MS = "Page 1 : " 
        URL_ = driver.current_url
        G_Page.writerow([MS, URL_]) 
        # N = 2                                                                               
        # while N <= int(f"{user_input_maxpage}"):                                            
        #     time.sleep(5)
        #     if len(driver.find_elements_by_css_selector(f"[aria-label='Page {N}']")) > 0:
        #         driver.find_element_by_css_selector(f"[aria-label='Page {N}']").click()
        #         driver.implicitly_wait(10)
        #         MS = f"Page {N} : "
        #         URL_ = driver.current_url                                             
        #         G_Page.writerow([MS, URL_]) 
        #         N = N + 1  
        #     else:                                                                                                                                           
        #         N = N + 1               
        driver.close()                                                                      
        driver.quit()  

    #4.0 Read Website Page URL & Crawl websites URL from keyword given & Give Header to Each keywords_Content
    G_Page_Reader = pd.read_csv(f"{Main_Path}\\1.Google_Data\\Google_{keyword}.csv")  
    G_Page_Reader.dropna(axis=0,how='any',thresh=None,subset=None,inplace=True)  
    G_Page_Reader.to_csv(f"{Main_Path}\\1.Google_Data\\Google_{keyword}.csv", index = False) 
    #G_Page_Reader = pd.read_csv(f"{Main_Path}\\1.Google_Data\\Google_{keyword}.csv")  
    #G_Page_Reader = pd.read_csv(f"{Main_Path}\\1.Google_Data\\Google_{keyword}.csv" , skiprows=[i for i in range(1, int(f"{Start_Page}"))], engine='python')  
    G_Page_Reader = pd.read_csv(f"{Main_Path}\\1.Google_Data\\Google_{keyword}.csv" , engine='python')    
    G_Page_URL = G_Page_Reader['Current_URL']

    for G_link in G_Page_URL:
        Page_URL = webdriver.Chrome(executable_path = Path)
        Page_URL.get(G_link)          
        Res = requests.get(Page_URL.current_url)                                           
        soup = BeautifulSoup(Res.text,'html.parser')                                                    
        with open(f"{Main_Path}\\2.Website_Data\\Keywords_Contents_{keyword}.csv", mode='a') as ContentData: 
            Content = csv.writer(ContentData)                                                                           
            for website in soup.find_all('div', class_="BNeawe UPmit AP7Wnd"):                          
                website = str(website).replace('<div class="BNeawe UPmit AP7Wnd">',"https://").replace("</div>", " ").split('›') 
                #title = str(website).replace('<div class="BNeawe UPmit AP7Wnd">'," ").replace("['https://", " ").replace('www.', " ").replace('.com'," ").replace('.my'," ").replace('.org'," ").replace("']", " ").split("',")
                website = website[0]
                #title = title[0]
                Content.writerow([x, DetailsDT, website])
                x = x + 1                                                                  
        ContentData.close()
        Page_URL.close()
        Page_URL.quit()

    #Give Header to each Columns
    time.sleep(5)
    df = pd.read_csv(f"{Main_Path}\\2.Website_Data\\Keywords_Contents_{keyword}.csv")                
    df.columns = ['Num', 'Date/Time','URL']
    df.to_csv(f"{Main_Path}\\2.Website_Data\\Keywords_Contents_{keyword}.csv", index = False) 

    #Read Specific Column from CSV file
    read_keywords_contents = pd.read_csv(f"{Main_Path}\\2.Website_Data\\Keywords_Contents_{keyword}.csv")
    URL_column = read_keywords_contents['URL']
    #URL_title = read_keywords_contents['Title']
    #5.0 Websrapping Phone No, Email & Title
    URL_LGTH = 1

    #for link,Title in zip(URL_column,URL_title):
    for link in URL_column:
        with open(f'{Main_Path}\\3.Scrap_Data\\Data_{URL_LGTH}.csv', mode='w') as Data:      
            S_Data = csv.writer(Data) 
            #S_Data.writerow(["Main Website","Title","Mobile/Phone Number", "Mail", "Address", "Address_Type2", "Selangor_Address", "Selangor_Address_Type_2"]) 
            S_Data.writerow(["Main Website","Mobile/Phone Number"]) 
            try:
                URL_csv = webdriver.Chrome(executable_path = Path)
                URL_csv.implicitly_wait(20)
                start = time.time()
                URL_csv.get(link)
                res1 = requests.get(URL_csv.current_url, headers=headers, timeout=100)
                print(res1)
                #Title = Title.title()
                #print(Title)
                print(URL_csv.current_url)
                soup1 = BeautifulSoup(res1.text,'html.parser')
                SE = str(soup1)
                #Emails = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", SE)
                #Address = re.findall(r"[\d\s]*[a-zA-Z0-9\s]*[,\s]{0,3}",SE)
                #Address_2 = re.findall(r"[0-9A-Z\s]{0,3}[a-zA-Z,\s]*[<A-Z0-9]{0,8}[,\\s]{0,2}[a-zA-Z\s]*[,]{0,1}[\a-zA-Z\s]{0,3}[\d]{5}[\s*]+[a-zA-Z]*[\s*]{0,5}[a-zA-Z]*[\s]{0,5}[,]{1,5}[\s]{0,5}[a-zA-Z]*", SE)
                Address = re.findall(r"[a-zA-Z0-9\s]*[,][\s]{0,3}[a-zA-Z\s]*[,][\s]{0,3}[a-zA-z \s]*[,][\s]{0,3}[\d]{5}",SE)
                #WL1 = r"\+?[\d\s]+[-–—]{0,1}[\d\s]+" #+6012-123 1242
                #Address_2 = re.findall(r"[a-zA-Z]{3,10}[\s]{0,1}[a-zA-Z]{3,10}[,]{1}[0-9\s]{7}[a-zA-Z\s]{0,20}[,]{1}[\s]{0,1}[a-zA-Z]{0,20}",SE)

                SE1 = SE.replace("&ndash;","-").replace("&mdash;","-")
                WL1 = r"\+?[\d\s]{0,6}[-]{0,1}[\d\s]{5,10}" 
                WLPhones1 = re.findall(WL1, SE1)

                for m1 in WLPhones1:
                    m1 = m1.strip()
                    if not (m1.startswith("03") or m1.startswith("04") or m1.startswith("+60") or m1.startswith("05") or m1.startswith("06") or
                            m1.startswith("07") or m1.startswith("09") or m1.startswith("081") or m1.startswith("082") or m1.startswith("083") or
                            m1.startswith("084") or m1.startswith("085") or m1.startswith("086") or m1.startswith("087") or m1.startswith("088") or
                            m1.startswith("010") or m1.startswith("011") or m1.startswith("012") or m1.startswith("013") or m1.startswith("014") or 
                            m1.startswith("016") or m1.startswith("017") or m1.startswith("018") or m1.startswith("019")):
                        continue

                    noOfNumbers = re.findall(r"\d", m1)
                    m1 = m1.lstrip("+")
                    if len(m1) < 10 or len(m1) > 15 or len(noOfNumbers) > 11 or len(noOfNumbers) < 9:
                        continue

                    d1 = m1
                    #S_Data.writerow([URL_csv.current_url,Title,d1,0,0,0,0,0])
                    S_Data.writerow([URL_csv.current_url,d1])
                else:
                    #S_Data.writerow([URL_csv.current_url,Title,"NA",0,0,0,0,0])
                    S_Data.writerow([URL_csv.current_url,"NA"])     
                # for mail in Emails:
                #     mail = mail.strip()
                #     if not (mail.endswith(".com") or mail.endswith(".my")):
                #         continue

                #     f = mail
                #     S_Data.writerow([URL_csv.current_url,Title,0,f,0,0,0,0])
                # else:
                #     S_Data.writerow([URL_csv.current_url,Title,0,"NA",0,0,0,0])

                # for alamat in Address:
                #     #if len(alamat) < 12:
                #     #    continue
                #     if any(ext in alamat for ext in Selangor_Postcode) and len(alamat) > 12:
                #         h = alamat
                #         S_Data.writerow([URL_csv.current_url,Title,0,0,0,0,h,0])
                #     else:
                #         g = alamat
                #         S_Data.writerow([URL_csv.current_url,Title,0,0,g,0,0,0])
                # else:
                #     S_Data.writerow([URL_csv.current_url,Title,0,0,"NA",0,0,0])

                # for alamat_2 in Address_2:
                #     #if len(alamat_2) < 12:
                #     #    continue
                #     if any(ext in alamat_2 for ext in Selangor_Postcode) and len(alamat_2) > 12:
                #         h1 = alamat_2
                #         S_Data.writerow([URL_csv.current_url,Title,0,0,0,0,0,h1])
                #     else:
                #         g1 = alamat_2
                #         S_Data.writerow([URL_csv.current_url,Title,0,0,0,g1,0,0])
                # else:
                #     S_Data.writerow([URL_csv.current_url,Title,0,0,0,"NA",0,0])
                
            except:
                print("Oops!", sys.exc_info()[0], "occurred.")
                print("Next entry.")
                print()
        
        end = time.time()
        print("Total Time(in seconds) : "+"{:.2f}".format(end - start))
        URL_LGTH = URL_LGTH + 1
        URL_csv.close()
        URL_csv.quit()   

    
    #6.0 Combine All to 1 CSV file
    all_data_files = glob.glob(os.path.join(BC_Path, "Data_*.csv"))
    df_from_each_data_file = (pd.read_csv(f, sep=',',engine='python') for f in all_data_files)
    df_merged_data = pd.concat(df_from_each_data_file, ignore_index=True)
    df_merged_data.to_csv(f"{Main_Path}\\4.Final_Data\\BeforeClean_RemoveDirectory\\Combined_{keyword}.csv",index = False)

    #7.0 Cleaning Data(remove duplicated phone number) and remove data that are considered directory
    data = pd.read_csv(f"{Main_Path}\\4.Final_Data\\BeforeClean_RemoveDirectory\\Combined_{keyword}.csv")
    frame = pd.DataFrame(data)
    frame = frame.dropna().replace("0", "NA").replace("0.0","NA").drop_duplicates()
    frame.to_csv(f"{Main_Path}\\4.Final_Data\\Combined_{keyword}.csv", index=False)
    #Remove data that are considered directory, above 20 datas
    data_clean = pd.read_csv(f"{Main_Path}\\4.Final_Data\\Combined_{keyword}.csv")
    df_remove = pd.DataFrame(data_clean)
    vc = df_remove["Main Website"].value_counts()
    to_remove = vc[vc>=50].index
    save = df_remove[~df_remove['Main Website'].isin(to_remove)]
    save.to_csv(f"{Main_Path}\\4.Final_Data\\Combined_{keyword}.csv", index = False)
    #data Add Keywords Column
    data_addcolumn = pd.read_csv(f"{Main_Path}\\4.Final_Data\\Combined_{keyword}.csv")
    df_add = pd.DataFrame(data_addcolumn)
    df_add.insert(0,"Keywords", f"{keyword}", allow_duplicates=False)
    df_add.to_csv(f"{Main_Path}\\4.Final_Data\\Combined_{keyword}.csv",index = False)
    #Final Output CSV file
    all_files = glob.glob(os.path.join(FO_Path, "Combined_*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',',engine='python') for f in all_files)
    df_merged   = pd.concat(df_from_each_file, ignore_index=True)
    df_merged.to_csv(f"{Main_Path}\\5.All Data Combined\\{final_output_csv}.csv",index = False)
    #Final Output without Filter CSV File
    all_files = glob.glob(os.path.join(FO_Path_WithoutFilter, "Combined_*.csv"))
    df_from_each_file = (pd.read_csv(f, sep=',',engine='python') for f in all_files)
    df_merged   = pd.concat(df_from_each_file, ignore_index=True)
    df_merged.to_csv(f"{Main_Path}\\5.All Data Combined\\{final_output_csv}_withoutfilter.csv",index = False)
    #Clean_Data
    Read = pd.read_csv(f"{Main_Path}\\5.All Data Combined\\{final_output_csv}.csv", engine='python')
    Read_Data = pd.DataFrame(Read)
    Read_Data = Read_Data.fillna("NA")
    Read_Data.to_csv(f"{Main_Path}\\5.All Data Combined\\{final_output_csv}.csv", index=False)
    #8.0 Remove all related csv file for next keywords data
    directory = f"{Main_Path}\\3.Scrap_Data"
    remove_csv()