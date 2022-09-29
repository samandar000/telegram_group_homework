from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    a=[]
    b=[]
    for i in data["messages"] :
        a.append(i.get('actor',0))
        b.append(i.get('from',0))
    for k in a :
        if k!=0:
            if k not in b :
                b.append(k) 
    return b
d=read_data(("data/result.json"))
print(find_all_users_name(d))



