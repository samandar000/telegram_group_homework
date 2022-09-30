from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    x = data["messages"]
    a = []
    
    for i in x :
        if i.get("actor_id") and i.get("actor_id") not in a:
            a.append(i["actor_id"])
        
        if i.get("from_id") and i.get("from_id") not in a:
            a.append(i["from_id"])
        
        
    return a

d=read_data(("data/result.json"))
print(find_all_users_id(d))
