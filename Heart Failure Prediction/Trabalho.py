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
    

if __name__ == "__main__":
    main()