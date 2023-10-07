import streamlit as st
import speech_recognition as sr

# Barra lateral
with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Haptica")
    )

# Interfaz para la modalidad "Audio a Texto"
if mod_radio == "Auditiva":
    st.subheader("Audio a Texto")

    # Crear un botón para que el doctor pida al paciente hablar
    if st.button("Pídale al paciente que hable"):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            st.info("Hable ahora...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success("Texto convertido del audio:")
            st.write(text)
        except sr.UnknownValueError:
            st.warning("No se pudo reconocer el audio.")
        except sr.RequestError as e:
            st.error(f"Error en la solicitud de reconocimiento de voz: {e}")

# Interfaz para la identificación de la persona
if mod_radio == "Visual":
    st.subheader("Identificación de la Persona")
