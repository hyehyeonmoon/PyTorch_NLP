## Subword segmentation 실습

(강의는 Mac 기반이어서 window일 경우 mecab도 안되고, 명령어도 다르기 때문에 실습이 진행 안됨)

```
#경로 설정
cd directory/11-subword_segmentation

#clone
clone shelll sciprt 실행

#text 부분만 따로 빼줌
cut -f2 review.sorted.uniq.refined.tsv > review.sorted.uniq.refined.tsv.text

#mecab을 적용하고, under scroe를 붙여주는 post_tokenize.py
cat ./review.sorted.uniq.refined.tsv.text | mecab -O wakati | python post_tokenize.py ./review.sorted.uniq.refined.tsv.text > review.sorted.uniq.refined.tsv.text.tok

#bpe 명령어 탐색
python ./subword-nmt/learn_bpe.py -h

#bpe 알고리즘 수행->model 파일에 저장됨
python ./subword-nmt/learn_bpe.py --input ./review.sorted.uniq.refined.tsv.text.tok --output ./model --symbols 30000

#만들어진 model 파일을 이용해 subword segmentation을 수행
python ,/subword-nmt/apply_bpe.py --codes ./model <review.sorted.uniq.refined.tsv.text.tok > review.sorted.uniq.refined.tsv.text.tok.bpe

#label과 subword segmentation 파일 합치기
cut -f1 ./review.sorted.uniq.refined.tsv > review.sorted.uniq.refined.tsv.label

paste ./review.sorted.uniq.refined.tsv.label ./review.sorted.uniq.refined.tsv.text.tok.bpe > review.sorted.uniq.refined.tok.bpe.tsv

#또는 shell script 이용해서 위의 업무를 한번에 할 수 있음
./tokenize.sh ./review.sorted.uniq.refined.tsv review.sorted.uniq.refined.tok.bpe.tsv
```

## 파일
|File |Description |
|:-- |:-- |
|clone.sh|subword segmentation model을 가져오는 코드 |
|post_tokenize.py|under score를 붙이는 함수 |
|tokenize.sh|label과 subword segmentation이 수행된 text 파일을 합치는 코드 |
|review.sorted.uniq.refined.tsv| 홈쇼핑 리뷰 raw data|

(여기에 없는 파일은 https://www.notion.so/11-subword_segmentation-33460324e29648d4a91a30c099cbe746 에 있습니다.)

