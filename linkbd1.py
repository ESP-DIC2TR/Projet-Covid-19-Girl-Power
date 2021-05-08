import xlsxwriter
import mysql.connector

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('C:\\Users\\HP\\Documents\\Cours_DIC2\\Semestre1\\SGBD\\Projet_SGBD\\cas_communess.xlsx')
worksheet = workbook.add_worksheet()

# Create style for cells
header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
body_cell_format = workbook.add_format({'border': True})

# The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
cnx = mysql.connector.connect(
    host='localhost',
    database='basee',
    user='root',
    password='Mysql123',
    auth_plugin = 'caching_sha2_password'
)

# Test the connection
print(cnx)

cursor = cnx.cursor()
cursor.execute('select Nom_commune,sum(Nb_Cas_Communautaires) from (select * from cas_commune C join communes R on C.id_communes=R.idCommunes) SR1 group by Nom_Commune')

row_index = 0
column_index = 0

for column_name in [row[0] for row in cursor.description]:
    worksheet.write(row_index, column_index, column_name, header_cell_format)
    column_index += 1

row_index += 1
for row in cursor.fetchall():
    column_index = 0
    for column in row:
        worksheet.write(row_index, column_index, column, body_cell_format)
        column_index += 1
    row_index += 1

print(str(row_index) + ' rows written successfully to ' + workbook.filename)

# Closing resource
cnx.close()
workbook.close() 