"""The package's CLI entrypoint
"""

from functools import wraps
import logging
import click

import click_log

from gitea_declarative_config.cli_commands.apply_config import apply_config

from gitea_declarative_config.model.gitea_server import GiteaServer

from gitea_declarative_config.cli_options.options_groups import git_options


logger = logging.getLogger("default")

@click.group()
@click_log.simple_verbosity_option(logger)
@git_options
def cli(git_options):
    """Gitea server management"""
    gitea_server = GiteaServer()

    gitea_server.raw_url=git_options['gitea_server']
    gitea_server.user=git_options['gitea_user']
    gitea_server.password=git_options['gitea_password']


# @click.group()
# @click_log.simple_verbosity_option(logger)
# def cli():
#     """Asten K8s Factory Main CLI"""
#     pass

# project.add_command(template)

cli.add_command(apply_config)
# cli.add_command(serve_api)
# cli.add_command(customers_env_management)

if __name__ == '__main__':
    cli()
