from datasets import load_dataset
dataset = load_dataset('Ankursingh/openwebtext_10K')



for lines in dataset['train']:
    with open('openweb10k_train.txt','a', encoding='utf8') as f:
        f.write(lines['text'])

for lines in dataset['val']:
    with open('openweb10k_val.txt','a', encoding='utf8') as f:
        f.write(lines['text'])
