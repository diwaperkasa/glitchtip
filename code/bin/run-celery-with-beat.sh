#!/usr/bin/env bash
export IS_CELERY="true"
set -e

exec /Users/user/.pyenv/shims/python3.10 -m celery --workdir=/Applications/MAMP/htdocs/glitchtip-repo/code -A glitchtip worker -l info -B -s /tmp/celerybeat-schedule