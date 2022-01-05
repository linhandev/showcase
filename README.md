# run server
export FLASK_APP=app
flask run

paddlex --export_inference --model_dir=./model/ppyolo-tiny --save_dir=./inference

<!-- paddle2onnx --model_dir ./inference_model/inference_model --model_filename model.pdmodel --params_filename model.pdiparams --save_file ./onnx/shoe.onnx --opset_version 11 --enable_onnx_checker True -->


<!-- hub convert --model_dir inference_model/inference_model \
            --module_name shoe \
            --module_version 1.0.0 \
            --output_dir hub_serving -->


# capture image
sudo pacman -S sox

labelImg data/pascal/JPEGImages data/pascal/labels.txt data/pascal/Annotations

# train
python prep/list.py
cd data/pascal
zip -r shoe_$(date +"%y-%m-%d-%H-%M").zip *
cd ../../
ls -l ./data/pascal/Annotations/| wc -l ; ls -l ./data/pascal/JPEGImages/ | wc -l


# download imagenet
python ./downloader.py -data_root ./imgnet  -use_class_list True  -class_list n02882894 n03472535 n03865949 n04120489 n04199027 n04200000 n04252331 n04546081 -images_per_class 10000

n02767147,baby shoe,507,269
n02882894,bowling shoe,1381,1368
n03472535,gym shoe,283,158
n03865949,overshoe,1153,100
n04120489,running shoe,1546,1113
n04199027,shoe,1265,705
n04200000,shoe,975,642
n04252331,snowshoe,1141,731
n04546081,walking shoe,228,172


transfer(){ if [ $# -eq 0 ];then echo "No arguments specified.\nUsage:\n  transfer <file|directory>\n  ... | transfer <file_name>">&2;return 1;fi;if tty -s;then file="$1";file_name=$(basename "$file");if [ ! -e "$file" ];then echo "$file: No such file or directory">&2;return 1;fi;if [ -d "$file" ];then file_name="$file_name.zip" ,;(cd "$file"&&zip -r -q - .)|curl -k --progress-bar --upload-file "-" "https://transfer.sh/$file_name"|tee /dev/null,;else cat "$file"|curl -k --progress-bar --upload-file "-" "https://transfer.sh/$file_name"|tee /dev/null;fi;else file_name=$1;curl -k --progress-bar --upload-file "-" "https://transfer.sh/$file_name"|tee /dev/null;fi;}
