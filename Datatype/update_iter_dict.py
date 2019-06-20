import json

nested_dict = {'Ventilation only'
               : {'2nd 3rd prompt'
                  : {'VentilationVolume'
                     : {'wrong': 'Provide a ventilation volume of between 500ml and 800ml for each ventilation'}}},
               'CPR Training'
               : {'2nd 3rd prompt'
                  : {'VentilationVolume'
                     : {'wrong'
                        : 'Provide a ventilation volume of between 500ml and 800ml for each ventilation'}}}}


def iter_update_nest_dict(src_dict, custom_dict):
    for key, val in custom_dict.items():
        if isinstance(val, dict):
            iter_update_nest_dict(src_dict[key], val)
        else:
            if key in src_dict:
                src_dict[key] = val
            else:
                print('key \'{}\' is not exist'.format(key))


if __name__ == "__main__":
    f_prompt = open('prompt_book_eng_uk.json', 'rb')

    origin_prompt = json.load(f_prompt)
    custom_prompt = nested_dict

    iter_update_nest_dict(origin_prompt, custom_prompt)

    print(origin_prompt)