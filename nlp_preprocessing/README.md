## [Summary]

### 과정

앞으로 실습에 사용할 데이터를 전처리 하는 과정입니다.

1. Data를 ctrl+c, ctrl+v를 통해 Excel에서 TSV 파일로 옮깁니다.
2. Shuffling을 한 이후 Train, Valid, Test set으로 나눕니다.(리눅스 사용)
3. mecab으로 한국어 Tokenization, moestokenizer로 영어 Tokenization 시행(리눅스 사용)
4. sub-nmt를 github에서 clone해서 Subword segmetation을 bpe를 통해 수행합니다.

### 데이터

데이터는 저작권의 문제로 주어지지 않습니다.

[AI-Hub](https://www.aihub.or.kr/sample_data_board](https://www.aihub.or.kr/sample_data_board)에서 "한국어-영어 번역 말뭉치"를 다운 받습니다. 

Excel로 다운받아지며 (한국어, 영어) 또는 (한국어, NMT) column을 ctrl+c, ctrl+v를 통해 txt 파일로 옮깁니다. 한국어와 영어 사이에 tab이 생성되어 tsv 파일 형태가 완성됩니다.

### 실행환경

window10에서 실습을 진행하기 위해서는 [여기](https://github.com/hyehyeonmoon/PyTorch_NLP/blob/main/env.md)를 참고해 주시기 바랍니다.

```
## 환경
Window10
WSL
Ubunta
Anaconda
Python 3.7

## 필요한 라이브러리
mecab
mosestokenizer
KoNLpy
torch

## subword-nmt file 다운받는 곳

For subword segmentation, you can clone the following repository:
https://github.com/kh-kim/subword-nmt

If you are using Microsoft Windows, you can download Cygwin to mimic linux command-line environment.

URL: https://www.cygwin.com/


```

### Tip

subword segmentation에서 lean_bpe.py를 실행할 때, vocab을 2만~3만으로 만들기 위해서 Symbol을 지정

영어는 5만 정도, 한국어는 3만 정도로 지정하고 상황에 따라 symbol을 늘렸다 줄었다 하면 된다.

## [File]

|File |Description|Folder|
|:-- |:-- |:--|
|data files|한국어영어 말뭉치 txt, tsv, 전처리 한 파일들 모아놓는 곳|/data|
|divide_train_valid_test|데이터를 train, valid, test set으로 나누는 명령어 | /data|
|Tokenization|Tokenization을 실행| /data|
|subword_segmentation|subword segmentation을 실행| /data|
|post_tokenize|'_"를 붙여주는 역할|.|
|detokenizer|토큰화된 말뭉치를 원상복귀시키는 역할  |. |
|tokenizer|.|.|
|learn_bpe|train set에서 bpe를 학습시키는 것|/subword_nmt|
|apply_bpe|학습시킨 bpe를 train, valid, test set에 적용해 subword segmentation 수행|/subword_nmt|


