def process_data(table, function, variables, action_variable):
    if function == 'group_by':
        return table.groupby(variables)
    elif function == 'sum':
        return table.groupby(variables)[action_variable].sum()
    elif function == 'avg': 
        return table.groupby(variables)[action_variable].mean()
    elif function == 'count': 
        return table.groupby(variables)[action_variable].count()
    elif function == 'max':
        return table.groupby(variables)[action_variable].max()
    elif function == 'min':
        return table.groupby(variables)[action_variable].min()