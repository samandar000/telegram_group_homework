from read_data import read_data


def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    x = data["messages"]
    a = []
    
    for i in x :
        if i.get("actor") and i.get("actor") not in a:
            a.append(i["actor"])
        
        if i.get("from") and i.get("from") not in a:
            a.append(i["from"])
        
        
    return a

d=read_data(("data/result.json"))



