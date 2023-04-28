#list of tasks where the user can insert, remove and re-add them, using JSON.

import json

dict_lists={
    'Nome':'Júlia',
    'Sobrenome':'Cortez',
    'Idade':'24 anos'
}

with open('official_dict.json', 'w', encoding='utf8') as outfile:
    json.dump(
        dict_lists,
        outfile,
        #commands for text alignment and validating accents
        ensure_ascii=False,
        indent=2,
    )
