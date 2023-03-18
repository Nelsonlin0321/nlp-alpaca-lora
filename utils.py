import json
from textblob import TextBlob
import nltk
nltk.download('punkt')


def split_context_to_list(context, sentence_len=128):

    blob = TextBlob(context)
    final_sentence_list = []
    accumulate_len = 0
    windows_sentences = []
    for sentence in blob.sentences:

        word_len = len(sentence.words)
        if accumulate_len+word_len <= sentence_len:
            if not sentence.endswith("."):
                windows_sentences.append(str(sentence)+". ")
            else:
                windows_sentences.append(str(sentence))
            accumulate_len += word_len
        else:
            windows_sentence = " ".join(windows_sentences)
            final_sentence_list.append(windows_sentence)
            windows_sentences = [str(sentence)]
            accumulate_len = word_len

    if len(windows_sentences) > 0:
        windows_sentence = " ".join(windows_sentences)
        final_sentence_list.append(windows_sentence)

    return final_sentence_list


def save_json(object, file_path):
    with open(file_path, mode='w') as f:
        json.dump(object, f, indent=4)


def open_json(file_path):
    with open(file_path, mode='r') as f:
        json_object = json.load(f)
        return json_object
