from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    a = []
    b = []
    for i in data["messages"]:
        a.append(i.get("from_id",0))
    
    for k in data["messages"]:
        a.append(i.get("actor_id",0))
    for k in a:
        if k!=0:
            if k not in b:
                b.append(k)
    return b[:-3]
    
d=read_data(("data/result.json"))

