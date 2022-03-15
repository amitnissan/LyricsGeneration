# How a Song Is Born

Using Deep Learning Models to Produce a Custom Song By Your Favorite Artist

Natural Language Processing - 097215, Technion

## Usage

After downloading the project to `path/of/project/`, run the following:

1. `conda activate py38_pytorch`
2. `cd path/of/project/`
3. `chmod +x *.sh`

### (A) Using prepared models:

Interface for running trained models.<br>
To use: run `./generate_song_interface.sh`

Note: prepared models are the models we reported in the paper. This flow will download the models from google drive and
inference a new song with your given text.<br><br>
<b>Important</b>: Google can occasionally block the download if it was accessed too frequently. If the download fails,
one can either try again or download the models directly from
the drive (just download the content of `trained_models/` to `path/of/project/trained_models/`).

### (B) Training your own model:

run `./fine_tune_and_generate_song.sh`<br>
This will train the model on an artist of your choice and generate a song from your given sentence.

## User's input

You'll be presented with the following prompt:

```
*・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.*.。.:*・☆・゜・*:.。.:*・☆・゜・*:.。.*.。.:*・゜・*
		♪♫♪ Welcome to our lyric generation machine ♪♫♪

Here are the artists for today:
	# 0: Beatles
	# 1: Britneyspears
	# 2: Kanye
	# 3: Nirvana
	# 4: Avicii

Please enter # of artist of choice:
```

Enter the <b>number</b> of the artist of choice.<br>
Then, you'll choose the subject - that will be the opening of our new generates song.

```
Enter a sentence you wish Avicii start with (for example: "COVID-19 was like a"...). Plain text no quotes needed:
```

After entering the subject (plain text no quotes), you will see the following message:

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
