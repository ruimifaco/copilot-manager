def transform_query_in_dict(data_unfiltered):
    result_query_data = data_unfiltered.mappings().all() # Transforma a tabela que foi pedida em uma lista de dicionários porque Python não lê direito se fosse direto
    return result_query_data

def transform_query_in_dict_first(data_unfiltered):
    result_query_data_first = data_unfiltered.mappings().first() # Transforma a tabela que foi pedida em uma lista de dicionários porque Python não lê direito se fosse direto
    return result_query_data_first

def transform_query_in_dict_one(data_unfiltered):
    result_query_data_one = data_unfiltered.mappings().one()
    return result_query_data_one