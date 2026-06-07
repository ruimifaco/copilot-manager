
def transform_query_in_dict(data_unfiltered):
    result_query_data = data_unfiltered.mappings().all() # Transforma a tabela que foi pedida em uma lista de dicionários porque Python não lê direito se fosse direto
    return result_query_data