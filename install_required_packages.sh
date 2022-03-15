# Installing required packages

if [ -d "transformers" ]
then
  if pip show transformers | grep Version | grep -q '4.18.0.dev0'
  then
    echo "Newer version of transformers already installed"
  else
    echo 'Installing a newer version of transformers library'
    pip install -e transformers/
    echo "finished installing"
  fi
else
  echo "Installing a newer version of transformers library"
  echo 'Cloning repo'
  git clone https://github.com/huggingface/transformers.git
  echo 'Installing package'
  pip install -e transformers/
  echo "finished installing"
fi


if pip show bert_score | grep Version | grep -q '0.3.11'
then
  echo "bert_score already installed"
else
  echo "Installing bert_score"
  pip install bert_score==0.3.11
  echo "finished installing"
fi