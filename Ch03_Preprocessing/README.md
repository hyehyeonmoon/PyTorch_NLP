## [Summary]

- Corpus 수집 및 정제하는 전체적인 과정에 대해 배웁니다.
- 정규식 표현을 배우고 실제로 이를 이용해 홈쇼핑(인터넷쇼핑) 리뷰를 전처리 해봅니다.
- Corpus labeling의 종류에 대해 배워봅니다.
- Tokenization의 필요성과 관련 tool들을 소개합니다.

## [File]

## [새롭게 알게 된 내용들]

### NLP Project Workflow

![Untitled](https://user-images.githubusercontent.com/55529617/106600548-ef0fe800-659d-11eb-9117-ce5275b27058.png)

### Preprocessing Workflow

정제 과정(Data cleaning)에서 

기계적인 노이즈 제거

→전형적인 노이즈 제거, 전각문자 변환

Interactive 노이즈 제거

→코퍼스의 특성에 따른 노이즈 제거, 일일이 작업하는 것

![Untitled 1](https://user-images.githubusercontent.com/55529617/106600544-ed462480-659d-11eb-9d5b-19e789b41e1e.png)

### Data crawling

![Untitled 2](https://user-images.githubusercontent.com/55529617/106600545-ee775180-659d-11eb-94a1-aa26c5880018.png)

### Tokenization

1. Sentence Segmentation →NLTK 이용
2. Tokenization→Mecab, KoNLPy 등의 POS tagger를 이용한 형태소 분석기 이용

(접어, 합성어, 교착어 나누기, 통일된 띄어쓰기를 위하여 시행)


