import streamlit as st
import random
import time

st.set_page_config(page_title="Quale Elemento Chimico Sei?", page_icon="🧪")

# 1. CSS ESTREMO: Sfondo animato a scorrimento e bottoni stile GBA
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    
    html, body, [class*="css"], h1, h2, h3, p, span, button {
        font-family: 'Press Start 2P', monospace !important;
        color: #ffffff !important;
    }
    
    header { display: none !important; }

    /* SFONDO PSICHEDELICO ANIMATO (Aura) */
    @keyframes psych-scroll {
        0% { background-position: 0 0; }
        100% { background-position: 100px 100px; }
    }
    
    .stApp {
        background-color: #1a0b2e;
        background-image: repeating-linear-gradient(
            45deg,
            #2d1154 25%, transparent 25%, transparent 75%, #2d1154 75%, #2d1154
        ),
        repeating-linear-gradient(
            45deg,
            #2d1154 25%, #1a0b2e 25%, #1a0b2e 75%, #2d1154 75%, #2d1154
        );
        background-position: 0 0, 50px 50px;
        background-size: 100px 100px;
        animation: psych-scroll 4s linear infinite;
    }

    /* BOX DELLA DOMANDA (Textbox PMD) */
    .stApp > header + div {
        background-color: rgba(0, 0, 0, 0.85) !important;
        border: 4px solid #ffffff !important;
        border-radius: 10px !important;
        padding: 30px !important;
        margin-top: 10vh !important;
        box-shadow: inset 0 0 0 4px #000, inset 0 0 0 6px #fff !important;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    h3 {
        color: #f8d030 !important; 
        font-size: 16px !important;
        line-height: 1.8 !important;
        margin-bottom: 40px !important;
    }

    /* TRASFORMA I PULSANTI IN TESTO DI GIOCO */
    div.stButton > button {
        background-color: transparent !important;
        border: none !important;
        color: #ffffff !important;
        text-align: left !important;
        display: block !important;
        width: 100% !important;
        padding: 10px 10px 10px 30px !important;
        font-size: 12px !important;
        box-shadow: none !important;
        position: relative;
    }
    
    div.stButton > button:hover {
        color: #00ffff !important;
    }
    
    div.stButton > button:hover::before {
        content: "▶";
        color: #00ffff !important;
        position: absolute;
        left: 5px;
    }
</style>
""", unsafe_allow_html=True)


# 2. DEFINIZIONE DEI RISULTATI
risultati = {
    "Litio": "Sei il Litio!nSei una fonte inesauribile di vitalità. Sempre in movimento e con mille progetti, ma attenzione al tuo carattere decisamente esplosivo.",
    "Platino": "Sei il Platino!\nRaro, prezioso ed elegante. Sei l'amico che sblocca le situazioni e sprona gli altri a dare il meglio.",
    "Argon": "Sei l'Argon!\nIl re della tranquillità. Non ti mischi mai con i drammi e scivoli via da ogni conflitto.",
    "Ferro": "Sei il Ferro!\nDuro, resistente e colonna portante del gruppo. Affronti la vita di petto, con uno stile inconfondibile.",
    "Mercurio": "Sei il Mercurio!\nFascino del pericolo in persona. Sfuggente, ipnotico e impossibile da etichettare."
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

# 3. MOTORE DI GIOCO (Stato della sessione)
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.punteggi = {"Litio": 0, "Platino": 0, "Argon": 0, "Ferro": 0, "Mercurio": 0}
    
    # Pesca 10 domande casuali all'avvio
    domande_scelte = random.sample(domande, 10)
    shuffled = []
    for d in domande_scelte:
        ops = list(d["opzioni"].items())
        random.shuffle(ops) 
        shuffled.append({"domanda": d["domanda"], "opzioni": ops})
    st.session_state.shuffled_q = shuffled

# 4. RENDER DELLA SCHERMATA CORRENTE
if st.session_state.step < 10:
    q = st.session_state.shuffled_q[st.session_state.step]
    
    # Stampa la domanda
    st.markdown(f"### {q['domanda']}")
    
    # Genera un bottone per ogni risposta possibile
    for testo_risposta, elementi in q['opzioni']:
        # Quando l'utente clicca una risposta, esegue questo blocco:
        if st.button(testo_risposta, key=f"btn_{st.session_state.step}_{testo_risposta}"):
            if isinstance(elementi, list):
                for el in elementi:
                    st.session_state.punteggi[el] += 1
            else:
                st.session_state.punteggi[elementi] += 1
            
            # Avanza di livello e ricarica istantaneamente la pagina
            st.session_state.step += 1
            st.rerun()

else:
    # 5. SCHERMATA FINALE DEL RISULTATO
    vincitore = max(st.session_state.punteggi, key=st.session_state.punteggi.get)
    
    st.markdown("### L'aura che ti circonda si sta manifestando...")
    time.sleep(1.5) # Piccola pausa drammatica per l'effetto suspense
    
    st.markdown(f"## SEI {vincitore.upper()}!")
    st.image(immagini_risultati[vincitore], use_container_width=True)
    st.markdown(f"<p>{risultati[vincitore]}</p>", unsafe_allow_html=True)
    
    # Bottone per rigiocare
    st.write("---")
    if st.button("Ricomincia l'esplorazione"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()