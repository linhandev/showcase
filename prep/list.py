import os
import os.path as osp
import random

base = "./data/pascal/"
labs = os.listdir(osp.join(base, "Annotations"))
imgs = os.listdir(osp.join(base, "JPEGImages"))
imgs_base = [n.split(".")[0] for n in imgs]

random.shuffle(labs)

s = [0, int(len(labs) * 0.9), int(len(labs) * 0.95), len(labs)]


def gen_list(num):
    names = ["train_list.txt", "val_list.txt", "test_list.txt"]
    f = open(f"./data/pascal/{names[num]}", "w")
    for lab in labs[s[num] : s[num + 1]]:
        try:
            img_idx = imgs_base.index(lab.split(".")[0])
        except:
            print(f"Image for {lab} not fond")
            continue
        img_name = imgs[img_idx]
        print(f"JPEGImages/{img_name} Annotations/{lab}", file=f)


for idx in range(3):
    gen_list(idx)
