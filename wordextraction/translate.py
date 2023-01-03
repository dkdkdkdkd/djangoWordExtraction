# pip install googletrans==4.0.0-rc1

from googletrans import Translator
from .models import WordDb
import re


def engToKr(word):  # 영어 한국어로 번역
    translator = Translator()
    temp = translator.translate(word, src='en', dest='ko')  # 번역

    kr = re.sub(r"[^ ㄱ-ㅣ가-힣+]", "~", temp.text)  # 번역 실패시  "" 반환

    return kr


def makeWordDic(words):
    for word in words:
        kr = engToKr(word)
        if kr[0] == "~":
            continue
        else:
            WordDb.objects.create(
                eng=word,
                kor=kr
            )

if __name__ == "__main__":
    pass
