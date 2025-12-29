import torch
import torch.nn as nn
import torch.optim as optim

# 1. 데이터: 리스트와 텐서만 사용
sentences = ["happy", "i love this", "it is great", "i hate it", "it is bad"]
labels = torch.tensor([1.0, 1.0, 1.0, 0.0, 0.0])  # 긍정 1, 부정 0

# 2. 아주 간단한 단어 사전 (Python 기본 dict 사용)
words = list(set(" ".join(sentences).split()))
word_to_idx = {word: i for i, word in enumerate(words)}
vocab_size = len(word_to_idx)

# print(" ".join(sentences).split())
# print(word_to_idx)
# print(vocab_size)
class Model(nn.Module):
    def __init__(self, size):
        super().__init__()
        self.embed = nn.Embedding(size, 3)
        self.fc = nn.Linear(3, 1)
        self.sigmoid = nn.Sigmoid()
    def forward(self, x):
        embedded = self.embed(x)
        pooled = torch.mean(embedded, dim=0)
        score = self.fc(pooled)
        return self.sigmoid(score)


model = Model(vocab_size)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.1)

print("학습 시작")
for epoch in range(1000):
    total_loss = 0
    for i in range(len(sentences)):
        sentence_indices = torch.tensor([word_to_idx[w] for w in sentences[i].split()])
        label = torch.tensor([labels[i]])
        prediction = model(sentence_indices)

        loss = criterion(prediction, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    if epoch % 10 == 0:
        print(f"반복 {epoch+1}/100, 오차: {total_loss/4:.4f}")

test_sentence = "love"
test_indices = torch.tensor([word_to_idx[w] for w in test_sentence.split()])
model.eval()
with torch.no_grad():
    prediction = model(test_indices)
    prob = prediction.item()

print(test_sentence)
print(prob * 100)


# class PureTorchModel(nn.Module):
#     def __init__(self, vocab_size, embed_dim):
#         super().__init__()
#         self.embedding = nn.Embedding(vocab_size, embed_dim)
#         self.fc = nn.Linear(embed_dim, 1)
#         self.sigmoid = nn.Sigmoid()
#
#     def forward(self, x):
#         # x는 단어 인덱스들이 담긴 텐서
#         embeds = self.embedding(x)
#         # mean() 함수를 써서 문장의 평균 벡터 계산 (NumPy 없이 텐서 연산)
#         pooled = torch.mean(embeds, dim=0)
#         return self.sigmoid(self.fc(pooled))
#
#
# # 4. 모델 설정
# model = PureTorchModel(vocab_size, embed_dim=4)
# criterion = nn.BCELoss()
# optimizer = optim.Adam(model.parameters(), lr=0.05)
#
# # 5. 학습 루프
# for epoch in range(50):
#     for i, sen in enumerate(sentences):
#         # 텍스트 -> 인덱스 리스트 -> 파이토치 텐서
#         indices = torch.tensor([word_to_idx[w] for w in sen.split()], dtype=torch.long)
#
#         optimizer.zero_grad()
#         output = model(indices)
#         loss = criterion(output, labels[i].unsqueeze(0))
#         loss.backward()
#         optimizer.step()
#
# # 6. 저장하기 (NumPy 없이 .pth 파일로 저장)
# # 이 방식은 모델의 가중치값들(Tensor)만 파일로 뽑아냅니다.
# torch.save({
#     'model_state_dict': model.state_dict(),
#     'vocab': word_to_idx  # 사전도 딕셔너리 형태로 함께 저장 가능
# }, "my_model.pth")
#
# print("학습 및 저장 완료! (NumPy 사용 안 함)")