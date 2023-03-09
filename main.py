!pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
!pip install transformers requests beautifulsoup4 pandas numpy
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

class sentiment:
    def findScore(self, review):
        tokens = tokenizer.encode(review, return_tensors='pt')
        result = model(tokens)
        score = int(torch.argmax(result.logits))+1
        positive = (score/5)*100
        negative = ((5-score)/5)*100
        return positive, negative