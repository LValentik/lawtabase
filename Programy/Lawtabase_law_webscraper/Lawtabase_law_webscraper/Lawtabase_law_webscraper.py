import psycopg2
import requests
from bs4 import BeautifulSoup

#print("https")
#https = input()
#print("html")
#html = input()
#print("html2")
#html2 = input()
#print("clas")
#clas = input()
print("clas2")
#clas2 = input()
print("count")
#count = int(input())
print("table")
#table = input()
print("num")
num = int(input())
con = psycopg2.connect(host="localhost", port="5432", user="postgres", password="VaL123eNt456Ik789.", database="Lawtabase")

cur = con.cursor()
#for x in range(1, count):
add = num
r = requests.get("https://www.kurzy.cz/zakony/89-2012-obcansky-zakonik/paragraf-1")
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll("div", id_='zneni_zakona')
   
    
for link in links:
    cur.execute("""INSERT INTO cz_leg.oz_89_2012_sb (paragraph, law)
                VALUES (%s, %s)""",
                ( add,
                  link.find_all('p', class_='odstavec')
                )
    )
              
                    
    
                    
        
con.commit()
cur.close()
con.close()