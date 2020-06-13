def grades(*g, status=False):
    """
    -> Function to analise many grades
    :param g: One or more grades
    :param status: Optional, boolean, Indicates weather shows or not the grades situation
    :return: One dictionary with How many grades, the biggest grade, the smallest grade,
    the grades average and the situation
    """
    dict_ = dict()
    dict_['count'] = len(g)
    dict_['average'] = sum(g)/len(g)
    dict_['biggest'] = max(g)
    dict_['smallest'] = min(g)
    if status:
        if dict_['average'] < 5:
            dict_['status'] = 'BAD'
        elif 5 < dict_['average'] < 7:
            dict_['status'] = 'REGULAR'
        elif dict_['average'] >= 7:
            dict_['status'] = 'GOOD'

    return dict_


# Main program
info = grades(10, 8, 8, 8, status=True)
print(info)
help(grades)
