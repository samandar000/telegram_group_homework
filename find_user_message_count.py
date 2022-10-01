from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    message_cout = {}
    for i in users_id:
        message_cout[i] = 0
    for m in data['messages']:
        actor_id = m.get('actor_id',False)
        from_id = m.get('from_id',False)
        users_id = 0
        if actor_id:
            users_id = actor_id
        else:
            users_id = from_id
        
        
        message_cout[users_id] += 1 
    return message_cout
data = read_data('data/result.json')
users_id = find_all_users_id(data)
print(find_user_message_count(data, users_id))