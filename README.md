# Visdomino

A command-line utility to send all images in a directory to a
[Visdom](https://github.com/facebookresearch/visdom) server.

Install:

```
pip install git+https://github.com/lwneal/visdomino
```

## Example

Start a Visdom server:

```
python -m visdom.server --port 8097
```
Open `http://localhost:8097` and you should see an empty Visdom UI.


Then run visdomino:

```
visdomino --port 8097 --dir /home/username/my_pictures
```

Now all the JPG or PNG images in `my_pictures` should appear in your
Visdom environment.
