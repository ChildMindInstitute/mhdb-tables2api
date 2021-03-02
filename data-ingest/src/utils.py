import re

def convert_to_camelcase(input_string):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
