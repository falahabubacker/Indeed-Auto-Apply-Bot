def convert_header_text_to_dict(header_text):
    headers = {}
    lines = header_text.strip().strip('{}').strip().split('\n')

    for line in lines:
        if line and ':' in line:
            key, value = line.split(':', 1)
            
            headers[key.strip()] = value.strip()
            
    return headers