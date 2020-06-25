from flask import request


def get_data():
    """
    Returns a python dict with name, email, year, and color from data in a JSON request. 
    Sets attributes to None if not found in JSON.   
    """
    return {
        'name': request.json.get('name', None),
        'email': request.json.get('email', None),
        'year': request.json.get('year', None),
        'color': request.json.get('color', None)
    }


def make_response(num_response, year_response, lucky_num, data):
    """
    Generates a python dict response from the data given
    """
    try:
        return {
            'num': {
                'fact': num_response.text,
                'num': lucky_num
            },
            'year': {
                'fact': year_response.text,
                'year': data['year']
            }
        }
    except:
        return "There was an error - make sure your data is formatted correctly, then try again."

def check_for_errors(data):
    """ 
    Input: 
    data - python dict with name, email, year, color 
    Output:
    errors - python dict either empty or with error messages
    """
    errors = {}
    valid_colors = ['red', 'green', 'orange', 'blue']
    error_messages = {
        'name': 'This field is required',
        'email': 'This field is required',
        'year': 'Invalid value. Year must be between 1900 and 2000',
        'color': 'Invalid value. Color must be one of "red", "green", "orange", "blue"'
    }

    for key, val in data.items():
        if not val:
            errors[key] = error_messages[key]
    try:
        if not int(data['year']) >= 1900 or not int(data['year']) <= 2000:
            errors['year'] = error_messages['year']
        if data['color'] not in valid_colors:
            errors['color'] = error_messages['color']
        return errors
    except:
        return errors
