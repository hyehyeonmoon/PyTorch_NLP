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

### File
|File| Description|
|:-- |:-- |
|install_mecab_linux.sh|Mecab을 리눅스에서 설치하는 command|
|install_mecab_mac.sh|Mecab을 Mac에서 설치하는 command |
|tokenize.sh|review.sorted.uniq.refined.tsv 파일에서 리뷰를 Mecab 분석기를 통해 tokenization 실시|
|review.sorted.uniq.refined.tsv| 05-regex를 거친 정제된 홈쇼핑리뷰데이터|
