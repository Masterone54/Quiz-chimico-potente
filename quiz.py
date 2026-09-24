import streamlit as st
import random
import time

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    /* Cambia il font di tutto il sito */
    html, body, [class*="css"], h1, h2, h3, p, span {
        font-family: 'Press Start 2P', monospace !important;
        font-size: 14px !important;
    }
    
    /* Sfondo principale */
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(#333333 1px, transparent 1px);
        background-size: 20px 20px;
    }

    /* Stile del blocco delle domande (il box di dialogo) */
    [data-testid="stForm"] {
        background-color: #1a4f8b !important; /* Blu Mystery Dungeon */
        border: 4px solid #ffffff !important;
        border-radius: 10px !important;
        padding: 20px !important;
        color: white !important;
        box-shadow: 5px 5px 0px #000000;
    }

    /* Testo bianco per le domande */
    [data-testid="stMarkdownContainer"] p {
        color: white !important;
        line-height: 1.8;
    }

    /* Stile del bottone finale */
    [data-testid="baseButton-secondaryFormSubmit"] {
        background-color: #ffcc00 !important;
        color: black !important;
        border: 2px solid white !important;
        border-radius: 5px !important;
    }
</style>
""", unsafe_allow_html=True)

# 1. CONFIGURAZIONE PAGINA
def text_animato(testo):
    for lettera in testo:
        yield lettera
        time.sleep(0.03) # Cambia questo numero per renderlo più veloce o più lento

# Mostra il titolo animato (solo se non è già stato mostrato, per evitare che ripeta l'animazione a ogni click)
if 'intro_fatta' not in st.session_state:
    st.write_stream(text_animato("Benvenuto. Questo è un portale verso un mondo sconosciuto... \n\nRispondi alle domande sinceramente. Sei pronto?"))
    st.session_state.intro_fatta = True
else:
    st.write("Benvenuto. Questo è un portale verso un mondo sconosciuto... \n\nRispondi alle domande sinceramente. Sei pronto?")

# 2. DEFINIZIONE DEI RISULTATI
risultati = {
    "Litio": "**Sei il Litio: La mina vagante piena di energia!**\nSei una fonte inesauribile di vitalità. Sempre in movimento e con mille progetti, ma attenzione al tuo carattere decisamente esplosivo.",
    "Platino": "**Sei il Platino: Il risolutore di problemi (Catalizzatore)!**\nRaro, prezioso ed elegante. Sei l'amico che sblocca le situazioni e sprona gli altri a dare il meglio, tirando le fila con classe.",
    "Argon": "**Sei l'Argon: Il maestro zen imperturbabile!**\nIl re della tranquillità. Non ti mischi mai con i drammi e scivoli via da ogni conflitto. Sei la personificazione assoluta del 'chill'.",
    "Ferro": "**Sei il Ferro: La roccia con troppo stile (Swag)!**\nDuro, resistente e colonna portante del gruppo. Affronti la vita di petto, con uno stile inconfondibile e un carisma magnetico.",
    "Mercurio": "**Sei il Mercurio: La red flag ipnotica!**\nFascino del pericolo in persona. Sfuggente, ipnotico e impossibile da etichettare. Sei bellissimo da guardare, ma chi si avvicina troppo rischia di bruciarsi."
}
immagini_risultati = {
    "Litio": "litio.jpg",
    "Platino": "platino.jpg",
    "Argon": "argon.jpg",
    "Ferro": "ferro.jpg",
    "Mercurio": "mercurio.jpg"
}


# 3. DOMANDE E RISPOSTE ORIGINALI (Il sistema le mischierà da solo)
domande = [
        {
        "domanda": "Sei al cinema. Cosa stai guardando?",
        "opzioni": {
            "Un film d'azione.": ["Litio", "Ferro"], 
            "Un film drammatico.": ["Mercurio", "Argon"], 
            "Un film romantico": "Platino" 
        }
    },
        {
        "domanda": "Come ti organizzi nello studio?",
        "opzioni": {
            "Lavoro duro, giorno dopo giorno.": ["Platino", "Ferro"], 
            "Se mi ricordassi di farlo...": "Litio", 
            "Faccio il minimo indispensabile.": "Argon", 
            "Non ce la farò mai senza aiuto...": "Mercurio" 
        }
    },
        {
        "domanda": "Ti è stato chiesto di occuparti di un incarico problematico. Cosa fai?",
        "opzioni": {
            "Ci penso io!": ["Argon", "Ferro"], 
            "Chiedo aiuto a qualcuno.": "Litio", 
            "Lo faccio fare ad altri!": ["Mercurio","Platino"]
        }
    },
    {
        "domanda": "Trovi un portafoglio per strada. Cosa fai?",
        "opzioni": {
            "Lo porto alla polizia!": ["Platino", "Ferro"],
            "Evviva! Soldi gratis!": ["Litio", "Mercurio"],
            "Lo ignoro e tiro dritto.": ["Argon"]
        }
    },
    {
        "domanda": "Hai vinto alla lotteria! Cosa fai con il premio?",
        "opzioni": {
            "Risparmio tutto in banca.": ["Platino", "Argon"],
            "Compro regali per tutti!": ["Ferro", "Mercurio"],
            "Spendo tutto subito per me!": ["Litio"]
        }
    },
    {
        "domanda": "Il tuo amico piange a dirotto. Cosa fai?",
        "opzioni": {
            "Cerco di farlo ridere.": ["Litio", "Platino"],
            "Piango insieme a lui.": ["Mercurio"],
            "Gli do una pacca sulla spalla.": ["Ferro"],
            "Non so cosa fare...": ["Argon"]
        }
    },
    {
        "domanda": "Un gatto randagio ti fissa insistentemente...",
        "opzioni": {
            "Lo fisso anche io.": ["Ferro", "Litio"],
            "Gli do qualcosa da mangiare.": ["Platino", "Argon"],
            "Faccio 'miao' e me ne vado.": ["Mercurio"]
        }
    },
    {
        "domanda": "Cadi rovinosamente davanti a un sacco di gente.",
        "opzioni": {
            "Arrossisco e scappo.": ["Platino", "Argon"],
            "Faccio finta che fosse calcolato.": ["Mercurio", "Ferro"],
            "Rido di me stesso con gli altri.": ["Litio"]
        }
    },
    {
        "domanda": "Ti regalano un pacco misterioso e pesantissimo.",
        "opzioni": {
            "Lo apro subito strappando la carta!": ["Litio", "Mercurio"],
            "Lo scuoto per capire cos'è.": ["Platino", "Ferro"],
            "Lo metto via per dopo.": ["Argon"]
        }
    },
    {
        "domanda": "Senti odore di cibo buonissimo, ma non sai da dove viene.",
        "opzioni": {
            "Seguo l'odore come un segugio!": ["Litio", "Ferro"],
            "Mi viene solo fame.": ["Platino", "Mercurio"],
            "Lo ignoro.": ["Argon"]
        }
    },
    {
        "domanda": "Vedi una pozzanghera gigantesca dopo la pioggia.",
        "opzioni": {
            "Ci salto dentro a piedi pari!": ["Litio", "Mercurio", "Ferro"],
            "Ci giro intorno attento a non sporcarmi.": ["Platino", "Argon"]
        }
    },
    {
        "domanda": "Sei su una barca che sta per affondare!",
        "opzioni": {
            "Prendo un salvagente e mi tuffo!": ["Litio", "Ferro"],
            "Urlo e vado nel panico!": ["Mercurio", "Argon"],
            "Cerco di riparare la falla.": ["Platino"]
        }
    },
    {
        "domanda": "Qualcuno ti fa un bel complimento sincero.",
        "opzioni": {
            "Dico grazie, fiero di me.": ["Ferro", "Litio"],
            "Mi imbarazzo e guardo in basso.": ["Argon", "Platino"],
            "Penso che mi stia prendendo in giro.": ["Mercurio"]
        }
    },
    {
        "domanda": "Ti piace stare al centro dell'attenzione?",
        "opzioni": {
            "Lo adoro! Guardatemi!": ["Litio", "Mercurio", "Ferro"],
            "Preferisco stare nell'ombra.": ["Platino", "Argon"]
        }
    },
    {
        "domanda": "Ti piace fare scherzi agli altri?",
        "opzioni": {
            "Sì, sono un maestro degli scherzi!": ["Mercurio", "Litio", "Ferro"],
            "No, non mi piace far arrabbiare la gente.": ["Platino", "Argon"]
        }
    },
    {
        "domanda": "C'è una torta sul tavolo. Nessuno ti guarda.",
        "opzioni": {
            "Ne mangio una fetta enorme!": ["Litio", "Ferro"],
            "Resisto alla tentazione.": ["Platino", "Argon"],
            "Le do solo una piccola leccatina...": ["Mercurio"]
        }
    },
    {
        "domanda": "Hai un esame importantissimo domani!",
        "opzioni": {
            "Studio tutta la notte!": ["Platino", "Ferro"],
            "Gioco ai videogiochi, ormai è tardi.": ["Litio", "Mercurio"],
            "Vado a letto presto sperando in bene.": ["Argon"]
        }
    },
    {
        "domanda": "Ti fanno una critica sul tuo lavoro.",
        "opzioni": {
            "La accetto e cerco di migliorare.": ["Platino", "Ferro"],
            "Mi offendo tantissimo.": ["Litio", "Mercurio"],
            "Ignoro tutto.": ["Argon"]
        }
    },
    {
        "domanda": "Incontri una persona molto famosa.",
        "opzioni": {
            "Chiedo subito una foto e un autografo!": ["Litio", "Ferro"],
            "La guardo da lontano in silenzio.": ["Argon", "Platino"],
            "Faccio finta di non riconoscerla.": ["Mercurio"]
        }
    }
]

# 4. LOGICA DI RANDOMIZZAZIONE DELLE RISPOSTE
if 'shuffled_q' not in st.session_state:
    domande_scelte = random.sample(domande, 10)
    shuffled = []
    for d in domande_scelte:
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
        # Controlla se 'r' è una lista di più elementi (es. ["Litio", "Ferro"])
        if isinstance(r, list): 
            for elemento in r:
                punteggi[elemento] += 1
        # Altrimenti se è un elemento singolo (es. "Argon")
        else:
            punteggi[r] += 1
    
    # Trova l'elemento con il punteggio massimo
    vincitore = max(punteggi, key=punteggi.get)
    
    st.success("Test completato!")
    st.title(f"🏆 RISULTATO: {vincitore}")
    st.image(immagini_risultati[vincitore], use_container_width=True)
    st.write(risultati[vincitore])
    st.balloons()