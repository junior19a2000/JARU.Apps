import streamlit as st
import base64
import time

st.set_page_config(page_title = "JARU Apps", page_icon = "🦅", layout = "wide")

@st.cache_data
def load_gif():
    file_1   = open(r'SearchIT.gif', "rb")
    content1 = file_1.read()
    gif1     = base64.b64encode(content1).decode("utf-8")
    file_1.close()
    file_2   = open(r'Creator.gif', "rb")
    content2 = file_2.read()
    gif2     = base64.b64encode(content2).decode("utf-8")
    file_2.close()
    return gif1, gif2

gif1, gif2 = load_gif()

col1, col2 = st.columns([1, 1])
with col1:
    col3, col4, col5 = st.columns([1, 2.1, 1])
    with col4:
        st.markdown('#')
        st.header('SearchIT y Creator')
        st.text_input('Usuario:', placeholder = 'Ingrese aqui su usuario')
        st.text_input('Contraseña:', type = "password", placeholder = 'Ingrese aqui su contraseña')
        selectbox_1 = st.selectbox('Aplicativo:', ('App SearchIT', 'App Creator'))
        button_1 = st.button('Ingresar', use_container_width = True)
        empty_1  = st.empty()
        if button_1:
            with empty_1.container():
                st.warning('Las credencialas ingresadas no son correctas. Porfavor, reviselas e intente denuevo.')
                time.sleep(2.5)
                empty_1.empty()
        st.markdown('''<marquee style='font-size: 2; width: 100%' scrollamount='10'>
            <b>Desarrollados por: Junior Aguilar</b>
        </marquee>''', unsafe_allow_html = True)
with col2:
    if selectbox_1 == 'App SearchIT':
        st.subheader('App.SearchIT')
        st.markdown('''<div style="text-align: justify;">
            Te ayudara a buscar resoluciones parecidas a las que quieras desarrollar, mediante el uso de palabras 
            clave que permitan identificar dicha resolución. Ademas, podras visualizar dichas resoluciones sin necesidad 
            de descargarlas.
        </div>''', unsafe_allow_html = True)
        st.markdown('####')
        st.markdown(f'<img src = "data:image/gif;base64,{gif1}" width = "100%">', unsafe_allow_html = True)
    else:
        st.subheader('App.Creator')
        st.markdown('''<div style="text-align: justify;">
            Te ayudara generar el proyecto de resolución en si, pero mas rápido de lo normal, ya que los 
            datos que se encuentren disponibles en el expediente se agregaran en el documento Word de manera automática. 
            Ademas, podras agregar parrafos segun tus necesidades.
        </div>''', unsafe_allow_html = True)
        st.markdown('####')
        st.markdown(f'<img src = "data:image/gif;base64,{gif2}" width = "100%">', unsafe_allow_html = True)
