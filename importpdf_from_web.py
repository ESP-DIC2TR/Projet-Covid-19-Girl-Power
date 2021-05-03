import urllib.request
import requests
import time
import datetime
from bs4 import BeautifulSoup
from urllib.request import unquote
import sys
import os
import os.path
import random
import PIL
import pytesseract
from pdf2image import*
from pprint import pprint
import json

from pdf2image import convert_from_path,convert_from_bytes
from pdf2image.exceptions import (
PDFInfoNotInstalledError,
PDFPageCountError,
PDFSyntaxError
)
print("Exportation locale des fichiers pdf...")

def getuserAgent():
  lines=open('user-agents.txt').read().splitlines()
  return {'User-Agent': random.choice(lines)}

def pdf_download(url,file_name):
  dir_path=os.path.dirname(os.path.realpath(__file__))
  file_path=dir_path+'\\telechargement_COMMUNIQUES\\'+file_name+'.pdf'
  response = requests.get(url,headers=getuserAgent())
  expdf=response.content
  egpdf=open(file_path,'wb')
  egpdf.write(expdf)
  egpdf.close()





url = "http://www.sante.gouv.sn/Pr%C3%A9sentation/coronavirus-informations-officielles-et-quotidiennes-du-msas/"

print('HTTP GET: %s',url)
  # Exécuter la requête GET
response = requests.get(url,headers=getuserAgent())
#print(response.iter_content())
if response.ok:
  soup=BeautifulSoup(response.text,'html.parser')
   #recuperer touts les liens du site
  tds=soup.findAll('a')
   #afficher le nombre de liens dans le site
  
  #boucle qui parcours le nombre de liens
  i=0
  for url in tds:
    
    try:

      
      if 'pdf' in url['href']:
        pdf_url=' '
        if 'https' not in url['href']:
          pdf_url=url['href']
        else:
          pdf_url=url['href']
        print('HTTP GET:%s',pdf_url)
        

        #faire une requete https pour chercher les pdf
        pdf_response=requests.get(pdf_url,headers=getuserAgent())

        #extraire nom pdf
        
        file_name=pdf_response
        

         


        # pdf_download(" http://www.sante.gouv.sn/sites/default/sitrep15covid19.pdf","communique3")
        pdf_download(pdf_url, "communique n"+str(i))
        i=i+1
        
        time.sleep(1)
         

        #skip tous les url qui ne sont pas des pdf
    except Exception as e:
         print('Error:',e)

print("Successful...")
