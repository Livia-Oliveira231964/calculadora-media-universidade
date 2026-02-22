import streamlit as st
import altair as alt
import pandas as pd
from calculo import calcular_nota_final

# CSS para fundo claro
st.markdown(
    """
    <style>
    body {
        background-color: #F9F9FF; /* tom claro suave */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título estilizado
st.markdown("<h1 style='text-align: center; color: #AA77F2;'>😼 Calculadora de Média Universitária</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    m1 = st.number_input("Nota do primeiro bimestre (M1):", min_value=0, max_value=10, step=1, format="%d", value=0)

with col2:
    m2 = st.number_input("Nota do segundo bimestre (M2):", min_value=0, max_value=10, step=1, format="%d", value=0)

# Média mínima exigida pela universidade
media_uni = st.number_input("Digite a média mínima exigida pela universidade:", min_value=0, max_value=10, step=1, format="%d", value=6)

if st.button("Calcular Média"):
    resultado = calcular_nota_final(m1, m2)
    st.success(f"✅ Sua nota final é: {resultado}")

    # Mostrar quanto precisa para passar
    nota_necessaria = ((media_uni * 3) - m1) / 2
    if nota_necessaria <= 0:
        st.info("🎉 Você já garantiu a aprovação com a nota atual!")
    elif nota_necessaria > 10:
        st.error("❌ Infelizmente, mesmo com nota máxima no segundo bimestre não é possível atingir a média exigida.")
    else:
        st.warning(f"⚠️ Para passar, você precisa tirar pelo menos {round(nota_necessaria)} no segundo bimestre.")

    # Criar DataFrame para o gráfico
    dados = pd.DataFrame({
        "Bimestre": ["M1", "M2", "Média Final"],
        "Nota": [m1, m2, resultado]
    })

    # Paleta personalizada
    cores = {"M1": "#AA77F2", "M2": "#391DF2", "Média Final": "#2703A6"}

    # Gráfico mais fino
    grafico = alt.Chart(dados).mark_bar(size=40).encode(
        x="Bimestre",
        y="Nota",
        color=alt.Color("Bimestre", scale=alt.Scale(domain=list(cores.keys()), range=list(cores.values())))
    ).properties(
        title="Comparação das Notas"
    )

    st.altair_chart(grafico, use_container_width=True)