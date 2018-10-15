# SimpleShop Documentation file (markdown)

## Basic repository information
This project is intented to test my skills against Python3 and capability to cooperation with 7ninjas Company based in Rzeszow, Poland.

## Task specification
For more detailed information regarding task specification go to [Specification.md](ProjectSpecification/Specification.md)

## Toolchain
Applications and services used to solve this task:
* macOS High Sierra 10.12 / Manjaro Linux (rolling)
* PyCharm Community (2018.2.4)
* JetBrains Toolbox
* Django 1.11.16
* Django Rest Framework 3.8.2

## Frameworks

Application requires following frameworks:

* Django 1.11.16
* Django Rest Framework 3.8.2
* pytz (current)

They may be installed using
```bash
(venv)$ pip install -r requirements.txt
```

It is advised to use Virtual Environment when running this App.

## Running in modern distributions
Modern Linux distributions come with Python 3.7 preinstalled, however
Django 1.11+ is not currently compatible with current version.

[Solution](docs/InstallingConda.md)

## Deployment

### Local machine
```commandline
cd ninja
python -m manage migrate
python -m manage runserver
```
