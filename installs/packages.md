# linux machine

```bash
# get miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Ctrl^C and skip user agreement
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
conda install -c conda-forge black nb_black
```

# jupyter lab / notebook

```bash
# notebooks
%load_ext nb_black

# lab
%load_ext lab_black

# run cells it will be formatted automatically
```

# conda env handle

```bash
# new env
conda create -n {env_name} python=3.8 pandas numpy jupyter ipykernel

# remove env
conda remove -n {env_name} --all
```

# custom envs

## chatbot env

```bash
######### conda #########
# create env
conda create -n llm python=3.8 pandas numpy jupyter ipykernel nltk black

# ipywidgets
conda install -c conda-forge ipywidgets
jupyter nbextension enable --py widgetsnbextension

# nodejs for jupyterlab
conda install -c "conda-forge/label/cf201901" nodejs

# macos cpu version
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 -c pytorch

# linux cpu version
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# transformers
# conda install -c huggingface transformers

# yaml file support
conda install -c conda-forge pyyaml
#########################


######### pip #########

# hugging face transformers
pip install transformers
pip install sentencepiece
pip install protobuf

# hugging face cli and hub
pip install --upgrade huggingface_hub

# langchain
pip install langchain

# llama-index
pip install llama-index

# faiss
pip install faiss-cpu

# sentence to embedding
pip install sentence-transformers

# env
pip install pydotenv

# quantization
pip install bitsandbytes accelerate

# plots
pip install matplotlib
pip install seaborn

# utils
pip install youtube-transcript-api

# scrape and clean
pip install beautifulsoup4
pip install requests
pip install emoji
pip install clean-text
pip install Unicode

# utils
pip install --upgrade tqdm
#########################
```
