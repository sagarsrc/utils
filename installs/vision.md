# vision env

```bash
######### conda #########
# create env

conda create -n mp python=3.8 pandas numpy jupyter ipykernel black

# nodejs for jupyterlab
conda install -c "conda-forge/label/cf201901" nodejs

# macos cpu version
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 -c pytorch

# linux cpu version
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# linux gpu version
## cuda 12.1
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

## cuda 11.8
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia


# transformers (not working)
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

# env
pip install python-dotenv

# opencv
pip install opencv-python

# plots
pip install matplotlib
pip install seaborn

# aws
pip install awscli
pip install boto3

# utils
pip install PyMuPDF
pip install --upgrade tqdm
pip install --upgrade cutility
#########################
```
