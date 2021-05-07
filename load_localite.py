import simplejson
import mysql.connector
import json
import os.path

print("Connexion a la base de donnees...")


conn = mysql.connector.connect(host="localhost",user="root",password="Mysql123",db="basee")
cursor_covid=conn.cursor(buffered=True)

json_file_path = 'C:\\Users\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\\Projet_SGBD\\Senegal.json'


json_data=open(json_file_path)
json_obj=json.loads(json_data.read())

for item in json_obj:  
	region=item.get("region")
	print("La region :",region)
	cursor_covid.execute("INSERT INTO region(Nom_Region) VALUES (%s)",(region,))
	departements=item.get("departements")
	for element in departements:
			print("Nom departement ",element.get("departement"))
			cursor_covid.execute('Select idregion from region where Nom_Region like "'+region+'"')
			result = cursor_covid.fetchone()
			if(result):
				for row in result:
					idRegion=row
					print("idRegion :",row,)
					break
			cursor_covid.execute("INSERT INTO departement(Nom_Departement,Region_idRegion) VALUES (%s,%s)",(element.get("departement"),idRegion))	 
			for element1 in element.get("comard"):
					print('la commune '+element1)
					cursor_covid.execute('Select idDepartement from Departement where Nom_Departement like "'+element.get("departement")+'"')
					result = cursor_covid.fetchone()
					if(result):
						for row in result:
							idDepartement=row
							print("idDepartement : ",idDepartement)
							break
					cursor_covid.execute("INSERT INTO communes(Nom_Commune,Departement_idDepartement) VALUES (%s,%s)",(element1,idDepartement))		

			for element1 in element.get("arronds"):
						print('la commune '+element1)
						cursor_covid.execute('Select idDepartement from Departement where Nom_Departement like "'+element.get("departement")+'"')
						result = cursor_covid.fetchone()
						if(result):
							for row in result:
								idDepartement=row
								print("idDepartement : ",idDepartement)
								break
						cursor_covid.execute("INSERT INTO communes(Nom_Commune,Departement_idDepartement) VALUES (%s,%s)",(element1,idDepartement))				 	


conn.commit()
conn.close()
cursor_covid.close()
print("Successful....")