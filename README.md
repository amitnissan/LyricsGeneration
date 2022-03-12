# How a Song Is Born
Using Deep Learning Models to Produce a Custom Song By Your Favorite Artist

Natural Language Processing - 097215, Technion

## Installation
This projects requires a newer version of `huggingface`'s `tranformers` library. <br>
run the following:

```bash
conda activate py38_pytorch
/anaconda/envs/py38_pytorch/bin/python main.py
```
<b>Important notice</b>: In some cases, you'll need to run `main.py` twice for the library to be installed.

## Usage
Once the library is successfully installed, you'll be presented with the following prompt:
```
*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*
		♪♫♪ Welcome to our lyric generation machine ♪♫♪

Here are the artists for today:
	# 0: Avicii

Please enter # of artist of choice:
```

Enter the <b>number</b> of the artist of choice.<br>
Then, you'll choose the subject - that will be the opening of our new generates song.

```
Enter a sentence you wish Avicii start with (for example: "COVID-19 was like a"...):
```

After entering the subject, you will see the following message. Please allow some time, as the model fine tune itself with the artist of choice:
```
*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*
		♪♫♪ Generating a new song by Avicii talking about 'COVID-19 was like a'... ♪♫♪
```

After the process is done, you'll see:
```
*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*
		♪♫♪ This is 'COVID-19 was like a' by Avicii ♪♫♪
```
And your generated newly born song right after. Enjoy!