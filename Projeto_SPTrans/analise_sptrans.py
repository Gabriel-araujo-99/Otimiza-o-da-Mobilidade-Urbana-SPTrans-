import pandas as pd

# Configurações para exibição de DataFrames
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def converter_para_minutos(hms):
    """Converte formato HH:MM:SS para o total de minutos do dia."""
    try:
        h, m, s = map(int, hms.split(':'))
        return h * 60 + m + (s / 60)
    except:
        return 0

try:
    # 1. Carga dos Dados
    print("--- INICIANDO ANÁLISE EXPLORATÓRIA (EDA) ---")
    rotas = pd.read_csv('routes.txt')
    paradas_tempo = pd.read_csv('stop_times.txt')
    print("✅ Passo 1: Sucesso! Dados carregados.")

    # 2. Limpeza dos Dados
    rotas = rotas.drop_duplicates()
    paradas_tempo = paradas_tempo.drop_duplicates()
    print(f"✅ Passo 2: Limpeza concluída.")

    # 3. Análise Descritiva (Paradas)
    contagem_paradas = paradas_tempo.groupby('trip_id').size().reset_index(name='qtd_paradas')
    
    # --- NOVO: Passo 3.1: Análise de Tempo de Viagem ---
    print("⏳ Calculando durações das viagens...")
    
    # Pegamos o menor e maior tempo de cada viagem (trip_id)
    tempos_viagem = paradas_tempo.groupby('trip_id')['arrival_time'].agg(['min', 'max']).reset_index()
    
    # Convertemos para minutos e calculamos a diferença
    tempos_viagem['min_total'] = tempos_viagem['min'].apply(converter_para_minutos)
    tempos_viagem['max_total'] = tempos_viagem['max'].apply(converter_para_minutos)
    tempos_viagem['duracao_minutos'] = tempos_viagem['max_total'] - tempos_viagem['min_total']
    
    # Unimos a contagem de paradas com a duração
    analise_completa = pd.merge(contagem_paradas, tempos_viagem[['trip_id', 'duracao_minutos']], on='trip_id')
    
    media_paradas = analise_completa['qtd_paradas'].mean()
    media_tempo = analise_completa['duracao_minutos'].mean()
    print(f"✅ Passo 3: Média de paradas: {media_paradas:.2f} | Tempo médio: {media_tempo:.2f} min")

    # 4. Cruzamento de Dados
    analise_completa['route_id'] = analise_completa['trip_id'].str.split('-').str[0]
    df_final = pd.merge(analise_completa, rotas[['route_id', 'route_short_name', 'route_long_name']], on='route_id', how='inner')

    # 5. Identificação de Variáveis e Correlação
    df_final['route_id_numeric'] = pd.to_numeric(df_final['route_id'], errors='coerce')
    # Agora calculamos a correlação entre paradas e tempo (muito mais interessante!)
    correlacao_tempo = df_final[['qtd_paradas', 'duracao_minutos']].corr().iloc[0, 1]
    print(f"✅ Passo 4: Correlação (Paradas vs Tempo): {correlacao_tempo:.4f}")

    # 6. Relatório de Insights (TOP 5 MAIS DEMORADAS)
    print("\n--- TOP 5 LINHAS MAIS DEMORADAS (EM MINUTOS) ---")
    top_5_tempo = df_final.sort_values(by='duracao_minutos', ascending=False).drop_duplicates('route_id').head(5)
    print(top_5_tempo[['route_long_name', 'qtd_paradas', 'duracao_minutos']])

    # 7. Exportação para Dashboard
    df_final.to_csv('dados_para_looker.csv', index=False)
    print("\n✅ Passo 5: Arquivo atualizado gerado para o Dashboard.")

except Exception as e:
    print(f"❌ Erro durante o processamento: {e}")