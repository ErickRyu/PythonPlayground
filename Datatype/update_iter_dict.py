
nested_dict = {'Ventilation only'
               : {'2nd 3rd prompt'
                  : {'VentilationVolume'
                     : {'wrong': 'Provide a ventilation volume of between 500ml and 800ml for each ventilation'}}},
               'CPR Training'
               : {'2nd 3rd prompt'
                  : {'VentilationVolume'
                     : {'wrong'
                        : 'Provide a ventilation volume of between 500ml and 800ml for each ventilation'}}}}


def iterdict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            iterdict(v)
        else:
            print(k, ":", v)


iterdict(nested_dict)