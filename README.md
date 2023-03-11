# No, this is PaGPTrick
## Fine-tuning GPT-2 with Spongebob

This *educational* repository contains code for fine-tuning GPT-2 on dialogue from the TV series Spongebob Squarepants.

The code for fine-tuning GPT-2 comes from Karpathy's [NanoGPT](https://github.com/karpathy/nanoGPT)

0. [Setup](#setup)
1. [Scraping](#scraping)
2. [preprocessing](#preprocessing)
3. [training](#training)
4. [sampling](#sampling)

## Setup
`conda env create -f environment.yml`


## Scraping

Spongebob transcripts can be scraped from the [fandom website](https://spongebob.fandom.com/) using the `scrape.py` script and `Selenium`. The scripts for each episode are stored in `data`, and the full transcript of every episode is stored in `spongebob_anthology.txt`.

## Preprocessing

The `preprocess.py` script takes the full transcript and simply removes non-dialogue lines. The result is stored in `spongebob_anthology_cleaned.txt`.

## Training

Use `train.py` to train the model, with the either the following arguments
- `python train.py config/train_spongebob_char.py` to train from scratch and output to `out_spongebob_char`.
- `python train.py config/finetune.py` to train from GPT2 and output to `out_spongebob_gpt`.

## Sampling

Use `sample.py` to sample from the model

Example:
- `python sample.py --out_dur={specified output dir} --start="{starting text}" --num_samples={number of samples}`