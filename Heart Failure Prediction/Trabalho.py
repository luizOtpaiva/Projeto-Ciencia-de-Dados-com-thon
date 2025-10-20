import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # Lendo o dataset
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    
    print(df.head())

# Pergunta 1 - A idade é um fator determinante na mortalidade de pacientes com insuficiência cardíaca?
    morreram = df[df['DEATH_EVENT'] == 1]['age']
    sobreviveram = df[df['DEATH_EVENT'] == 0]['age']

    media_sobreviveu = sobreviveram.mean()
    media_morreu = morreram.mean()

    labels = [f'Sobreviveu\n({media_sobreviveu:.1f} anos)',
              f'Morreu\n({media_morreu:.1f} anos)']

    plt.figure(figsize=(6, 6))
    plt.bar(labels, [media_sobreviveu, media_morreu],
            color=['green', 'salmon'],width=0.5)
    plt.title('Idade Média por Desfecho', fontsize=14)
    plt.ylabel('Idade Média (anos)')
    plt.ylim(0, 80)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

#Pergunta 2 - Pacientes com diabetes têm maior taxa de mortalidade cardíaca?

    # Agrupa os dados por presença de diabetes (0 = não, 1 = sim)
    diabetes_mortalidade = df.groupby('diabetes')['DEATH_EVENT'].mean().sort_index() * 100

    valores = diabetes_mortalidade.values
    labels = [f'Sem Diabetes {valores[0]:.2f}%', f'Com Diabetes {valores[1]:.2f}%']

    plt.bar(labels, valores, color=['#6aa84f', '#e06666'], alpha=0.8,width=0.5)

    plt.title('Mortalidade por Insuficiência Cardíaca — Com ou Sem Diabetes', fontsize=13, pad=15)
    plt.ylabel('Taxa de Mortalidade (%)')

    plt.show()
    
# Pergunta 3 -  A hipertensão influencia na chance de óbito por insuficiência cardíaca? Comparar taxa de mortalidade entre hipertensos e não hipertensos.

    hipertensao_mortalidade = df.groupby('high_blood_pressure')['DEATH_EVENT'].mean().sort_index() * 100 # aqui ele pega a média da coluna DEATH_EVENT agrupando por high_blood_pressure
    valores = hipertensao_mortalidade.values # pega os valores da série resultante
    labels = [f'Sem Hipertensão {valores[0]:.2f}%', f'Com Hipertensão {valores[1]:.2f}%'] # cria os rótulos com as taxas formatadas
    plt.bar(labels, valores, color=["#a23d0a", "#0e91ef"], alpha=0.8,width=0.5)
    plt.title('Mortalidade por Insuficiência Cardíaca — Com ou Sem Hipertensão', fontsize=13, pad=15)
    plt.ylabel('Taxa de Mortalidade (%)')   
    plt.show()

