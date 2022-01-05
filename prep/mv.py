import os
import os.path as osp

base = (
    "/home/lin/Desktop/git/other/ImageNet-datasets-downloader/imgnet/imagenet_images/"
)
fdrs = os.listdir(base)
fdrs.remove("all")
print(fdrs)
input("here")

for fdr in fdrs:
    imgs = os.listdir(osp.join(base, fdr))
    for img in imgs:
        img_path = osp.join(base, fdr, img)
        dst_path = osp.join(base, "all", f"{fdr}-{img}")
        cmd = f"cp {img_path} {dst_path}"
        print(cmd)
        os.system(cmd)
