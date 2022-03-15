#!/bin/sh

./install_required_packages.sh
if pip show gdown | grep Version | grep -q '4.4.0'
then
  echo "gdown already installed"
else
  echo "Installing gdown"
  pip install gdown==4.4.0
  echo "finished installing"
fi

/anaconda/envs/py38_pytorch/bin/python interface.py
