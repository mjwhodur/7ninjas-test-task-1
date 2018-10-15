# Installing Conda Environment

Unfortunately, current version of Python (3.7+) does not support
older versions of Django Framework 1.11.16, which is required to run djangorestframework package.

## Dependency structure

* djangorestframework (current)
    * does not support Django 2+
        * django<2.0 -> Django 1.11.16
            * python<3.7 -> Python 3.6.5

This causes dependency hell which requires additional tweaking needed to run application.

## Solution

As stated before, only Python 3.6 is currently supported.
Django forums recommends to update Django to 2.0+, however our ```djangorestframework``` still does not support that.

We are ought to estabilish Python 3.6 environment. Currently, since there may be issues on operating systems requiring Python 3.7 it is advised to install conda environment.

### Downloading Conda

In the testing environment, installing Miniconda3 was enough to estabilish stable testing environment.
User/Developer is advised to install Anaconda or Miniconda environment. For more information regarding downloading  Conda head to www.conda.io

### Using Conda

After installing conda we have to create Python 3.6 environment, that will not conflict system Python installation.
```commandline
$ conda create -n py36 python==3.6
```
Conda will install needed libraries and commands in its home directory.

You can activate your new environment using

```commandline
$ source activate py36
```

Check the version of the environment using:
```commandline
(py36) $ python --version

```
You shall see following output:
```
Python 3.6.6 :: Anaconda, Inc.
```

To exit this environment in the terminal type:
```commandline
source deactivate
```
**If your distribution does yet not support Python 3.7 it is not required to use conda environment, however you may do that to avoid conflicting with your existing Python packages.**