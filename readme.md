# Github Maker Tools

## Usage

Create a repo.

```
docker run -it \
github-maker-tools \
-c -r testrepo
```

Delete a repo.

```
docker run -it \
github-maker-tools \
-d -r testrepo
```

## Install and setup

Clone this repository.

`git clone https://github.com/bedardn93/GihtubMakerTools`

Create a `ght.ini` file with you info inside `GithubMakerTools`.

```
[github.org]
User = bedardn93
Token = ghp_abcdefg
Organization = supertestorg123
```

Build container image.

```
docker build -t github-maker-tools .
```