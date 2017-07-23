#!/usr/bin/env python3

from setuptools import setup

setup(
    name='data-tools',
    version='0.1.0',
    description='File format conversion tools',
    url='https://github.com/clarkgrubb/data-tools',
    author='Clark Grubb',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='file format conversion data tools json csv tsv',

    packages=[
        'data_tools'
    ],
    entry_points={
        'console_scripts': [
            'csv-to-json = data_tools.csv_to_json:main',
            'convert-date = data_tools.convert_date:main',
            'counting-sort = data_tools.counting_sort:main',
            'csv-to-xlsx = data_tools.csv_to_xlsx:main',
            'data-fill = data_tools.data_fill:main',
            'date-seq = data_tools.data_seq:main',
            'highlight = data_tools.highlight:main',
            'html-table-to-csv = data_tools.html_table_to_csv:main',
            'join-tsv = data_tools.join_tsv:main',
            'normalize-utf8 = data_tools.normalize_utf8:main',
            'reservoir-sample = data_tools.reservoir_sample:main',
            'trim-tsv = data_tools.trim_tsv:main',
            'tsv-to-json = data_tools.tsv_to_json:main',
            'xlsx-to-csv = data_tools.xlsx_to_csv:main',
            'yaml-to-json = data_tools.yaml_to_json:main'
        ]
    },
    install_requires=[
        'beautifulsoup4>=4.5.3',
        'html5lib>=0.999999999',
        'openpyxl>=2.4.5',
        'PyYAML>=3.12',
        'xlrd==1.0.0',
    ],
    python_requires='>=3.4'
)
