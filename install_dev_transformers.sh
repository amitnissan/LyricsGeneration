echo "Installing a newer version of transformers library"

#if pip show transformers | grep Version | grep -q '4.18.0.dev0'
#then
#  echo "Newer version of transformers already installed"
#else
#  git clone https://github.com/huggingface/transformers.git
#  pip install -e transformers/
#  echo "finished installing"
#fi

echo 'Cloning repo'
git clone https://github.com/huggingface/transformers.git

echo ''
pip install -e transformers/
pip install bert_score==0.3.11

echo "finished installing"


