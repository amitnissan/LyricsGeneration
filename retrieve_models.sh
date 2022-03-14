echo "### Downloading models from google drive ###"

echo "installing gdown for downloading from drive"
pip install gdown

echo "##### retrieving models, this may take time #####"
#gdown --folder --id 1qzf9u0VkhjbC-QaZNve3fez899vF6fD5

gdown --folder --id 1ghZclFond80_I-D9OZphk_xm7SpBbfso # avicii
rm ~/.cache/gdown/cookies.json
gdown --folder --id 1YT9TYVbtGkNZ4I41RNvzHGvJhBYciHGi # beatles
rm ~/.cache/gdown/cookies.json
gdown --folder --id 1omMEmvNO31seBIGqhxkOGr0vBPKDawbL # britney
rm ~/.cache/gdown/cookies.json
gdown --folder --id 1jx8q7US8N0g8voX5gD3AvBca2eqPPdz0 # kanye
rm ~/.cache/gdown/cookies.json
gdown --folder --id 1LDVwdp9mznxBUFO2438B3P_oc-XMEnLa # nirvana
rm ~/.cache/gdown/cookies.json

echo "### finished downloading ###"


