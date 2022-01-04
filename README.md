paddlex --export_inference --model_dir=./output/shoe/best_model/ --save_dir=./inference_model

paddle2onnx --model_dir ./inference_model/inference_model --model_filename model.pdmodel --params_filename model.pdiparams --save_file ./onnx/shoe.onnx --opset_version 11 --enable_onnx_checker True


hub convert --model_dir inference_model/inference_model \
            --module_name shoe \
            --module_version 1.0.0 \
            --output_dir hub_serving


export FLASK_APP=app
flask run
