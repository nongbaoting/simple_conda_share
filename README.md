# simple_conda_share

a python script that produce a concise conda environment file contain only the main packages name and version 

`conda env export` export all environment packages

`conda env export  --from-history ` export user manually installed package names in history but may miss package version

my python script is able to export user manually installed package names in history and specific package version
# Install
Required: `python >=3.6`

`pip install fire`

# Usage
```
python3 simple_conda_share.py  --env_name fusion
```

# Result
` fusion.simple_conda_share.yml`
```
$ cat fusion.simple_conda_share.yml
name: fusion
channels:
dependencies:
  - arriba=1.2.0
  - pip=19.3.1
  - python=3.8.0
  - star=2.7.3a
  - star-fusion=1.7.0
  - pip:
    - fire==0.2.1
    - six==1.13.0
    - termcolor==1.1.0

```