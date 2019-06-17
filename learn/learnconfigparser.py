from configparser import ConfigParser
# https://www.youtube.com/watch?v=HH9L9WFMfnE
config = ConfigParser(allow_no_value=True)
config['default'] = {
    '; set True for application': None,
    'update': 'None',
    'Normal data': 'value'
}


# TODO: Create file generator for config
config['filename'] = {

}
config['path'] = {
    'cust_fw': 'None',
    'mst_fw': 'None'
}

with open("config.ini", 'w') as f:
    config.write(f)
