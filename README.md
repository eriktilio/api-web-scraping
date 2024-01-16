# Requirements

- [Python 3.10.6](https://www.python.org/downloads/release/python-365/)
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

# Getting Started

## Execute API

### Create the virtualenv environment:

_The `{env_name}` must be renamed by the name that you wanna put to the environment_

```
python3 -m virtualenv {env_name}
```

or

```
python -m virtualenv {env_name}
```

or

```
py -3 -m virtualenv {env_name}
```

### Activate virtualenv environment

Linux:

```
source {env_name}\bin\activate
```

Windows:

```
{env_name}\Scripts\activate
```

### Deactivate virtualenv

Linux:

```
deactivate
```

Windows:

```
{env_name}\Scripts\deactivate
```

### Install project dependencies

```
python -m pip install -r requirements.txt
```

or

```
pip install -r requirements.txt
```

### Start project

```
uvicorn main:app --reload
```

or

```
python -m uvicorn main:app --reload
```

### Export project dependencies

```
pip freeze > requirements.txt
```

or

```
python -m pip freeze > requirements.txt
```
