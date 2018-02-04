from subprocess import Popen, PIPE
from sys import argv
import os


PWD = os.path.abspath(__file__).split(os.path.sep)[1:-1]

TENSOR_FLOW_PATH_DIRS = ["tensorflow", "tensorflow", "examples", "label_image", "label_image.py"]

TENSOR_FLOW_ABS_PATH_DIRS = [os.sep] + PWD + TENSOR_FLOW_PATH_DIRS

TENSOR_FLOW_PATH = os.path.abspath(os.path.join(*TENSOR_FLOW_ABS_PATH_DIRS))

PREDICT_CMD = "python {0} --graph={1}/output_graph.pb " \
              "--labels={1}/output_labels.txt --input_layer=Mul --output_layer=final_result --input_mean=128 " \
              "--input_std=128 --image={2} "


def predict(model_path, image_path):
    proc = Popen(PREDICT_CMD.format(TENSOR_FLOW_PATH, model_path, image_path),
                 shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    return proc.communicate()[0] or proc.communicate()[1]


if __name__ == "__main__":
    try:
        model = argv[1]
        image = argv[2]
    except IndexError:
        print "USAGE: predict.py model_path, image_path"
        quit()
    print predict(model, image)