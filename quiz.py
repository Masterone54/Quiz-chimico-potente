import streamlit as st
import random

# 1. CONFIGURAZIONE PAGINA
st.set_page_config(page_title="Quale Elemento Chimico Sei?", page_icon="🧪")

st.title("🧪 Quale Elemento Chimico Sei?")
st.write("Scopri la tua personalità scientifica in poche domande!")

# 2. DEFINIZIONE DEI RISULTATI
risultati = {
    "Litio": "**Sei il Litio: La mina vagante piena di energia!**\nSei una fonte inesauribile di vitalità. Sempre in movimento e con mille progetti, ma attenzione al tuo carattere decisamente esplosivo.",
    "Platino": "**Sei il Platino: Il risolutore di problemi (Catalizzatore)!**\nRaro, prezioso ed elegante. Sei l'amico che sblocca le situazioni e sprona gli altri a dare il meglio, tirando le fila con classe.",
    "Argon": "**Sei l'Argon: Il maestro zen imperturbabile!**\nIl re della tranquillità. Non ti mischi mai con i drammi e scivoli via da ogni conflitto. Sei la personificazione assoluta del 'chill'.",
    "Ferro": "**Sei il Ferro: La roccia con troppo stile (Swag)!**\nDuro, resistente e colonna portante del gruppo. Affronti la vita di petto, con uno stile inconfondibile e un carisma magnetico.",
    "Mercurio": "**Sei il Mercurio: La red flag ipnotica!**\nFascino del pericolo in persona. Sfuggente, ipnotico e impossibile da etichettare. Sei bellissimo da guardare, ma chi si avvicina troppo rischia di bruciarsi."
}

# 3. DOMANDE E RISPOSTE ORIGINALI (Il sistema le mischierà da solo)
domande = [
    {
        "domanda": "1. La sveglia suona alle 6 del mattino.",
        "opzioni": {"Esplodi come una batteria difettosa.": "Litio", "Analizzi la frequenza del suono per ottimizzarla.": "Platino", "Non la senti, sei inerte.": "Argon", "La prendi a pugni con la tua mano d'acciaio.": "Ferro", "Ti dissolvi e scivoli fuori dalla finestra.": "Mercurio"}
    },
    {
        "domanda": "2. Il tuo panino cade nella sabbia.",
        "opzioni": {"Lo mangi in 2 secondi e poi corri in cerchio.": "Litio", "Usi un magnete per separare i minerali metallici.": "Platino", "Lo guardi e pensi 'vabbè'.": "Argon", "Lo schiacci per testarne la resistenza.": "Ferro", "Convinci qualcun altro che è un 'panino esotico'.": "Mercurio"}
    },
    {
        "domanda": "3. Vedi un palloncino per strada.",
        "opzioni": {"Lo fai scoppiare gridando 'BOOM!'.": "Litio", "Lo sfiori e catalizzi una reazione che lo gonfia in un dirigibile.": "Platino", "Ti ci addormenti sopra.": "Argon", "Lo tieni in mano con un carisma magnetico.": "Ferro", "Lo ipnotizzi con un riflesso argentato.": "Mercurio"}
    },
    {
        "domanda": "4. Devi fare i compiti di matematica.",
        "opzioni": {"Strappi il libro per l'iperattività.": "Litio", "Metti vicini due compagni e fai in modo che li risolvano loro.": "Platino", "Fissi il foglio per ore senza muovere un muscolo.": "Argon", "Colpisci la sedia con decisione.": "Ferro", "Ti trasformi in una red flag e scompari.": "Mercurio"}
    },
    {
        "domanda": "5. La porta di casa è bloccata.",
        "opzioni": {"La sfondi con un calcio esplosivo.": "Litio", "Acceleri chimicamente la ruggine: la serratura marcisce in due secondi.": "Platino", "Aspetti che qualcuno apra, senza fretta.": "Argon", "La spingi con tutta la tua forza bruta.": "Ferro", "Ti fai liquido e passi sotto la porta.": "Mercurio"}
    },
    {
        "domanda": "6. Ti trovi in una foresta buia.",
        "opzioni": {"Accendi un falò gigante e balli intorno.": "Litio", "Fai reagire due funghi creando una lampada da discoteca chimica.": "Platino", "Ti mimetizzi e dormi su una nuvola di Argon.": "Argon", "Spaventi le ombre con la tua presenza forte.": "Ferro", "Convinci un lupo che sei suo amico.": "Mercurio"}
    },
    {
        "domanda": "7. Il tuo gelato si sta sciogliendo velocemente.",
        "opzioni": {"Lo finisci in un boccone e urli per il congelamento cerebrale.": "Litio", "Inverti la reazione chimica per ricongelarlo.": "Platino", "Guardi il gelato sciogliersi con distacco.": "Argon", "Lo mangi con un carisma inconfondibile.": "Ferro", "Diventi lucido come il mercurio e lo bevi.": "Mercurio"}
    },
    {
        "domanda": "8. Qualcuno ti sfida a una gara di sguardi.",
        "opzioni": {"Sbatti le palpebre 100 volte in un secondo.": "Litio", "Brilli così tanto che l'avversario deve mettersi gli occhiali da sole.": "Platino", "Non sbatti le palpebre per 3 giorni, sei imperturbabile.": "Argon", "Vinci con uno sguardo duro come l'acciaio.": "Ferro", "Prendi un aspetto tossico ma affascinante e lo ipnotizzi.": "Mercurio"}
    },
    {
        "domanda": "9. La TV si spegne durante la tua scena preferita.",
        "opzioni": {"Lanci il telecomando contro il muro.": "Litio", "Agiti il telecomando e crei un mini-reattore che accende la TV per 100 anni.": "Platino", "Ti giri e ti addormenti.": "Argon", "Minacci la TV con il pugno.": "Ferro", "Scompari misteriosamente dalla stanza.": "Mercurio"}
    },
    {
        "domanda": "10. Incontri un alieno molto timido.",
        "opzioni": {"Gli urli 'CIAO!' a 2 cm dalla faccia.": "Litio", "Gli prepari un tè ai catalizzatori che gli fa passare la timidezza in 0,3 secondi.": "Platino", "Lo ignori completamente.": "Argon", "Gli mostri il tuo SWAG naturale.": "Ferro", "Ti avvicini lentamente e lo avveleni col tuo fascino.": "Mercurio"}
    }
]

