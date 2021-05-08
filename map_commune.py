import pandas as pd


us_cities = pd.read_csv("cas_communess.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="Nom_Commune", hover_data=["Nom_Commune", "Cas communautaires"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=600)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":1,"t":1,"l":0,"b":0})


# if __name__ == '__main__':
#     fig.run(host='0.0.0.0')

fig.show()

'''
def selected_item():
            try:
                if  listbox.get(listbox.curselection()): #de recuperer a partir des fichiers json les differentes dates puis de les selectionner
                    textes=afficherObjet(listbox.get(listbox.curselection()))
                    if textes:
                        fil = tk.Toplevel(self.master)
                        # fenetre blocante : empeche l’ouverture de fenetres identiques
                        self.master.wait_visibility(fil)
                        fil.grab_set()
                        # fermer fenetre blocante et reajustement des tailles des differentes fenetres qui apparaitront au niveau de l'interface
                        fil.geometry("600x600")
                        fil.title("Fichier :"+listbox.get(listbox.curselection()))
                        yscroll = tk.Scrollbar(fil)
                        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
                        xscroll = tk.Scrollbar(fil, orient=tk.HORIZONTAL)
                        xscroll.pack(side=tk.BOTTOM, fill=tk.X)
                        text1 = tk.Text(fil,wrap=tk.NONE,height=30, width=100,yscrollcommand=yscroll.set,
                        xscrollcommand=xscroll.set)  
                        text1.config(state="normal")
                        text1.insert("1.0",textes)   
                        text1.pack(side=tk.LEFT) 
                        yscroll.config(command=text1.yview)   
                        xscroll.config(command=text1.xview)             
                        fil.mainloop()
                        fil.quit()

                       

            except : #pour corriger les erreurs d'exception, on essaie de lancer un message. dans notre cas on a ...
                messagebox.showerror(title="Erreur !!!", message="Avez vous d'abord deja sélectionné un fichier pour vouloir le lire?")
        listbox.grid(row = 10, column = 0, pady =2 )
        
        btn = tk.Button(root, text='Ouvrir Le Fichier', command=selected_item)
   
        btn.grid(row = 10, column = 1, pady =6 )

       
    def create_widgets(self): # cette fonction permet de creer des widgets au niveau dans notre application
        self.lectureFichier()
    
     
   
                
if __name__ == '__main__':
    root=tk.Tk()
'''

