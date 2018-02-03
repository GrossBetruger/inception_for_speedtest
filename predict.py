from subprocess import Popen, PIPE
from sys import argv


PREDICT_CMD = "python tensorflow/tensorflow/examples/label_image/label_image.py --graph={0}/output_graph.pb " \
              "--labels={0}/output_labels.txt --input_layer=Mul --output_layer=final_result --input_mean=128 " \
              "--input_std=128 --image={1} "


def predict(model_path, image_path):
    proc = Popen(PREDICT_CMD.format(model_path, image_path),
                 shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

    return proc.communicate()[0]


if __name__ == "__main__":
    try:
        model = argv[1]
        image = argv[2]
    except IndexError:
        print "USAGE: predict.py model_path, image_path"
    print predict(model, image)