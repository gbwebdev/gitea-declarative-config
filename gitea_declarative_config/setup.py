from setuptools import setup, find_packages

setup(
    name='gitea_declarative_config',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'click_log',
        'pyyaml',
        'GitPython',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        gitea-declarative-config=gitea_declarative_config.cli:cli
    ''',
    package_data={
        'gitea_declarative_config' : ['res/**', 'res/templates/*']
    },
)