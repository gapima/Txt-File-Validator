import streamlit as st;

st.write("Validador de texto")

with st.form(key="include_arquivo"):
    input_name = st.selectbox("Selicone o Banco", ["Santander", "Itau", "Bradesco"])
    input_name = st.selectbox("Selecione o produto", ["Cobrança", "Pagamento a forncedores", "Pagamento de salarios"])
    input_name = st.selectbox("Selecione o layout", ["240", "400"])
    ##input_name = st.text_input(label="Insira o seu nome")
    ##input_age = st.number_input(label="insira sua idade")
    ##input_occupation = st.selectbox("Selicone o Banco", ["Santander", "Itau", "Bradesco"])
    input_arquivo = st.file_uploader("Upload")
    input_button_submit = st.form_submit_button("Processar")
    