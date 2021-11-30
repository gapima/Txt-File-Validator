import streamlit as st

st.write("VALIDADOR DE TEXTO")

with st.form(key="include_arquivo"):
    input_banco = st.selectbox("Selicione o Banco", options= ["Santander", "Itau", "Bradesco"])
    
    input_produto = st.selectbox("Selecione o produto", options=["Cobrança", "Pagamento a forncedores", "Pagamento de salarios"])
    input_layout = st.selectbox("Selecione o layout", options=["240", "400"])
    ##input_name = st.text_input(label="Insira o seu nome")
    ##input_age = st.number_input(label="insira sua idade")
    ##input_occupation = st.selectbox("Selicone o Banco", ["Santander", "Itau", "Bradesco"])
    input_arquivo = st.file_uploader("Upload")
    input_button_submit = st.form_submit_button("Validar")
    
    
    
    if input_button_submit:
        st.write(f'Arquivo: {input_arquivo}')
        st.write("arquivo correto!")
        
    