def knight_rows_to_dict(knight_rows):

    knight_dict = {knight_row['id'] : {'settler_id' : knight_row['settler_id'],
                                       'level': knight_row['level'],
                                       'is_active' : knight_row['is_active'],
                                       'is_promotable' : False} for knight_row in knight_rows}

    return knight_dict

