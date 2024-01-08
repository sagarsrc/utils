# chatbot env

```bash
######### conda #########
# create env
conda create -n llm python=3.8 pandas numpy jupyter ipykernel nltk black


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
pip install python-dotenv

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
