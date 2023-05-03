import psycopg2
import requests
from bs4 import BeautifulSoup

# Establish database connection
con = psycopg2.connect(host="localhost",
                       port="5432",
                       user="postgres",
                       password="VaL123eNt456Ik789.",
                       database="Lawtabase")
#check if connection is established
print(con.get_dsn_parameters())
cur = con.cursor()
for x in range(0, 397):
    link = "https://www.kurzy.cz/zakony/40-2009-trestni-zakonik/paragraf-"
    linkfin = link + str(x)
    r = requests.get(linkfin)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.findAll('div', id='zneni_zakona')
    for link in links:
        conf = str(link.find('p', class_='parag').text)
        name = str(link.find('h2', class_='parag_n'))
        name = name.replace('<h2 class="parag_n">', '')
        name = name.replace('</h2>', '')   
        odst = str(link.find_all('p'))
        odst = odst.replace('<p class="parag">', '')
        odst = odst.replace(conf, '')
        odst = odst.replace('<p class="odst">', '')
        odst = odst.replace('<p class="odst">', '')
        odst = odst.replace('<p class="pism">', '')          
        odst = odst.replace('<p class="parag_t">', '')
        odst = odst.replace('<p class="pism">', '')
        odst = odst.replace('</p>', '')
        odst = odst.replace('[', '')
        odst = odst.replace(']', '')
        odst = odst.replace(',', '')
        odst_soup = BeautifulSoup(odst, 'html.parser')
        for link in odst_soup.find_all('a'):
            link.replace_with('')
        odst = odst_soup.get_text(strip=True)
        cur.execute("""INSERT INTO cz_leg.zp_262_2006_sb (paragraph_num, paragraph_text, law) VALUES (%s, %s, %s)""",
            (
                x,
                conf,
                odst,

                		

        )
        )
    con.commit()
    
    print("Law no.", x,"has been scraped.")
print("Scraping completed!")
cur.close()
con.close()



                    