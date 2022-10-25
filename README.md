# GLITCHTIP
## Open Source Error Tracking

[![N|Solid](https://glitchtip.com/assets/logo-again.svg)](https://glitchtip.com/)

## Requires

- Pyhton 3.8
- Poetry
- Postgresql 13
- Redis
- NPM

```
sh install.sh
```

```
pm2 start --name glitchtip --interpreter python3 code/manage.py -- runserver
```

```
pm2 start --name glitchtip-celery sh -- code/bin/run-celery.sh
```