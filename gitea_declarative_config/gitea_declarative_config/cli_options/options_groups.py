from gitea_declarative_config.cli_options._options_group_meta import options_group

git_options_defs = [
    {'name': '--gitea-server',
     'envvar': "GITEA_SERVER",
     'default': "https://127.0.0.1:3000",
     'help': 'Gitea server address.'},
    {'name': '--gitea-user',
     'envvar': "GITEA_USER",
     'required': True,
     'help': 'Admin user account\'s username.'},
    {'name': '--gitea-password',
     'envvar': "GITEA_PASSWORD",
     'required': True,
     'help': 'Admin user account\'s password.'},
]

# Create the git_options decorator
git_options = options_group(git_options_defs, 'git_options')
