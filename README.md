# Visdomino

A command-line utility to send all images in a directory to a Visdom
server.

Install:

```
pip install git+https://github.com/lwneal/visdomino
```

## Example

Start a Visdom server:

```
python -m visdom.server --port 8097
```

Then run visdomino:

```
visdomino --port 8097 --dir /home/username/my_pictures
```

Now open `http://localhost:8097` and all image files in `my_pictures`
should be displayed.
