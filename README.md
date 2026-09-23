# testandoo

## criar imagem
``` bash
podman build -t python-estudo .
``` 

## montar ambiente de estudos
``` bash
podman run --rm -it \
    -v "$PWD:/estudo:Z" \
    python-estudo
```