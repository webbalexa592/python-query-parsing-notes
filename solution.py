import urllib.parse

def solve(value):
    return urllib.parse.parse_qs(value, keep_blank_values=True, max_num_fields=100)
