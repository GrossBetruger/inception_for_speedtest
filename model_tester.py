import os
from predict import predict
from shutil import copy
from multiprocessing import Pool
from functools import wraps

def max_args(model, image_path):
    return list(sorted([pred.split(" ")
                   for pred in
                   predict(model, image_path).split("\n")],
                   key=lambda x : x[-1]))[-1]


def to_path(pred):
    return "_".join(pred[0:-1])


def job_decorator(args):
    order_by_prediction(*args)


def order_by_prediction(model, img_path, save_path):
    predicted = max_args(model, img_path)
    dst_path = to_path(predicted)
    copy_to_path = os.path.join(save_path, dst_path)
    if not os.path.isdir(copy_to_path):
        os.makedirs(copy_to_path)
    copy(img_path, os.path.join(save_path, copy_to_path))
    print "classified and copied image\n new_path {}".format(os.path.join(copy_to_path, os.path.basename(img_path)))


if __name__ == "__main__":
    save_path = "/home/oren/ClassifierTest"
    dump_path = "/home/oren/s3/dump2"
    model, img_path = "models/11_classes_double_dataset/", "/home/oren/s3/dump2/04CE66A48046E2C3517D6290A6F78AEF-0.989509-hot-middle.png"

    img_paths = [os.path.join(dump_path, fpath) for fpath in os.listdir(dump_path)]
    jobs = [(model, imgp, save_path) for imgp in img_paths]
    order_by_prediction(model, img_path, save_path)
    prediction_pool = Pool(8)
    prediction_pool.map(job_decorator, jobs)
