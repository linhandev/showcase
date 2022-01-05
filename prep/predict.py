import os
import os.path as osp

from tqdm import tqdm
import paddlex as pdx
import cv2


opd = "./prep/ann"

img_dir = "./prep/img"
imgs = os.listdir(img_dir)
imgs.sort()
print(imgs)

# start_name = "sneakers-image206.jpg"
# try:
#     start_index = imgs.index(start_name)
# except ValueError:
#     start_index = 0
# imgs = imgs[start_index:]

# imgs = [i for i in imgs if i.startswith("soccer_shoes-image")]

print(f"Doing prediction on {len(imgs)} images")

input("continue ")

predictor = pdx.deploy.Predictor("./inference/ppyolov2")


def toPascal(fname, size, bbs, names):
    """Generate pascal format xml from detection result

    Parameters
    ----------
    fname : str
        image file name
    size : list
        WHC
    bbs : list
        [[wmin, hmin, wmax, hmax],[],...,[]]
    names : list
        name of object

    Returns
    -------
    str
        pascal format xml

    """
    objects = ""
    for b, name in zip(bbs, names):
        objects += f"""
        <object>
          <name>{name}</name>
          <pose>Unspecified</pose>
        	<truncated>0</truncated>
          <difficult>0</difficult>
          <bndbox>
            <xmin>{int(b[0])}</xmin>
            <ymin>{int(b[1])}</ymin>
            <xmax>{int(b[2])}</xmax>
            <ymax>{int(b[3])}</ymax>
          </bndbox>
        </object>
        """

    xml = f"""
    <annotation>
    <folder>JPEGImages</folder>
    <filename>{fname}</filename>
    <source>
      <database>Unknown</database>
    </source>

    <size>
      <width>{size[0]}</width>
      <height>{size[1]}</height>
      <depth>{size[2]}</depth>
    </size>
    <segmented>0</segmented>
    {objects}
    </annotation>
    """

    return xml


for img_name in tqdm(imgs):
    print(img_name)
    img = cv2.imread(osp.join(img_dir, img_name))
    results = predictor.predict(img)
    print(results)
    bbs = []
    scores = []
    for r in results:
        if r["score"] < 0.3:
            continue
        t = r["bbox"].copy()
        t[2] += t[0]
        t[3] += t[1]
        bbs.append(t)
        scores.append(r["score"])
    # print(max(scores))
    names = ["shoe"] * len(bbs)
    f = open(osp.join(opd, img_name.split(".")[0] + ".xml"), "w")
    xml = toPascal(img_name, img.shape, bbs, names)
    # print(xml)
    print(xml, file=f)
    f.close()
    # input("here")

    # img = pdx.det.visualize(img, results, threshold=0.3, save_dir=None)
    # cv2.imshow("result", img)
    # cv2.waitKey()
