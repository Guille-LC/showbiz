import streamlit as st
import pandas as pd
from datetime import datetime

# Datos de eventos simulados
eventos = [
    {"nombre": "Concierto Rock Legends", "portada": "https://example.com/rock.jpg", "lugar": "Teatro Gran Rex", "fecha": "2025-03-15", "hora": "20:00", "precio": "$5000", "descripcion": "Un homenaje a las mejores bandas de rock.", "boleteria": "https://ticketshop.com/rock"},
    {"nombre": "Festival de Jazz", "portada": "https://example.com/jazz.jpg", "lugar": "Luna Park", "fecha": "2025-04-10", "hora": "19:30", "precio": "$7000", "descripcion": "Los mejores artistas del jazz en una noche única.", "boleteria": "https://ticketshop.com/jazz"},
    {"nombre": "Stand-up Comedy Night", "portada": "https://example.com/comedy.jpg", "lugar": "Teatro Broadway", "fecha": "2025-05-20", "hora": "21:00", "precio": "$4500", "descripcion": "Los mejores comediantes en un solo escenario.", "boleteria": "https://ticketshop.com/comedy"},
]

df_eventos = pd.DataFrame(eventos)

# Configuración de la app
st.title("Showbiz - Descubre Eventos en tu Ciudad")
st.write("Nunca más te perderás un evento importante. Filtra y encuentra tus favoritos.")

# Filtros de búsqueda
nombre_evento = st.text_input("Buscar por nombre del evento:")
lugar_evento = st.text_input("Buscar por lugar:")
fecha_evento = st.date_input("Seleccionar fecha:", value=None, min_value=datetime(2025, 1, 1))

# Filtrado de eventos
filtrados = df_eventos
if nombre_evento:
    filtrados = filtrados[filtrados["nombre"].str.contains(nombre_evento, case=False)]
if lugar_evento:
    filtrados = filtrados[filtrados["lugar"].str.contains(lugar_evento, case=False)]
if fecha_evento:
    filtrados = filtrados[filtrados["fecha"] == fecha_evento.strftime("%Y-%m-%d")]

# Mostrar resultados
for _, evento in filtrados.iterrows():
    st.image(evento["portada"], width=300)
    st.subheader(evento["nombre"])
    st.write(f"📍 {evento['lugar']}")
    st.write(f"🗓 {evento['fecha']} - ⏰ {evento['hora']}")
    st.write(f"💲 {evento['precio']}")
    st.write(evento["descripcion"])
    st.markdown(f"[Comprar entradas]({evento['boleteria']})", unsafe_allow_html=True)
    st.markdown("---")

st.write("Encuentra más eventos próximamente en Showbiz.")
