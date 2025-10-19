import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # Lendo o dataset
    df = pd.read_csv('../heart_failure_clinical_records_dataset.csv')
    
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



#Conclusão pergunta 1
#A idade apresenta uma relação clara com a mortalidade por insuficiência cardíaca.
#Pacientes que morreram durante o acompanhamento têm, em média,
#uma idade cerca de 7 anos superior aos sobreviventes.
#Isso sugere que o envelhecimento é um fator importante de risco,
#possivelmente devido à menor capacidade de regeneração cardíaca
#e maior presença de comorbidades em idosos
#Portanto, é fundamental prestar atenção especial a pacientes idosos,
#priorizando o monitoramento constante,
#prevenção e acompanhamento médico mais rigoroso para reduzir o risco de mortalidade nessa faixa etária

#Conclusao pergunta 2
#A presença de diabetes não apresentou diferença significativa na mortalidade
#por insuficiência cardíaca neste conjunto de dados.
#As taxas de óbito foram praticamente iguais entre pacientes com e sem diabetes,
#o que sugere que, isoladamente, o diabetes pode não ser um fator determinante
#para a mortalidade neste contexto.
#Contudo, é importante destacar que o diabetes continua sendo uma condição de risco
#cardiovascular relevante, podendo atuar em conjunto com outros fatores (como idade, hipertensão e função cardíaca reduzida).

if __name__ == "__main__":
    main()