
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

### File
|File| Description|
|:-- |:-- |
|refine |refine.regex, review.sorted.uniq.tsvf를 받아 전각 문자를 모두 반각 문자로 반환|
|refine.regex |전각 문자, 반각 문자 들어가 있음|
|review.sorted.uniq.tsv |label과 함께 들어있는 홈쇼핑리뷰 raw data |
|review.sorted.uniq.refined.tsv |정규식 data cleaning을 거친 결과 |

(여기에 없는 파일은 https://www.notion.so/05-regex-1cfea82e2a7b482ba3cdd482a2677cf4 에 저장되어 있습니다.)
