import streamlit as st
import speech_recognition as sr
from textblob import TextBlob
import cv2

# Página de inicio
st.title("Aplicación de Notas Médicas")

# Sección para la identificación del paciente mediante reconocimiento facial
st.header("Identificación de Paciente")

uploaded_image = st.file_uploader("Cargue una imagen del paciente:")
if uploaded_image is not None:
    image = cv2.imread(uploaded_image.name)
    st.image(image, caption="Imagen del paciente", use_column_width=True)

# Sección para preguntar si el paciente está bien y realizar análisis de sentimiento
st.header("Pregunta al Paciente si está bien (Audio)")

audio_file = st.file_uploader("Cargue el audio de la pregunta:")
if audio_file is not None:
    recognizer = sr.Recognizer()
    audio_data = sr.AudioFile(audio_file.name)

    with audio_data as source:
        audio_text = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_text)
        st.text("Texto obtenido del audio:")
        st.text(text)

        # Realizar análisis de sentimiento
        blob = TextBlob(text)
        sentiment = blob.sentiment
        st.text("Análisis de sentimiento:")
        st.write(sentiment)
    except sr.UnknownValueError:
        st.warning("No se pudo reconocer el audio.")
    except sr.RequestError as e:
        st.error(f"Error en la solicitud de reconocimiento de voz: {e}")

# Sección para preguntar por los síntomas del paciente (Audio)
st.header("Pregunta al Paciente por los Síntomas (Audio)")

audio_file_symptoms = st.file_uploader("Cargue el audio de la pregunta por los síntomas:")
if audio_file_symptoms is not None:
    recognizer = sr.Recognizer()
    audio_data = sr.AudioFile(audio_file_symptoms.name)

    with audio_data as source:
        audio_text = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_text)
        st.text("Texto obtenido del audio de síntomas:")
        st.text(text)
    except sr.UnknownValueError:
        st.warning("No se pudo reconocer el audio de síntomas.")
    except sr.RequestError as e:
        st.error(f"Error en la solicitud de reconocimiento de voz: {e}")

# Sección para guardar la información
st.header("Guardar Información del Paciente")
