import sys
from src import train_sentence

def test_training():
    train_sentence.train(model_prefix='test_model',data_path='test/test_file.txt')
