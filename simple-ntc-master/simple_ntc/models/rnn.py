import torch.nn as nn


class RNNClassifier(nn.Module):

    def __init__(
        self,
        input_size, #vocab size로 cocrpus에 의해 정해지게 됨
        word_vec_size,
        hidden_size,
        n_classes,
        n_layers=4,
        dropout_p=.3,
    ):
        self.input_size = input_size  # vocabulary_size
        self.word_vec_size = word_vec_size
        self.hidden_size = hidden_size
        self.n_classes = n_classes
        self.n_layers = n_layers
        self.dropout_p = dropout_p

        super().__init__()

        self.emb = nn.Embedding(input_size, word_vec_size)
        self.rnn = nn.LSTM(
            input_size=word_vec_size,
            hidden_size=hidden_size,
            num_layers=n_layers,
            dropout=dropout_p,
            batch_first=True,
            bidirectional=True,
        )
        self.generator = nn.Linear(hidden_size * 2, n_classes)
        # We use LogSoftmax + NLLLoss instead of Softmax + CrossEntropy
        # 두 조합의 차이는 output을 y로 나타낼지 log y로 나타낼지의 차이
        # LogSoftmax + NLLLoss가 더 계산 면에서 아주 약간 낫다고 함
        self.activation = nn.LogSoftmax(dim=-1)

    def forward(self, x):
        # |x| = (batch_size, length)
        x = self.emb(x)
        # |x| = (batch_size, length, word_vec_size)
        x, _ = self.rnn(x)
        # |x| = (batch_size, length, hidden_size * 2)
        y = self.activation(self.generator(x[:, -1])) 
        # (x[:, -1]=(batch_size, 1, hidden_size*2), 
        # self.generator=(batch_size, n_classes)
        # |y| = (batch_size, n_classes)

        return y
