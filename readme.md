# Gihtub Maker Tools

## Usage

### Create a repo.

```
python main.py -c -r testrepo
```

With docker.

```
docker run -it \
gihtub-maker-tools \
-c -r testrepo
```

### Delete a repo.

```
python main.py -d -r testrepo
```

With docker.

```
docker run -it \
gihtub-maker-tools \
-d -r testrepo
```

## Setup

Clone this repository.

`git clone https://github.com/bedardn93/GihtubMakerTools`

Create a `ght.ini` file with you info inside `GihtubMakerTools`.

```
[github.org]
User = bedardn93
Token = ghp_abcdefg
Organization = supertestorg123
```

Install everything.

```
pip install -r requirements.txt.
```

Or if using docker.

```
docker build -t gihtub-maker-tools .
```