import sentencepiece as spm
from datetime import datetime
import argparse


def train(model_prefix, data_path):
    
    spm.SentencePieceTrainer.train(input=data_path,
                                    model_prefix=model_prefix, vocab_size=1000
                                    )

def test(model_prefix):
    sp = spm.SentencePieceProcessor(model_file=model_prefix+'.model')
    encoded_text = sp.encode('SentencePiece is a powerful tool for subword text tokenization and is widely used in natural language processing tasks.',
                             out_type=str)
    print(encoded_text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Training Sentence Piece",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--test", action="store_true", help="test model")

    args = parser.parse_args()

    current_date = datetime.now().strftime('%Y-%m-%d')
    model_prefix = f'models/{current_date}'

    if args.test:
        # Then, test the model
        test(model_prefix)
    else:
        # Run the complete training process
        train(model_prefix, 'data/openweb10k_train.txt')