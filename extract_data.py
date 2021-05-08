# -*- coding: utf-8 -*-
from json import JSONEncoder
import re
import os
from os.path import isfile, join
from os import listdir
import PIL
import pytesseract
from pdf2image import*
from pprint import pprint
import json
from datetime import date, time, datetime

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import pdf2image
from PyPDF2 import PdfFileReader
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

data = {}
data["janvier"] = []
data["février"] = []
data["mars"] = []
data["avril"] = []
data["mai"] = []
data["juin"] = []
data["juillet"] = []
data["août"] = []
data["septembre"] = []
data["octobre"] = []
data["novembre"] = []
data["décembre"] = []

donnees = {}
commune = {}
jour=mois=annee=NbTest=NbCasCom=NbCas=NbCasContacts=NbDeces=NbGueris=None

def getvalue(name: str, data: str) -> int:
    lines = data.split('\n')

    for i, line in enumerate(lines):
        Localite = re.search(re.escape(name), line, re.IGNORECASE)

        if(Localite):
            cas = re.search('\d+( )+', line, re.IGNORECASE)
            if (re.search(re.escape(name)+' \(\d+\)', line, re.IGNORECASE) or re.search('\(\d+\), '+re.escape(name), line, re.IGNORECASE)):
                entre=True;
                return 100;
            if cas:
                return int(cas.group())
            else:
                while i > 0:
                    cas = re.search(
                        '\d+( )+', lines[i], re.IGNORECASE)

                    if cas:
                        return int(cas.group())
                    i -= 1

                return 0

    return None


