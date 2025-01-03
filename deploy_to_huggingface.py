import tensorflow as tf
from transformers import AutoTokenizer, TFT5ForConditionalGeneration, TFAutoModelForSeq2SeqLM
from huggingface_hub import login

LOCAL_QG_MODEL_PATH = "C:/projects/question-generator/translator-eng-indo" 
TOKEN_HUGGINGFACE = "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"

# model = TFT5ForConditionalGeneration.from_pretrained(LOCAL_QG_MODEL_PATH, from_pt=False)
# tokenizer = AutoTokenizer.from_pretrained("t5-small")

translator_model = TFAutoModelForSeq2SeqLM.from_pretrained(LOCAL_QG_MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained("t5-small")

login()

translator_model.push_to_hub("blaxx14/t5-translator-eng-indo")
