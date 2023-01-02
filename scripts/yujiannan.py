import random
from pathlib import Path

if __name__ == '__main__':
    train, val = [], []
    for dataset in Path("/root/Wav2Lip/data/output").iterdir():
        for d in dataset.iterdir():
            data = f"{dataset.name}/{d.name}"
            if random.random() < 0.95:
                train.append(data)
            else:
                val.append(data)
    with open("/root/Wav2Lip/filelists/train.txt", "w") as f:
        f.write("\n".join(train))
    with open("/root/Wav2Lip/filelists/val.txt", "w") as f:
        f.write("\n".join(val))
