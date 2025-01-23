import streamlit as st
import time

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([3,1,1]) # colonne gauche 1.5x plus grande sinon st.columns(2) --> deux colonnes iso

col1.markdown(" # Bienvenue sur mon espace streamlit !!! ")
col1.markdown("***") #ligne horizontale
col1.markdown("* **Première puce")

col3.metric(label="Temperature", value="32 °C", delta="-3 °C" )

col2.header("Section perso")
if col2.button("Vegeta"):
    col3.subheader("Vegeta")
    col3.text('Le prince.')
    col3.write("Le meilleur saiyen.")
else:
    col2.text("Choisissez un personnage.")

if not col2.button("Goku"):
    col2.write("Allez allez...")
else:
    col3.subheader("Son Goku")
    col3.text('Le guerrier.')
    col3.write("La force tranquille.")

# s'affiche bien sur toute la longueur mais un petit souci, tant qu'il y a des col1, 2 ou 3 après alors ça se mettra par la suite
# ou ça se mettra avant la redéfinition des colonnes
st.write("Un autre essaie pour voir si ça fonctionne ou pas. On vérifie si ça s'étend bien ou pas. Il faut un text assez long pour avoir une preuve que cela occupe bien tout l'espace qu'on nous a donnés")

uploaded_photo = col1.file_uploader("Upload a photo")

taken_photo = col1.camera_input("Take a photo")

progress_bar = col1.progress(0)

for perc_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)

col1.success("Photo réussie !")

col1, col2 = st.columns(2)

col2.write("On teste l'affichage pour voir comment va s'écrire cette phrase longue dans l'application Streamlit ! (le redimensionnement fonctionne)")

with col1.expander("Click to read more"):
    st.text("Here are more information on the subject. Please leave a review.")
    if uploaded_photo is not None:
        st.image(uploaded_photo)

age_user = st.slider("How old are you ?", 0, 80, (30))
st.write("Votre âge :", age_user)

fourchette_salaire = st.slider("Entrer combien et combien, voudriez-vous que votre prochain salaire soit :", 30000, 80000, (35000,52000))
st.write("Vous souhaitez que votre prochain salaire soit entre:", fourchette_salaire) #st.write est mieux que st.text pour ça

st.title("Select Box")

col1, col2, col3 = st.columns(3)
choice = col1.selectbox(
    'Quel est le terrien que tu préfères dans DBZ ?',
    ('Tenshinhan', 'Tortue Géniale', 'Krillin')
)

st.write("Le terrien que tu préfère est : ", choice)

from datetime import time, datetime # ici car conflit avec l'autre package time sinon

st.subheader('Range time slider')

horaire = col3.slider(
     "Quels sont tes horaires ?",
     value=(time(9, 30), time(17, 30)))

col3.write("Tes horaires sont:", horaire)



