import json

nested_dict = {'Ventilation only'
               : {'2nd 3rd prompt'
                  : {'VentilationVolume'
                     : {'wrong': 'Provide a ventilation volume of between 500ml and 800ml for each ventilation'}}},
               'CPR Trai ning'
               : {'2nd 3rd prompt'
                  : {'VentilationVolume'
                     : {'wrong'
                        : 'Provide a ventilation volume of between 500ml and 800ml for each ventilation'}}}}


def iter_update_nest_dict(src_dict, custom_dict):
    try:
        for key, val in custom_dict.items():
            if isinstance(val, dict):
                iter_update_nest_dict(src_dict[key], val)
            else:
                src_dict[key] = val
    except Exception as e:
        print('Error iter_update_nest_dict: {}'.format(e))


if __name__ == "__main__":
    f_prompt = open('prompt_book_eng_uk.json', 'rb')

    origin_prompt = json.load(f_prompt)
    custom_prompt = nested_dict

    iter_update_nest_dict(origin_prompt, custom_prompt)

    #print(origin_prompt)