# 4. LOGICA DI RANDOMIZZAZIONE DELLE RISPOSTE
if 'shuffled_q' not in st.session_state:
    shuffled = []
    for d in domande:
        ops = list(d["opzioni"].items())
        random.shuffle(ops) # Ecco il tuo randomizer automatico
        shuffled.append({"domanda": d["domanda"], "opzioni": ops})
    st.session_state.shuffled_q = shuffled

# 5. GENERAZIONE DEL QUIZ IN PAGINA
punteggi = {"Litio": 0, "Platino": 0, "Argon": 0, "Ferro": 0, "Mercurio": 0}
risposte_date = []

with st.form("quiz_form"):
    for i, d in enumerate(st.session_state.shuffled_q):
        st.subheader(d["domanda"])
        # Estrae solo i testi delle opzioni per i radio button
        testi_opzioni = [opz[0] for opz in d["opzioni"]]
        scelta = st.radio("Scegli un'opzione:", testi_opzioni, key=f"q_{i}")
        
        # Recupera l'elemento collegato all'opzione scelta
        elemento_scelto = next(opz[1] for opz in d["opzioni"] if opz[0] == scelta)
        risposte_date.append(elemento_scelto)
        st.write("---")

    submitted = st.form_submit_button("Scopri il risultato! 🚀")

# 6. CALCOLO E STAMPA DEL RISULTATO
if submitted:
    for r in risposte_date:
        punteggi[r] += 1
    
    # Trova l'elemento con il punteggio massimo
    vincitore = max(punteggi, key=punteggi.get)
    
    st.success("Test completato!")
    st.title(f"🏆 RISULTATO: {vincitore}")
    st.write(risultati[vincitore])
    st.balloons()