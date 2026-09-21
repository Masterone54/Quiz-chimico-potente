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
        "domanda": "La sveglia suona alle 7 del mattino.",
        "opzioni": {
            "Esplodi come una batteria difettosa.": "Litio", 
            "Analizzi la frequenza del suono per ottimizzarla.": "Platino", 
            "Non la senti, sei inerte.": "Argon", 
            "La prendi a pugni con la tua mano d'acciaio.": "Ferro", 
            "Fondi e scivoli fuori dalla finestra.": "Mercurio"
        }
    },
    {
        "domanda": "Il tuo panino cade nella sabbia.",
        "opzioni": {
            "Lo mangi in 2 secondi e poi corri in cerchio.": "Litio", 
            "Regola dei 5 secondi.": "Platino", 
            "Lo guardi e pensi 'vabbè'.": "Argon", 
            "Lo schiacci per testarne la resistenza.": "Ferro", 
            "Convinci qualcun altro che è un 'panino esotico'.": "Mercurio"
        }
    },
    {
        "domanda": "Devi fare i compiti di matematica.",
        "opzioni": {
            "Strappi il libro per l'iperattività.": "Litio", 
            "Metti vicini due compagni e fai in modo che li risolvano loro.": "Platino", 
            "Fissi il foglio per ore senza muovere un muscolo.": "Argon", 
            "Colpisci il banco con decisione.": "Ferro", 
            "Mangi il quaderno per merenda.": "Mercurio"
        }
    },
    {
        "domanda": "La porta di casa è bloccata.",
        "opzioni": {
            "La sfondi con un calcio esplosivo.": "Litio", 
            "Crei una chiave d'emergenza al volo.": "Platino", 
            "Aspetti che qualcuno apra, senza fretta.": "Argon", 
            "La spingi con tutta la tua forza bruta.": "Ferro", 
            "Fondi la serratura ed entri senza problemi.": "Mercurio"
        }
    },
    {
        "domanda": "Il tuo gelato si sta sciogliendo velocemente.",
        "opzioni": {
            "Lo finisci in un boccone e urli per il congelamento cerebrale.": "Litio", 
            "Costruisci un cono-isotermico al volo.": "Platino", 
            "Guardi il gelato sciogliersi con distacco.": "Argon", 
            "Lo mangi con un carisma inconfondibile.": "Ferro", 
            "Lo bevi da un bicchiere.": "Mercurio"
        }
    },
    {
        "domanda": "Qualcuno ti sfida a una gara di sguardi.",
        "opzioni": {
            "Sbatti le palpebre 100 volte in un secondo.": "Litio", 
            "Brilli così tanto che l'avversario deve mettersi gli occhiali da sole.": "Platino", 
            "Non sbatti le palpebre per 3 giorni, sei imperturbabile.": "Argon", 
            "Vinci con uno sguardo duro come l'acciaio.": "Ferro", 
            "Assumi uno sguardo affascinante e lo ipnotizzi.": "Mercurio"
        }
    },
    {
        "domanda": "La TV si spegne durante la tua scena preferita.",
        "opzioni": {
            "Lanci il telecomando contro il muro.": "Litio", 
            "Smonti la TV per trovare il guasto.": "Platino", 
            "Ti giri e ti addormenti.": "Argon", 
            "Minacci la TV con il pugno.": "Ferro", 
            "Scompari misteriosamente dalla stanza.": "Mercurio"
        }
    },
    {
        "domanda": "Incontri un alieno molto timido.",
        "opzioni": {
            "Gli urli 'CIAO!' a 2 cm dalla faccia.": "Litio", 
            "Costruisci un traduttore universale.": "Platino", 
            "Lo ignori completamente.": "Argon", 
            "Gli mostri il tuo SWAG naturale.": "Ferro", 
            "Gli offri una cicca con l'idea di avvelenarlo.": "Mercurio"
        }
    },
    {
        "domanda": "Il tuo compagno fa 67 alla prof.",
        "opzioni": {
            "Ti alzi e lo fai pure tu.": "Litio", 
            "Convinci tutta la classe a farlo.": "Platino", 
            "Fai finta di niente.": "Argon", 
            "Lo smolecoli.": "Ferro", 
            "Gli ricordi che è un poveraccio.": "Mercurio"
        }
    },
    {
        "domanda": "La prof non ti lascia andare al bagno.",
        "opzioni": {
            "La fai nel cestino.": "Litio", 
            "Inizi a far casino con i tuoi compagni.": "Platino", 
            "LAspetti l'intervallo.": "Argon", 
            "Ribalti il banco dalla rabbia.": "Ferro", 
            "La convinci con uno sguardo.": "Mercurio"
        }
    },
    {
        "domanda": "Un tuo amico viene aggredito da un bullo.",
        "opzioni": {
            "Sei il bullo.": "Litio", 
            "Lo convinci a calmarsi.": "Platino", 
            "Fai finta di niente.": "Argon", 
            "Finalmente una scusa per alzare le mani.": "Ferro", 
            "Gli sta bene.": "Mercurio"
        }
    }
]

# 4. LOGICA DI RANDOMIZZAZIONE DELLE RISPOSTE
if 'shuffled_q' not in st.session_state:
    shuffled = []
    for d in domande:
        ops = list(d["opzioni"].items())
        random.shuffle(ops) # Mischia l'ordine delle risposte
        shuffled.append({"domanda": d["domanda"], "opzioni": ops})
    random.shuffle(shuffled) # Mischia l'ordine delle domande!
    st.session_state.shuffled_q = shuffled

# 5. GENERAZIONE DEL QUIZ IN PAGINA
punteggi = {"Litio": 0, "Platino": 0, "Argon": 0, "Ferro": 0, "Mercurio": 0}
risposte_date = []

with st.form("quiz_form"):
    for i, d in enumerate(st.session_state.shuffled_q):
        st.subheader(f"{i+1}. {d['domanda']}")
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