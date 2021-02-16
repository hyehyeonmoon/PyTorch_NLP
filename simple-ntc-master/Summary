## [Summary]

- dataset과 dataloader를 통해 이전 data_loader 파일에서 구현했던 데이터 split, 전처리, shuffle+mini batch 구현을 더 간단히 해볼 수 있었다.
- PyTorch Ignite을 통해 짧고 간단하면서도 여러 모델 또는 상황에 적용 가능한 Boilerplate을 만들 수 있었다.

## **[File]**

|File|Description|
|:-- |:-- |
| custom_dataset_practice|dataset, dataloader을 이용해 이진분류 실습 |
| data_loader | MNIST dataset, load_mnist, get_loader을 이용해 train/valid/test set 분할 및 mini batch 만듦|
| model| LeakyReLU, BatchNorm, softmax를 사용한 DNN|
| train| argparser, main 함수로 신경망의 학습을 시작|
| trainer| PyTorch Ignite으로 구현되어 process function과 동작순서가 저장|
| utils| parameter, gradienr의 L2 norm을 구하는 함수|


## [새롭게 알게 된 내용들]

학습

```
#directory 설정

python train.py --model_fn ./models/review.pth --train_fn ./data/review.sorted.uniq.refined.tok.shuf.train.tsv --gpu_id -1 --batch_size 128 --n_epochs 10 --word_vec_size 256 --dropout .3 --rnn --hidden_size 512 --n_layers 4 --cnn --window_sizes 3 4 5 6 7 8 --n_filters 128 128 128 128 128 128
#rnn과 cnn의 ensemble model로 review.pth에 결과값 저장
```

![Untitled (3)](https://user-images.githubusercontent.com/55529617/108087992-50b27500-70bb-11eb-9c08-805bf3e85788.png)

[Test]

```
cut -f2 ./data/review.sorted.uniq.refined.tok.shuf.test.tsv | shuf | head -n 10 | python ./classify.py --model_fn ./models/review.pth --gpu_id 0
#test.tsv 파일에서 f2(text)부분만 가자ㅕ와서 shuf링을 한다음에 10개의 head만 가져와서 classify 파이썬 스크립트를 실행
#model은 review.pth에 있는 것을 사용한다.

echo "배송이 늦게 왔지만 제품 자체는 정말 좋네요." | mecab -o wakati | python ./classify.py --model_fn ./models/review.pth --gpu_id 0
문장에 대해 mecab tokenization을 해준 뒤 python 스크립트에서 실행하는데 review.pth model을 이용해서 만듦.
```
![Untitled (4)](https://user-images.githubusercontent.com/55529617/108087988-4f814800-70bb-11eb-941a-33d9c79ea3fa.png)

![Untitled (5)](https://user-images.githubusercontent.com/55529617/108087994-514b0b80-70bb-11eb-848e-95d159a90a29.png)
