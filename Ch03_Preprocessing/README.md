## [Summary]

- Corpus 수집 및 정제하는 전체적인 과정에 대해 배웁니다.
- 정규식 표현을 배우고 실제로 이를 이용해 홈쇼핑(인터넷쇼핑) 리뷰를 전처리 해봅니다.
- Corpus labeling의 종류에 대해 배워봅니다.
- Tokenization의 필요성과 관련 tool들을 소개합니다.
- subword segmentation과 detokenization을 알아봅니다.
- 병렬 코퍼스를 정렬 하는 방법에 대해 배웁니다.
- torchtext를 이용해 정제한 text data를 mini-batch train, valid, test set으로 만듭니다.

## [File]

|Folder| Description|
|:-- |:-- |
|05-regex |정규표현식을 이용한 data cleaning 실습|
|08-tokenization |Mecab을 이용한 tokenization 실습 |
|11-subword_sementation |tokenization 된 text를 더 세분화하게 나눔 |
|13-detokenization|subword segmentation을 한 data를 다시 원상복귀하는 실습 |
|18-torchtext|정제한 text data를 mini-batch train, valid, test set으로 만드는 실습 |

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

### Procedure to Build Parallel Corpus

1. Bi-lingual Corpus 정제(노이즈 제거)
2. Tokenization 수행(No subword segmentation)
3. 각 언어별 코퍼스에 대해서 word embedding 수행(FastText 활용)
4. MUSE를 활용하여 word translation dictionary 추출
5. Champollion을 활용하여 align 수행

### 미니배치의 형태

![Untitled](https://user-images.githubusercontent.com/55529617/106778609-80a85400-6689-11eb-874c-5cf85b66e8f3.png)

![Untitled (1)](https://user-images.githubusercontent.com/55529617/106778619-82721780-6689-11eb-9d88-95d9b9f7c182.png)

## Reference

[김기현의 딥러닝을 활용한 자연어처리 입문 올인원 패키지 Online. | 패스트캠퍼스](https://www.fastcampus.co.kr/data_online_dpnlp)
