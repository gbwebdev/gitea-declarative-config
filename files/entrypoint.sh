#!/bin/sh
set -e

if [ "$MODE" = "development" ];  then
    pip install -e /home/gdc/src/gitea_declarative_config
fi

exec /usr/local/bin/gitea_declarative_config $*
