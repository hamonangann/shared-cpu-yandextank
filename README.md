# Shared-CPU-Yandex.Tank

This is for research purpose (WIP)

### Installation

Prerequisite: Docker

```
docker run \
    -v $(pwd):/var/loadtest \
    -v $SSH_AUTH_SOCK:/ssh-agent -e SSH_AUTH_SOCK=/ssh-agent \
    --net host \
    -it yandex/yandex-tank
```