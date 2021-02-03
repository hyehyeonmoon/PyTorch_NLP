
## train, test set으로 나누기
```
gshuf < review.sorted.uniq.refined.tok.tsv >review.sorted.uniq.refined.tok.shuf.tsv
```

## 파일

|File |Description|
|:-- |:-- |
|data_loader|Field, TabularDataset.splits, BucketIterator.splits, build_vocab를 이용해 train, vaild set 만들기  |
|torchtext|data_loader를 train data에 적용해서 살펴보기 |
