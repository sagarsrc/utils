# linux machine

```bash
# get miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Ctrl^C and skip user agreement
```

# conda env handle

```bash
# activate base enviornment
conda activate base

# new env
conda create -n {env_name} python=3.8 pandas numpy jupyter ipykernel

# conda activate newly created env
conda activate {env_name}

# remove env
conda remove -n {env_name} --all

```

# base

```bash
# basics
conda install ipykernel jupyter pandas numpy

# all ipykernels install
conda install nb_conda_kernels

# lab
conda install -c conda-forge jupyterlab

# jupyter extensions
conda install -c conda-forge jupyter_contrib_nbextensions

# notebook format
pip install jupyter-black

# ipywidgets
conda install -c conda-forge ipywidgets
jupyter nbextension enable --py widgetsnbextension

```

# jupyter lab / notebook

```bash
# add this in the beginning of jupyter lab or notebook
import jupyter_black
jupyter_black.load()

# run cells it will be formatted automatically
```
