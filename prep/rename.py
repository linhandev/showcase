import os
import os.path as osp

ann_dir = "./data/pascal/Annotations"
anns = os.listdir(ann_dir)
imgs_full = os.listdir("./data/pascal/JPEGImages")
imgs = [i.split(".")[0] for i in imgs_full]

for ann in anns:
    idx = imgs.index(ann.split(".")[0])
    img = imgs_full[idx]
    new_ann = "_".join(img.split(".")) + ".xml"
    print(osp.join(ann_dir, ann), osp.join(ann_dir, new_ann))
    os.rename(osp.join(ann_dir, ann), osp.join(ann_dir, new_ann))
