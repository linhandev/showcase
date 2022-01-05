import os
import os.path as osp

base = "/home/lin/Desktop/git/other/showcase/data/pascal"
labs = os.listdir(osp.join(base, "Annotations"))
imgs = os.listdir(osp.join(base, "JPEGImages"))
imgs_base = [n.split(".")[0] for n in imgs]

f = open("test_list.txt", "w")
s = [0, int(len(labs) * 0.8), int(len(labs) * 0.9), len(labs)]
for lab in labs[s[2] : s[3]]:
    img_idx = imgs_base.index(lab.split(".")[0])
    img_name = imgs[img_idx]
    print(f"JPEGImages/{img_name} Annotations/{lab}", file=f)
