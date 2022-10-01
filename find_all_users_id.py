from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    messages = data['messages']
    users_id = []
    for m in messages:
        actor_id = m.get('actor_id',False)
        from_id = m.get('from_id',False)
        i = 0
        if actor_id:
            i = actor_id
        else:
            i = from_id

        if i not in users_id:
            users_id.append(i)
    
    return users_id
data = read_data('data/result.json')
print(find_all_users_id(data))

        
        
    



