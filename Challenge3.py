'''
We have a nested object. We would like a function where you pass in the object and a key and get back the value.
Example Inputs
object={'a': {'b': {'c': 'd'}}}
key=a/b/c
object={'x':{'y':{'z':'a'}}}
key x/y/z
value = a
'''
def fetch_Key(obj: dict):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('There is a multiple key available or empty dict')
    else:
        return keys[0]


def fetch_NestedValue(obj: dict, key: str, isFound = False):
    # check if object is dict type or not and isFound is true
    if type(obj) is not dict and not isFound:
        return None
    if (isFound or (key in obj.keys())) :
        if type(obj[key]) is dict:
            out_value=fetch_NestedValue(obj[key], fetch_Key(obj[key]), True) #fetch_key is the function to read key from object
            return out_value
        else:
            
            return obj[fetch_Key(obj)]
    else:
        nestedKey = fetch_Key(obj)
        out_value_new=fetch_NestedValue(obj[nestedKey], key, False)
        return out_value_new

if __name__ == '__main__':
    # Defining object 
    obj_val = {'x':{'y':{'z':'a'}}}
    # call function to read nested value
    value = fetch_NestedValue(obj_val, 'x')
    print(value)
