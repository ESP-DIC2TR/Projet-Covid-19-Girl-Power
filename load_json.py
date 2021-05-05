# -*- coding: utf-8 -*-
import simplejson
import mysql.connector
import json
import os.path



# print("Chargement a la base....")
# con = mysql.connector.connect(host="localhost",user="root",password="Mysql123",db="base")
# cursor=con.cursor(buffered=True)

print("Connexion a la base de donnees...")

# base_covid19=open("C:\\Users\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\\Projet_SGBD\\BD_covid.sql").read()
# cursor.execute(base_covid19,multi=True)
conn = mysql.connector.connect(host="localhost",user="root",password="Mysql123",db="basee")
cursor_covid=conn.cursor(buffered=True)

print("Chargement des json files....")
for element in os.listdir('C:\\Users\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\\Projet_SGBD\\Fichier json'):
    json_file_path = "C:\\Users\\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\Projet_SGBD\\Fichier json\\"+element
    print(element)

    json_data=open(json_file_path )
    json_obj=json.loads(json_data.read())

    for item in json_obj:
        print(item.get("la_date"))
        la_date=item.get("la_date")
        Nb_Test=item.get("Nb_Test")
        Nb_nouveaux_Cas=item.get("Nb_nouveaux_Cas")
        Nb_Cas_Contacts=item.get("Nb_Cas_Contacts")
        Nb_Cas_Communautaires=item.get("Nb_Cas_Communautaires")
        Nb_Deces=item.get("Nb_Deces")
        Nb_Gueris=item.get("Nb_Gueris")
        NomFichierSource=item.get("NomFichierSource")
        DateHeureExtraction=item.get("DateHeureExtraction")
        mois=item.get("mois")
        id_communique=0
        cursor_covid.execute("INSERT INTO  communique(la_date,Nb_Test,Nb_nouveaux_Cas,Nb_Cas_Contacts,Nb_Cas_Communautaires,Nb_Gueris,Nb_Deces,NomFichierSource,DateHeureExtraction,mois) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(la_date,Nb_Test,Nb_nouveaux_Cas,Nb_Cas_Contacts,Nb_Cas_Communautaires,Nb_Gueris,Nb_Deces,NomFichierSource,DateHeureExtraction,mois))	
        
        Leslocalites = ('Guédiawaye|Almadies|Gorée|Plateau|Gueule Tapée|Fass|Colobane|Fann-Point E-Amitié|Médina|Grand-Dakar|Biscuiterie|Dieuppeul-Derklé|Hann-Bel-Air|Sicap-Liberté|HLM|Mermoz-Sacré Coeur|Ouakam|Ngor|Yoff|Grand-Yoff|Patte d’oie|Parcelles Assainies|Cambérène|Ville de Guédiawaye|Golf-Sud|Sam-Notaire|Ndiarème-Limamoulaye|Wakhinane|Médina Gounass|Ville de Pikine|Pikine-Est|Pikine-Nord|Pikine-Ouest|Dalifort|Djeddha Thiaroye Kao|Guinaw Rail-Nord|Guinaw Rail-Sud|Thiaroye Gare|Thiaroye sur Mer|Tivaoune-Diacksao|Diamagueune-Sicap Mbao|Mbao|Keur Massar|Malika|Yeumbeul|Rufisque|Bargny|Sébikotane|Sendou|Rufisque-Est|Rufisque-Nord|Rufisque-Ouest|Bambylor|Yène|Tivaouane Peulh-Niaga|Diamniadio|Sangalkam|Jaxaay-Parcelles-Niakoul Rap|Diourbel|Ndoulo|Ngohe|Pattar|Tocky Gare|Touré Mbondé|Ndankh Séne|Gade Escale|Touba Lappé|Keur  Ngalgou|Ndindy|Taïba Moutoupha|Bambey|Dinguiraye|Baba  Garage|Keur Samba Kane|Ngoye|Thiakhar|Ndondol|Ndangalma|Lambaye|Réfane|Gawane|Ngogom|Mbacké|Touba Mosquée|Dalla Ngabou|Missirah|Nghaye|Touba Fall|Darou Salam Typ|Darou Nahim|Kael|Madina|Touba Mboul|Taïba Thièkène|Dendèye Gouy Gui|Ndioumane|Taïf|Sadio|Fatick|Dioffior|Thiaré Ndialgui|Diaoulé|Mbéllacadiao|Ndiop|Diakhao|Djilasse|Fimela|Loul Sessène|Palmarin Facao|Niakhar|Ngayokhème|Patar|Diarrère|Diouroup|Tattaguine|Foundiougne|Sokone|Keur Saloum Diané|Keur Samba Gueye|Toubacouta|Nioro Alassane Tall|Karang Poste|Passy|Soum|Diossong|Djilor|Niassène|Diagane Barka|Mbam|Bassoul|Dionewar|Djirnda|Gossas|Mbar|Ndiene Lagane|Ouadiour|Patar Lia|Kaffrine|Nganda|Diamagadio|Diokoul Belbouck|Kathiotte|Médinatoul Salam 2|Gniby|Boulel|Kahi|Birkelane|Keur Mboucki|Touba Mbella|Diamal|Mabo|Ndiognick|Ségré-gatta|Mbeuleup|Malème-Hodar|Darou Miname II|Khelcom|Ndioum Ngainth|Ndiobène Samba Lamo|Sagna|Dianké Souf|Koungheul|Missirah Wadène|Maka Yop|Ngainthe Pathé|Fass-Thièkène|Saly|Ida Mouride|Ribot Escale|Lour Escale|Kaolack|Kahone|Keur Baka|Latmingué|Thiaré|Ndoffane|Keur Socé|Ndiaffat|Ndiedieng|Dya|Ndiébel|Thiomby|Gandiaye|Sibassor|Guinguinéo|Guinguinéo|Khelcom – Birane|Mbadakhoune|Ndiago|Ngathie Naoudé|Gagnick|Dara Mboss|Nguélou|Ourour|Panal Ouolof|Mboss|Nioro du Rip|Kayemor|Médina Sabakh|Ngayene|Gainthe Kaye|Dabaly|Darou Salam|Paos Koto|Porokhane|Taïba Niassène|Keur Maba Diakhou|Keur Madongo|Ndramé Escale|Wack Ngouna|Keur Madiabel|Kédougou|Ninéfécha|Bandafassi|Tomboroncoto|Dindefelo|FONGOLIMBI|Fongolimbi|Dimboli|Salémata|Kévoye|Dakatéli|Ethiolo|Oubadji|Dar salam|Saraya|Bembou|Médina Baffé|Sabodala|Khossanto|Missirah Sirimana|Kolda|Dialambéré|Médina Chérif|Mampatim|Coumbacara|Bagadadji|Dabo|Thiétty|Saré Bidji|Guiro Yéro Bocar|Dioulacolon|Tankanto Escale|Médina El hadj|Salykégné|Saré Yoba Diéga|Médina Yoro Foulah|Badion|Fafacourou|Bourouco|Bignarabé|Ndorna|Koulinto|Niaming|Dinguiraye|Pata|Kéréwane|Vélingara|Vélingara|Diaobé-Kabendou|Kounkané|Kandia|Saré Coly Sallé|Kandiaye|Némataba|Pakour|Paroumba|Ouassadou|Bonconto|Linkering|Médina Gounass|Sinthiang Koundara|Louga|Coki|Ndiagne|Guet Ardo|Thiamène Cayor|Pété Ouarack|Keur Momar Sarr|Nguer Malal|Syer|Gande|Mbédiene|Niomré|Nguidilé|Kéle Gueye')
        Leslocalites1 = ('Léona|Sakal|Ngueune Sarr|Kébémer|Bandegne Ouolof|Diokoul Diawrigne|Kab Gaye|Ndande|Thieppe|Guéoul|Mbacké Cajor|Darou Marnane|Darou Mousty|Mbadiane|Ndoyene|Sam Yabal|Touba Mérina|Ngourane Ouolof|Thiolom Fall|Sagatta Gueth|Kanène Ndiob|Loro|Linguére|Dahra|Barkédji|Gassane|Thiargny|Thiel|Boulal|Dealy|Thiamène Pass|Sagatta Djolof|Affé Djolof|Dodji|Labgar|Ouarkhokh|Kamb|Mboula|Téssékéré Forage|Yang-Yang|Mbeuleukhé|Matam|Ourossogui|Thilogne|Nguidjilone|Dabia|Des Agnam|Oréfondé|Bokidiawé|Nabadji Civol|Ogo|Kanel|Odobéré|Wouro Sidy|Ndendory|Sinthiou Bamambé Banadji|Hamady Hounaré|Aouré|Bokiladji|Orkadiéré|Ouaoundé|Semmé|Dembancané|Ranérou|Lougré Thioly|Oudalaye|Vélingara|Saint-Louis|Saint Louis|Mpal|Fass-Ngom|Ndiébène Gandiol|Gandon|Dagana|Richard Toll|Ross-Béthio|Rosso-Sénégal|Ngnith|Diama|Ronkh|Ndombo Sandjiry|Gae|Bokhol|Mbane|Ndioum|Podor|Méry|Doumga Lao|Madina Diathbé|Golléré|Mboumba|Walaldé|Aéré Lao|Gamadji Saré|Dodel|Guedé Village|Guédé Chantier|Démette|Bodé Lao|Fanaye|Ndiayene Peindao|Niandane|Mbolo Birane|Boké Dialloubé|Galoya Toucouleur|Pété|Sédhiou|Marssassoum|Djiredji|Bambaly|Oudoucar|Sama Kanta Peulh|Diannah Ba|Koussy|Sakar|Diendé|Diannah Malary|San Samba|Bémet Bidjini|Djibabouya|Bounkiling|Bounkiling|Ndiamacouta|Boghal|Tankon|Ndiamalathiel|Djinany|Diacounda|Inor|Kandion Mangana|Bona|Diambati|Faoune|Diaroumé|Madina Wandifa|Goudomp|Diattacounda|Samine|Yarang Balante|Mangaroungou Santo|Simbandi Balante|Djibanar|Kaour|Diouboudou|Simbandi Brassou|Baghère|Niagha|Tanaff|Karantaba|Kolibantang|Tambacounda|Tambacounda|Niani Toucouleur|Makacolibantang|Ndoga Babacar|Missirah|Néttéboulou|Dialacoto|Sinthiou Malème|Koussanar|Kothiary|Goudiry|Boynguel Bamba|Sinthiou Mamadou Boubou|Koussan|Dougué|Dianké Makha|Boutoucoufara|Bani Israel|Sinthiou Bocar Aly|Koulor|Komoti|Bala|Koar|Goumbayel|Bakel|BELE|Bélé|Sinthiou Fissa|Kidira|Toumboura|Sadatou|Madina Foulbé|Gathiary|Moudery|Ballou|Gabou|Diawara|Koumpentoum|Koumpentoum|Malem Niany|Ndame|Méréto|Kahène|Bamba Thialène|Payar|Kouthiaba|Wolof|Kouthia Gaydi|Pass Coto|Malem Niany|Ville de Thiès|Khombole|Pout|Thiès Ouest|Thiès Est|Thiès Nord|Thiénaba|Ngoudiane|Ndiéyène Sirakh|Touba Toul|Keur Moussa|Diender|Fandène|Kayar|Notto|Tassète|Mbour|Joal Fadiouth|Fissel|Ndiaganiao|Sessene|Sandiara|Nguéniène|Thiadiaye|Sindia|Malicounda|Diass|Nguékhokh|Saly Portudal|Ngaparou|Somone|Popenguine-Ndayane|Tivaouane|Mékhé|Mboro|Méouane|Darou Khoudoss|Taïba Ndiaye|Mérina Dakhar|Koul|Pékèsse|Niakhène|Mbayène|Thilmakha|Ngandiouf|Notto Gouye Diama|Mont Rolland|Pire Goureye|Chérif Lo|Pambal|Ziguinchor|Ziguinchor|Niaguis|Adéane|Boutoupa Camaracounda|Niassia|Enampore|Bignona|Thionck Essyl|Kataba 1|Djinaky|Kafountine|Diouloulou|Tenghori|Niamone|Ouonck|Coubalan|Balinghore|Diégoune|Kartiack|Mangagoulack|Mlomp|Djibidione|Oulampane|Sindian|Suelle|Oussouye|Diembéring|Santhiaba Manjack|Oukout|Mlomp|')
        Regionss =('Dakar|Diourbel|Fatick|Kaffrine|Kaolack|Kédougou|Kolda|Louga|Matam|Saint-Louis|Sédhiou|Tambacounda|Thiés|Ziguinchor')
        locals = Leslocalites.split('|')
        locals1 = Leslocalites1.split('|')
        locals.extend(locals1)
        Regions = Regionss.split('|')
        com =item.get('communes')
        for local in locals:
            # print(local," : ",item.get(local))
            for item1 in com:
                if(item1==local):
                    cursor_covid.execute('Select idCommunes from Communes where Nom_Commune like "'+local+'"')
                    result = cursor_covid.fetchone()
                    cursor_covid.execute('Select id_communique from communique where NomFichierSource like "'+NomFichierSource+'"')
                    result1 = cursor_covid.fetchone()
                    if(result and result1):
                        for row in result:
                            idcommune=row
                            # print("idcommune",idcommune)
                            break
                        for row1 in result1:   
                            idcommunique=row1
                            # print("idcommunique",idcommunique)
                            break
                        if(idcommunique !=idcommune):
                            cursor_covid.execute("INSERT INTO  cas_commune(id_Communes,id_communique,Nb_Cas_Communautaires) VALUES (%s,%s,%s)",(idcommune,idcommunique,com.get(local)))
        for region in Regions :
            if(item1.get(region)):
                print("La region ",region," : ",item.get(region))
                cursor_covid.execute('Select idRegion from region where Nom_Region like "'+region+'"')
                result = cursor_covid.fetchone()
                cursor_covid.execute('Select id_communique from communique where NomFichierSource like "'+NomFichierSource+'"')
                result1 = cursor_covid.fetchone()
                if(result and result1):
                    for row in result:
                        idRegion=row
                        # print("idRegion",idRegion)
                        # break
                    for row1 in result1:   
                        idcommunique=row1
                        print("idcommunique",idcommunique)
                        # break
                    cursor_covid.execute("INSERT INTO  cas_region(Region_idRegion,communique_id_communique,Nb_Cas_Communautaires_Reg) VALUES (%s,%s,%s)",(idRegion,idcommunique,item.get(region)))

    
# conn.commit()
# con.close()
conn.close()
# cursor.close()
cursor_covid.close()
print("Successful....")