# Convert PDF contents to pages
print("Extraction des donnees....")
print("Creation des fichiers json....")
for element in os.listdir('C:\\Users\\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\\Projet_SGBD\\telechargement_COMMUNIQUES'):
    print(element)
    pages = pdf2image.convert_from_path("C:\\Users\\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\\Projet_SGBD\\telechargement_COMMUNIQUES\\"+element, poppler_path='C:\\Program Files (x86)\\poppler-0.68.0\\bin')
    # entre=False
    # Just using this to give the pages a number
    for page in pages:
            j = 0
            counter = 0
            file_name = 'page' + str(counter) + '.jpg'
            # Save images to the same folder
            page.save(file_name, 'JPEG')
            # Open the file as an image
            image_file = PIL.Image.open(file_name)
            # Use tesseract to extract the text from the image
            string_contents = pytesseract.image_to_string(image_file)
            #print(string_contents)
            
            jour = re.search('Ce (Lundi|Mardi|Mercredi|Jeudi|Vendredi|Samedi|Dimanche)(.)*(,)', string_contents,re.IGNORECASE)
            if(jour):
                jourr = re.search('\d+', jour.group(),re.IGNORECASE)
            mois = re.search(
                'Janvier|Février|Mars|Avril|Mai|Juin|Juillet|Août|Septembre|Octobre|Novembre|Décembre', string_contents,re.IGNORECASE)
            annee = re.search(' 2020| 2021', string_contents,re.IGNORECASE)
            if(re.search('\d+ tests', string_contents,re.IGNORECASE)):
                NbTest = re.search('\d+', (re.search('\d+ tests', string_contents,re.IGNORECASE)).group(),re.IGNORECASE)

            if(re.search('\d+ sont (.)evenus positifs', string_contents,re.IGNORECASE)):
                NbCas = re.search('\d+', (re.search('\d+ sont (.)evenus positifs', string_contents,re.IGNORECASE)).group(),re.IGNORECASE)

            if(re.search('\d+(.)+contacts', string_contents,re.IGNORECASE)):
                NbCasContacts = re.search('\d+', (re.search('\d+(.)+contacts', string_contents,re.IGNORECASE)).group(),re.IGNORECASE)

            if(re.search('\d+(.)+communautaire', string_contents,re.IGNORECASE)):
                NbCasCom = re.search('\d+', (re.search('\d+(.)+communautaire', string_contents,re.IGNORECASE)).group(),re.IGNORECASE)

            if(re.search('\d+(.)+décés', string_contents,re.IGNORECASE)):
                NbDeces = re.search('\d+',(re.search('\d+(.)+décés', string_contents,re.IGNORECASE)).group(),re.IGNORECASE)

            if(re.search('\d+(.)+négatifs', string_contents,re.IGNORECASE)):
                NbGueris = re.search('\d+',(re.search('\d+(.)+négatifs', string_contents,re.IGNORECASE)).group(),re.IGNORECASE) 

            if mois and annee and jour and NbCas and NbCasContacts and NbTest and NbCasCom:
                print(jourr.group(),"111111111111")
                print(mois.group(),"22222222222")
                # jourr.group().lower
                if(jourr.group()=='1' or jourr.group()=='2' or jourr.group()=='3' or jourr.group()=='4' or jourr.group()=='5' or jourr.group()=='6' or jourr.group()=='7' or jourr.group()=='8' or jourr.group()=='9'):
                    jourr= '0'+jourr.group()
                else:
                    jourr= jourr.group()
                if(mois.group().lower()=='janvier'):
                    numm= '01'   
                if(mois.group().lower()=='février'):
                    numm= '02'   
                if(mois.group().lower()=='mars'):
                    numm= '03' 
                if(mois.group().lower()=='avril'):
                    numm= '04'
                if(str(mois.group().lower())=='mai'):
                    numm= '05' 
                if(mois.group().lower()=='juin'):
                    numm= '06'   
                if(mois.group().lower()=='juillet'):
                    numm= '07'
                if(mois.group().lower()=='août'):
                    numm= '08'
                if(mois.group().lower()=='septembre'):
                    numm= '09'   
                if(mois.group().lower()=='octobre'):
                    numm= '10'  
                if(mois.group().lower()=='novembre'):
                    numm= '11'
                if(mois.group().lower()=='décembre'):
                    numm= '12'
                donnees = {
                    "la_date": annee.group()+'-'+numm+'-'+jourr,
                    "Nb_Test": int(NbTest.group()),
                    "Nb_nouveaux_Cas": int(NbCas.group()),
                    "Nb_Cas_Contacts": int(NbCasContacts.group()),
                    "Nb_Cas_Communautaires": int(NbCasCom.group()),
                    "NomFichierSource": element,
                    "DateHeureExtraction": str(date.today()),
                    "mois": str(mois.group())
                }
            if(NbDeces):
                donnees["Nb_Deces"] = int(NbDeces.group())
            if(NbGueris):
                donnees["Nb_Gueris"] = int(NbGueris.group())

            Leslocalites = ('Guédiawaye|Almadies|Gorée|Plateau|Gueule Tapée|Fass|Colobane|Fann-Point E-Amitié|Médina|Grand-Dakar|Biscuiterie|Dieuppeul-Derklé|Hann-Bel-Air|Sicap-Liberté|HLM|Mermoz-Sacré Coeur|Ouakam|Ngor|Yoff|Grand-Yoff|Patte d’oie|Parcelles Assainies|Cambérène|Ville de Guédiawaye|Golf-Sud|Sam-Notaire|Ndiarème-Limamoulaye|Wakhinane|Médina Gounass|Ville de Pikine|Pikine-Est|Pikine-Nord|Pikine-Ouest|Dalifort|Djeddha Thiaroye Kao|Guinaw Rail-Nord|Guinaw Rail-Sud|Thiaroye Gare|Thiaroye sur Mer|Tivaoune-Diacksao|Diamagueune-Sicap Mbao|Mbao|Keur Massar|Malika|Yeumbeul|Rufisque|Bargny|Sébikotane|Sendou|Rufisque-Est|Rufisque-Nord|Rufisque-Ouest|Bambylor|Yène|Tivaouane Peulh-Niaga|Diamniadio|Sangalkam|Jaxaay-Parcelles-Niakoul Rap|Diourbel|Ndoulo|Ngohe|Pattar|Tocky Gare|Touré Mbondé|Ndankh Séne|Gade Escale|Touba Lappé|Keur  Ngalgou|Ndindy|Taïba Moutoupha|Bambey|Dinguiraye|Baba  Garage|Keur Samba Kane|Ngoye|Thiakhar|Ndondol|Ndangalma|Lambaye|Réfane|Gawane|Ngogom|Mbacké|Touba Mosquée|Dalla Ngabou|Missirah|Nghaye|Touba Fall|Darou Salam Typ|Darou Nahim|Kael|Madina|Touba Mboul|Taïba Thièkène|Dendèye Gouy Gui|Ndioumane|Taïf|Sadio|Fatick|Dioffior|Thiaré Ndialgui|Diaoulé|Mbéllacadiao|Ndiop|Diakhao|Djilasse|Fimela|Loul Sessène|Palmarin Facao|Niakhar|Ngayokhème|Patar|Diarrère|Diouroup|Tattaguine|Foundiougne|Sokone|Keur Saloum Diané|Keur Samba Gueye|Toubacouta|Nioro Alassane Tall|Karang Poste|Passy|Soum|Diossong|Djilor|Niassène|Diagane Barka|Mbam|Bassoul|Dionewar|Djirnda|Gossas|Colobane|Mbar|Ndiene Lagane|Ouadiour|Patar Lia|Kaffrine|Nganda|Diamagadio|Diokoul Belbouck|Kathiotte|Médinatoul Salam 2|Gniby|Boulel|Kahi|Birkelane|Keur Mboucki|Touba Mbella|Diamal|Mabo|Ndiognick|Ségré-gatta|Mbeuleup|Malème-Hodar|Darou Miname II|Khelcom|Ndioum Ngainth|Ndiobène Samba Lamo|Sagna|Dianké Souf|Koungheul|Missirah Wadène|Maka Yop|Ngainthe Pathé|Fass Thièkène|Saly|Ida Mouride|Ribot Escale|Lour Escale|Kaolack|Kahone|Keur Baka|Latmingué|Thiaré|Ndoffane|Keur Socé|Ndiaffat|Ndiedieng|Dya|Ndiébel|Thiomby|Gandiaye|Sibassor|Guinguinéo|Guinguinéo|Khelcom – Birane|Mbadakhoune|Ndiago|Ngathie Naoudé|Fass|Gagnick|Dara Mboss|Nguélou|Ourour|Panal Ouolof|Mboss|Nioro du Rip|Kayemor|Médina Sabakh|Ngayene|Gainthe Kaye|Dabaly|Darou Salam|Paos Koto|Porokhane|Taïba Niassène|Keur Maba Diakhou|Keur Madongo|Ndramé Escale|Wack Ngouna|Keur Madiabel|Kédougou|Ninéfécha|Bandafassi|Tomboroncoto|Dindefelo|FONGOLIMBI|Fongolimbi|Dimboli|Salémata|Kévoye|Dakatéli|Ethiolo|Oubadji|Dar salam|Saraya|Bembou|Médina Baffé|Sabodala|Khossanto|Missirah Sirimana|Kolda|Dialambéré|Médina Chérif|Mampatim|Coumbacara|Bagadadji|Dabo|Thiétty|Saré Bidji|Guiro Yéro Bocar|Dioulacolon|Tankanto Escale|Médina El hadj|Salykégné|Saré Yoba Diéga|Médina Yoro Foulah|Badion|Fafacourou|Bourouco|Bignarabé|Ndorna|Koulinto|Niaming|Dinguiraye|Pata|Kéréwane|Vélingara|Vélingara|Diaobé-Kabendou|Kounkané|Kandia|Saré Coly Sallé|Kandiaye|Némataba|Pakour|Paroumba|Ouassadou|Bonconto|Linkering|Médina Gounass|Sinthiang Koundara|Louga|Coki|Ndiagne|Guet Ardo|Thiamène Cayor|Pété Ouarack|Keur Momar Sarr|Nguer Malal|Syer|Gande|Mbédiene|Niomré|Nguidilé|Kéle Gueye')
            Leslocalites1 = ('Sakal|Léona|Sakal|Ngueune Sarr|Kébémer|Bandegne Ouolof|Diokoul Diawrigne|Kab Gaye|Ndande|Thieppe|Guéoul|Mbacké Cajor|Darou Marnane|Darou Mousty|Mbadiane|Ndoyene|Sam Yabal|Touba Mérina|Ngourane Ouolof|Thiolom Fall|Sagatta Gueth|Kanène Ndiob|Loro|Linguére|Dahra|Barkédji|Gassane|Thiargny|Thiel|Boulal|Dealy|Thiamène Pass|Sagatta Djolof|Affé Djolof|Dodji|Labgar|Ouarkhokh|Kamb|Mboula|Téssékéré Forage|Yang-Yang|Mbeuleukhé|Matam|Ourossogui|Thilogne|Nguidjilone|Dabia|Des Agnam|Oréfondé|Bokidiawé|Nabadji Civol|Ogo|Kanel|Odobéré|Wouro Sidy|Ndendory|Sinthiou Bamambé Banadji|Hamady Hounaré|Aouré|Bokiladji|Orkadiéré|Ouaoundé|Semmé|Dembancané|Ranérou|Lougré Thioly|Oudalaye|Vélingara|Saint-Louis|Saint Louis|Mpal|Fass Ngom|Ndiébène Gandiol|Gandon|Dagana|Richard Toll|Ross-Béthio|Rosso-Sénégal|Ngnith|Diama|Ronkh|Ndombo Sandjiry|Gae|Bokhol|Mbane|Ndioum|Podor|Méry|Doumga Lao|Madina Diathbé|Golléré|Mboumba|Walaldé|Aéré Lao|Gamadji Saré|Dodel|Guedé Village|Guédé Chantier|Démette|Bodé Lao|Fanaye|Ndiayene Peindao|Niandane|Mbolo Birane|Boké Dialloubé|Galoya Toucouleur|Pété|Sédhiou|Marssassoum|Djiredji|Bambaly|Oudoucar|Sama Kanta Peulh|Diannah Ba|Koussy|Sakar|Diendé|Diannah Malary|San Samba|Bémet Bidjini|Djibabouya|Bounkiling|Bounkiling|Ndiamacouta|Boghal|Tankon|Ndiamalathiel|Djinany|Diacounda|Inor|Kandion Mangana|Bona|Diambati|Faoune|Diaroumé|Madina Wandifa|Goudomp|Diattacounda|Samine|Yarang Balante|Mangaroungou Santo|Simbandi Balante|Djibanar|Kaour|Diouboudou|Simbandi Brassou|Baghère|Niagha|Tanaff|Karantaba|Kolibantang|Tambacounda|Tambacounda|Niani Toucouleur|Makacolibantang|Ndoga Babacar|Missirah|Néttéboulou|Dialacoto|Sinthiou Malème|Koussanar|Kothiary|Goudiry|Boynguel Bamba|Sinthiou Mamadou Boubou|Koussan|Dougué|Dianké Makha|Boutoucoufara|Bani Israel|Sinthiou Bocar Aly|Koulor|Komoti|Bala|Koar|Goumbayel|Bakel|BELE|Bélé|Sinthiou Fissa|Kidira|Toumboura|Sadatou|Madina Foulbé|Gathiary|Moudery|Ballou|Gabou|Diawara|Koumpentoum|Koumpentoum|Malem Niany|Ndame|Méréto|Kahène|Bamba Thialène|Payar|Kouthiaba|Wolof|Kouthia Gaydi|Pass Coto|Malem Niany|Ville de Thiès|Khombole|Pout|Thiès Ouest|Thiès Est|Thiès Nord|Thiénaba|Ngoudiane|Ndiéyène Sirakh|Touba Toul|Keur Moussa|Diender|Fandène|Kayar|Notto|Tassète|Mbour|Joal Fadiouth|Fissel|Ndiaganiao|Sessene|Sandiara|Nguéniène|Thiadiaye|Sindia|Malicounda|Diass|Nguékhokh|Saly Portudal|Ngaparou|Somone|Popenguine-Ndayane|Tivaouane|Tivaouane|Mékhé|Mboro|Méouane|Darou Khoudoss|Taïba Ndiaye|Mérina Dakhar|Koul|Pékèsse|Niakhène|Mbayène|Thilmakha|Ngandiouf|Notto Gouye Diama|Mont Rolland|Pire Goureye|Chérif Lo|Pambal|Ziguinchor|Ziguinchor|Niaguis|Adéane|Boutoupa Camaracounda|Niassia|Enampore|Bignona|Thionck Essyl|Kataba 1|Djinaky|Kafountine|Diouloulou|Tenghori|Niamone|Ouonck|Coubalan|Balinghore|Diégoune|Kartiack|Mangagoulack|Mlomp|Djibidione|Oulampane|Sindian|Suelle|Oussouye|Diembéring|Santhiaba Manjack|Oukout|Mlomp|Dakar|Diourbel|Fatick|Kaffrine|Kaolack|Kédougou|Kolda|Louga|Matam|Saint-Louis|Sédhiou|Tambacounda|Thiés|Ziguinchor')
            locals = Leslocalites.split('|')
            locals1 = Leslocalites1.split('|')
            k = 1

            locals.extend(locals1)
            # donnees['communes']=None
            for local in locals:
                value = getvalue(local, string_contents)
                if(value==100):
                    break
                if value is not None and value!=0:
                    commune[local] = value
            donnees['communes']=commune
                    

    if((mois is not None) and (annee is not None) and value!=100):
        data[mois.group().lower()].append(donnees)
        with open("C:\\Users\\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\\Projet_SGBD\\Fichier JSON\\"+annee.group()+"-"+mois.group().lower()+".json", "w", encoding="utf-8") as file:
            json.dump(data[mois.group().lower()], file, indent=4, ensure_ascii=False)
            file.write('\n')
        commune = {}


print("Successful!")
