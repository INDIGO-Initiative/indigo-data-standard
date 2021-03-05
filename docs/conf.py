import os

project = 'INDIGO Data Standard'

extensions = ['indigosphinxcontrib.datadictionary']

schema_dir_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..',
    'schema'
)

codelist_dir_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..',
    'schema',
    'codelists'
)

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]
