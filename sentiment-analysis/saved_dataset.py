from datasets import load_dataset
import torch
# Tải dữ liệu từ IMDb dataset
train_data, test_data = load_dataset("imdb", split=["train", "test"])


# Lưu trữ cục bộ dữ liệu
train_data.save_to_disk("./Data/imdb/train")
test_data.save_to_disk("./Data/imdb/test")
