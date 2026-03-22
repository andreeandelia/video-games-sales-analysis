import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


image = Image.open('students-img.jpg')

st.image(image, width="stretch")

st.markdown("""
# Analiza sanatatii mintale si a burnout-ului in randul studentilor

""", text_alignment="justify")

section = st.sidebar.radio("Navigati catre:",
                     ["Introducere", "Ceva", "EDA"])

if section == "Introducere":
    st.markdown("""
    Viata academica moderna vine adesea la pachet cu un nivel ridicat de stres, presiune,
    performanta si provocari legate de echilibrul dintre viata personala si studii. Sanatatea 
    mintala a studentilor si fenomenul de "burnout" au devenit subiecte critice de discutie
    in mediul educational. Intelegerea factorilor care declanseaza acest sindrom este primul
    pas catre preventie si suport adecvat.

    ***
    
    ### Obiectivul proiectului

    Scopul principal al acestei aplicatii este de a transforma datele brute intr-o poveste usor de
    inteles printr-o Analiza Exploratorie a Datelor (EDA) interactiva. Utilizatorii pot nu doar sa 
    vizualizeze distributia si corelatiile dintre factori, dar si sa interactioneze direct cu setul
    de date.
            
    """, text_alignment="justify")

    uploaded_file = st.file_uploader("Alegeti fisierul")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)

        item_count, col_count = df.shape
        st.markdown(f"""
        ### Despre setul de date
        
        Acest proiect are la baza un set de date de mari dimensiuni ({item_count} de inregistrari
        si {col_count} de variabile), creat special pentru a analiza si prezice nivelul de burnout
        al studentilor. Desi este un set de date generat sintetic, el a fost modelat pentru a reflecta
        cu acuratete realitatea, combinand variabile numerice si categorice din trei arii esentiale:
        - Factori academici: volum de studiu, note, prezenta;
        - Factori psihologici: nivelul de stres raportat, anxietate;
        - Factori de stil de viata: calitatea somnului, activitatea fizica, activitati extracuriculare.
        
        #### Prezentarea detaliata a variabilelor
        
        Pentru a oferi o imagine clara asupra informatiilor analizate, am grupat cele 20 de variabile in
        patru categorii logice:
        
        ##### A. Date demografice si academice
        
        Aceasta sectiune descrie profilul de baza al studentului si performanta sa educationala:
        - ***student_id***: Identificator unic atribuit fiecarei inregistrari (variabila nominala);
        - ***age***: Varsta studentului, exprimata in ani (variabila numerica);
        - ***gender***: Genul studentului (variabila categoriala: Male, Female, Other);
        - ***course***: Programul de studiu sau specializarea urmata (variabila categoriala);
        - ***year***: Anul curent de studiu al studentului (variabila categoriala ordinala: 1st, 2nd, 3rd, 4th);
        - ***attendance_percentage***: Rata de prezenta la cursuri, exprimata procentual (variabila numerica continua);
        - ***cgpa***: Media cumulata a notelor, reflectand performanta academica generala (variabila numerica continua).
        
        ##### B. Stil de viata
        
        Variabilele din aceasta categorie cuantifica obiceiurile zilnice care pot influenta starea de bine:
        - ***daily_study_hours***: Timpul mediu, in ore, dedicat studiului individual zilnic (variabile numerica);
        - ***daily_sleep_hours***: Numarul mediu de ore de somn pe noapte (variabila numerica);
        - ***sleep_quality***: Evaluarea subiectiva a calitatii somnului (variabila categorica ordinala: Poor, Average, Good);
        - ***screen_time_hours***: Timpul zilnic estimat petrecut in fata ecranelor, excluzand studiul (variabila numerica);
        - ***physical_activity_hours***: Timpul mediu zilnic alocat exercitiilor fizice sau sportului (variabila numerica);
        - ***internet_quality***: Calitatea conexiunii la internet (variabila categorica: Poor, Average, Good). 
        
        ##### C. Evaluari psihologice si factori de stres
        
        Aceste variabile reprezinta scoruri auto-raportate sau evaluate care masoara diferite dimensiuni ale sanatatii mintale:
        - ***stress_level***: Nivelul general de stres resimtit (variabila categorica ordinala: Low, Medium, High);
        - ***anxiety_score***: Un scor numeric (de la 1 la 10) care indica severitatea simptomelor de anxietate;
        - ***depression_score***: Un scor numeric care masoara prezenta si intensitatea starilor depresive;
        - ***academic_pressure_score***: Scorul care cuantifica presiunea resimtita de student in legatura cu termenele limita, examenele si asteptarile academice;
        - ***financial_stress_score***: Nivelul de ingrijorare cu privire la situatia financiara proprie sau a familiei;
        - ***social_support_score***: Un indicator al spijinului emotional sau practic perceput din partea familiei, prietenilor sau comunitatii.
        
        ##### D. Variabila tinta
        
        - ***burnout_level***: Aceasta este variabila dependenta a setului de date, reprezentand nivelul final de epuizare al studentului (variabila categorica ordinala: Low, Medium, High).
        Toate celelalte caracteristici vor fi analizate din perspectiva impactului pe care il au asupra acestei variabile.
        
        """, text_alignment="justify")

elif section == "Ceva":
    st.markdown("Ceva")
elif section == "EDA":
    st.markdown("EDA")