# Pergunta 4 - O nível de creatinina sérica (indicador da função renal) tem relação com o risco de morte? 
# Médicos usam creatinina como preditor de prognóstico; ótimo insight biomédico.

    morreram = df[df['DEATH_EVENT'] == 1]['serum_creatinine'] # filtra os pacientes que morreram e pega os níveis de creatinina
    sobreviveram = df[df['DEATH_EVENT'] == 0]['serum_creatinine'] # filtra os pacientes que sobreviveram e pega os níveis de creatinina
    media_sobreviveu = sobreviveram.mean()
    media_morreu = morreram.mean()
    labels = [f'Sobreviveu\n({media_sobreviveu:.2f} mg/dL)',
              f'Morreu\n({media_morreu:.2f} mg/dL)']
    plt.figure(figsize=(6, 6))
    plt.bar(labels, [media_sobreviveu, media_morreu],
            color=['#38761d', '#cc0000'],width=0.5)
    plt.title('Nível Médio de Creatinina Sérica por Desfecho', fontsize=14)
    plt.ylabel('Creatinina Sérica Média (mg/dL)')
    plt.ylim(0, 5)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

 # Pergunta 5 - Pacientes com níveis baixos de sódio no sangue apresentam maior mortalidade?
 # Hiponatremia (baixo sódio)
 
 
    morreram = df[df['DEATH_EVENT'] == 1]['serum_sodium'] # filtra os pacientes que morreram e pega os níveis de sódio
    sobreviveram = df[df['DEATH_EVENT'] == 0]['serum_sodium'] # filtra os pacientes que sobreviveram e pega os níveis de sódio
    media_sobreviveu = sobreviveram.mean()
    media_morreu = morreram.mean()
    labels = [f'Sobreviveu\n({media_sobreviveu:.2f} mEq/L)',
              f'Morreu\n({media_morreu:.2f} mEq/L)']
    plt.figure(figsize=(6, 6))
    plt.bar(labels, [media_sobreviveu, media_morreu],
            color=['#1155cc', '#ff0000'],width=0.5)
    plt.title('Nível Médio de Sódio Sérico por Desfecho', fontsize=14)
    plt.ylabel('Sódio Sérico Médio (mEq/L)')
    plt.ylim(120, 150)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()


    # Pergunta 6 - Há diferença de mortalidade entre homens e mulheres?

    # Calcula a taxa de mortalidade (%) por sexo
    mortalidade_sexo = df.groupby('sex')['DEATH_EVENT'].mean().sort_index() * 100
    valores = mortalidade_sexo.values
    labels = [f'Mulheres {valores[0]:.2f}%', f'Homens {valores[1]:.2f}%']

    plt.figure(figsize=(6, 6))
    plt.bar(labels, valores, color=['#9370DB', '#6495ED'], alpha=0.8, width=0.4, edgecolor='black')

    plt.title('Taxa de Mortalidade por Sexo', fontsize=14, pad=15)
    plt.ylabel('Taxa de Mortalidade (%)')
    plt.ylim(0, max(valores) + 10)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.show()

    #Pergunta 7 - O tabagismo (fumar) aumenta o risco de mortalidade cardíaca nesse grupo?

    # Calcula a taxa de mortalidade (%) por tabagismo
    mortalidade_fumo = df.groupby('smoking')['DEATH_EVENT'].mean().sort_index() * 100
    valores = mortalidade_fumo.values

    contagem = df['smoking'].value_counts().sort_index()

    labels = [
        f'Não fumantes\n({contagem[0]} pessoas)',
        f'Fumantes\n({contagem[1]} pessoas)'
    ]

    plt.figure(figsize=(6, 6))
    plt.bar(labels, valores, color=['#8FD19E', '#E07B91'], alpha=0.8, width=0.4, edgecolor='black')

    plt.title('Taxa de Mortalidade por Tabagismo', fontsize=14, pad=15)
    plt.ylabel('Taxa de Mortalidade (%)')
    plt.ylim(0, max(valores) + 10)
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.show()

    #Pergunta 8 - 8. Os níveis da enzima CPK (indicador de dano muscular) estão associados à morte cardíaca?

    # Calcula as médias de CPK para cada grupo
    media_cpk = df.groupby('DEATH_EVENT')['creatinine_phosphokinase'].mean()

    valores = media_cpk.values
    labels = [f'Sobreviveram \n {valores[0]:.2f} (U/L)', f'Morreram \n {valores[1]:.2f} (U/L)']

    plt.figure(figsize=(6, 6))
    plt.bar(labels, valores, color=['#8FD19E', '#E07B91'], alpha=0.8, edgecolor='black', width=0.5)

    plt.title('Nível Médio da Enzima CPK por Ocorrência de Morte Cardíaca', fontsize=14, pad=15)
    plt.ylabel('Nível médio de CPK (U/L)')
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.show()

    # Pergunta 9 - O percentual de ejeção do coração (Ejection Fraction) é o melhor indicador de sobrevida?

    # 9.1 Comparação da Média de Fração de Ejeção por Desfecho
    morreram = df[df['DEATH_EVENT'] == 1]['ejection_fraction']
    sobreviveram = df[df['DEATH_EVENT'] == 0]['ejection_fraction']
    media_sobreviveu = sobreviveram.mean()
    media_morreu = morreram.mean()

    labels = [f'Sobreviveu\n({media_sobreviveu:.1f}%)',
              f'Morreu\n({media_morreu:.1f}%)']

    plt.figure(figsize=(6, 6))
    plt.bar(labels, [media_sobreviveu, media_morreu],
            color=['#4CAF50', '#FF5733'], width=0.5)
    plt.title('Fração de Ejeção Média por Desfecho', fontsize=14)
    plt.ylabel('Fração de Ejeção Média (%)')
    plt.ylim(0, 50)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()  # Usado show() para o código que será apresentado ao usuário

    # 9.2 Comparação da Taxa de Mortalidade por Grupo de Risco (FE <= 40% vs. FE > 40%)
    df['EF_Group'] = np.where(df['ejection_fraction'] <= 40, 'Baixa (<= 40%)', 'Normal (> 40%)')
    mortalidade_ef = df.groupby('EF_Group')['DEATH_EVENT'].mean() * 100

    # Garantir que a ordem dos grupos no gráfico é a mesma para as labels e valores
    mortalidade_ef = mortalidade_ef.sort_index(ascending=False)  # Ordem: Normal primeiro, Baixa depois

    valores_ef = mortalidade_ef.values
    labels_ef = [f'Baixa ({mortalidade_ef.loc["Baixa (<= 40%)"]:.2f}%)',
                 f'Normal ({mortalidade_ef.loc["Normal (> 40%)"]:.2f}%)']

    plt.figure(figsize=(6, 6))
    # Ordem das barras ajustada: Baixa primeiro (índice 0), Normal segundo (índice 1)
    plt.bar([labels_ef[0], labels_ef[1]], [valores_ef[0], valores_ef[1]],
            color=['#FFC300', '#33AFFF'], alpha=0.8, width=0.5)

    plt.title('Taxa de Mortalidade por Grupo de Fração de Ejeção', fontsize=14, pad=15)
    plt.ylabel('Taxa de Mortalidade (%)')
    plt.ylim(0, max(valores_ef) + 10)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

    # Pergunta 10 - Quais fatores (entre idade, hipertensão, creatinina, sódio, etc.) mais influenciam a mortalidade?

    # Selecionar colunas de interesse
    colunas_correlacao = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
                          'ejection_fraction', 'high_blood_pressure', 'platelets',
                          'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']

    # Calcular a correlação com a variável alvo (DEATH_EVENT)
    correlacoes = df[colunas_correlacao + ['DEATH_EVENT']].corr()['DEATH_EVENT'].drop('DEATH_EVENT')

    # Ordenar as correlações pelo valor absoluto (importância)
    correlacoes_abs_ordenadas = correlacoes.abs().sort_values(ascending=False)

    # Reordenar os valores de correlação originais com base na ordem absoluta
    correlacoes_ordenadas = correlacoes.loc[correlacoes_abs_ordenadas.index]

    # Mapear nomes das colunas para nomes mais legíveis em Português
    nomes_portugues = {
        'time': 'Tempo de Acompanhamento (dias)',
        'serum_creatinine': 'Creatinina Sérica',
        'ejection_fraction': 'Fração de Ejeção',
        'age': 'Idade',
        'serum_sodium': 'Sódio Sérico',
        'high_blood_pressure': 'Hipertensão',
        'anaemia': 'Anemia',
        'creatinine_phosphokinase': 'CPK',
        'sex': 'Sexo (Homem)',
        'smoking': 'Tabagismo',
        'diabetes': 'Diabetes',
        'platelets': 'Plaquetas'
    }

    rotulos_ordenados = [nomes_portugues.get(col, col) for col in correlacoes_ordenadas.index]
    valores_ordenados = correlacoes_ordenadas.values

    # Cores: Positivo (Risco Maior) em Vermelho, Negativo (Risco Menor) em Verde
    cores = ['#cc0000' if c > 0 else '#38761d' for c in valores_ordenados]

    plt.figure(figsize=(10, 8))
    plt.barh(rotulos_ordenados, valores_ordenados, color=cores)
    plt.axvline(0, color='grey', linestyle='--', alpha=0.7)  # Linha de referência no zero
    plt.title('Correlação dos Fatores com a Mortalidade (DEATH_EVENT)', fontsize=16, pad=15)
    plt.xlabel('Coeficiente de Correlação (R)', fontsize=12)
    plt.gca().invert_yaxis()  # Colocar o fator mais influente no topo
    plt.xlim(-0.5, 0.5)  # Limitar o eixo x para melhor visualização
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    main()