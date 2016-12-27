Docker integration
==================

### Build an image

To build the Git repo into an image type in:

```
docker build -t mote-phat .
```

For a leaner image you can use Alpine Linux:

```
docker build -t mote-phat . -f Dockerfile.alpine
```

### Run an image

```
docker run --privileged -ti mote-phat
```

The base Dockerfile is built to run the `test.py` file but you can override the `CMD` instruction to run whatever you want. Imagine you created your own file called rainbows.py.

```
FROM mote-phat
COPY rainbows.py .
CMD ["python", "rainbows.py"]
```

For more information check out the tutorials by Alex Ellis here:

* [Docker & Pi tutorials](http://blog.alexellis.io/tag/raspberry-pi/)


