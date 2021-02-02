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

### 정규식 실습

1. refine 파일을 이용해 전각 문자를 모두 반각 문자로 전환
2. 1번 과정을 거친 파일을  sublime text3에서 열어 비정상적인 단어들을 찾아(ctrl+f) 정규식표현을 이용하여 제거
3. review.sorted.uniq.refined.tsv에 저장

Sublime text3 설치

```
# 실행방법
cd directory/05-regex

python refine.py refine.regex.txt 1 <review.sorted.uniq.tsv> review.sorted.uniq.refined.tsv
```

(하지만 강의에서는 Mac 기반이었으며 Window10의 cmd 창에서 실행해 본 결과 unicode error가 떴으며, open(—, encoding="UTF-8")으로 refine 파일 코드를 수정했으나 index out error가 떠서 실습을 진행하지 못하게 되었다.)

### 형태소 분석기를 활용한 Tokenization 실습

1. Mecab Window10에 설치
2. review.sorted.uniq.refined.tsv 파일에서 리뷰를 Mecab 분석기를 통해 tokenization 실시

```
# 실행방법
cd directory/08-tokenization

## 결과확인
cut -f2 ./review.sorted.uniq.refined.tsv | mecab -O wakati | head -n 2
#(위의 식이 window에서 돌아가지 않는다면, 아래 식을 실행)
#cut -f2 review.sorted.uniq.refined.tsv | mecab -O wakati | head -n 2

## 라벨과 Tokenization 결과 함께 저장
## shell script 속 코드를 이용(파일 올려져 있음)
./tokenize.sh review.sorted.uniq.refined.tsv review.sorted.uniq.refined.tok.tsv
```

(Mecab은 window에서 사전설치가 까다로운데, 강의는 설치방법을 알려주지 않으므로 실제 설치를 해도 잘 돌아가지 않는 경우가 있다. Python에서는 잘 돌아갔지만 cmd 창에서는 돌아가지 않아서 역시 실습을 진행하지 못하게 되었다.)
