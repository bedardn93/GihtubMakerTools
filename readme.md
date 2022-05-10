# Github Maker Tools

## Install and setup

Add `ght.ini` file and appropriate info.

```
[github.org]
User =
Token =
Organization =
```

Build container image.

```
docker build -t github-maker-tools .
```

Run and enter container.

```
docker run -it github-maker-tools \
    github-maker-tools COMMAND...
```

