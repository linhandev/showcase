import paddlex as pdx
from paddlex import transforms as T

# 定义训练和验证时的transforms
# API说明：https://github.com/PaddlePaddle/PaddleX/blob/develop/docs/apis/transforms/transforms.md
train_transforms = T.Compose(
    [
        T.MixupImage(mixup_epoch=-1),
        # T.RandomDistort(),
        # T.RandomExpand(im_padding_value=[123.675, 116.28, 103.53]),
        # T.RandomCrop(),
        T.RandomHorizontalFlip(),
        # T.BatchRandomResize(
        #     target_sizes=[192, 224, 256, 288, 320, 352, 384, 416, 448, 480, 512],
        #     interp="RANDOM",
        # ),
        T.Resize(target_size=320, interp="CUBIC"),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

eval_transforms = T.Compose(
    [
        T.Resize(target_size=320, interp="CUBIC"),
        T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

# 定义训练和验证所用的数据集
# API说明：https://github.com/PaddlePaddle/PaddleX/blob/develop/docs/apis/datasets.md
# train_dataset = pdx.datasets.VOCDetection(
#     data_dir="insect_det",
#     file_list="insect_det/train_list.txt",
#     label_list="insect_det/labels.txt",
#     transforms=train_transforms,
#     shuffle=True,
# )
train_dataset = pdx.datasets.VOCDetection(
    data_dir="/home/aistudio/data/data124424/",
    file_list="/home/aistudio/data/data124424/train_list.txt",
    label_list="/home/aistudio/data/data124424/labels.txt",
    transforms=train_transforms,
    shuffle=True,
    num_workers=8,
)

eval_dataset = pdx.datasets.VOCDetection(
    data_dir="/home/aistudio/data/data124424",
    file_list="/home/aistudio/data/data124424/val_list.txt",
    label_list="/home/aistudio/data/data124424/labels.txt",
    transforms=eval_transforms,
    shuffle=False,
    num_workers=8,
)

# 初始化模型，并进行训练
# 可使用VisualDL查看训练指标，参考https://github.com/PaddlePaddle/PaddleX/blob/develop/docs/visualdl.md
num_classes = len(train_dataset.labels)
model_name = "PPYOLOv2"
# model = pdx.det.PPYOLOTiny(num_classes=num_classes)
# model = pdx.det.PicoDet(num_classes=num_classes)
# model = pdx.det.YOLOv3(num_classes=num_classes)
model = eval(f"pdx.det.{model_name}")(num_classes=num_classes)


# API说明：https://github.com/PaddlePaddle/PaddleX/blob/develop/docs/apis/models/detection.md
# 各参数介绍与调整说明：https://github.com/PaddlePaddle/PaddleX/blob/develop/docs/parameters.md
bs = {
    "PPYOLOv2": 64,
    "YOLOv3": 128,
    "PPYOLOTiny": 128,
}
model.train(
    num_epochs=550,
    train_dataset=train_dataset,
    log_interval_steps=1,
    train_batch_size=bs[model_name],
    eval_dataset=eval_dataset,
    pretrain_weights="COCO",
    learning_rate=0.005,
    warmup_steps=100,
    warmup_start_lr=0.00001,
    lr_decay_epochs=[130, 540],
    lr_decay_gamma=0.5,
    save_interval_epochs=10,
    save_dir=f"output/{model_name}",
    use_vdl=True,
)
