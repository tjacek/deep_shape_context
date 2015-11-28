import utils
import preproc
import point_cloud
import action
import time_series as td

def transform_files(in_path,out_path,transform,dirs=False):
    utils.make_dir(out_path)
    if(dirs):
        names=utils.get_dirs(in_path)
    else:
        names=utils.get_files(in_path)
    for name in names:
        full_in_path=in_path+name
        full_out_path=out_path+name
        transform(full_in_path,full_out_path)

def binary_to_raw(in_path,out_path):
    raw_action=preproc.read_binary(in_path)
    out_path=out_path.replace(".bin",".raw")
    print(out_path)
    utils.save_object(raw_action,out_path)

def raw_to_pcloud(in_path,out_path):
    pcloud=action.make_action(in_path)
    pcloud.standarize()
    out_path=out_path.replace(".raw",".cloud")
    print(out_path)
    utils.save_object(pcloud,out_path)

def pcloud_to_img(in_path,out_path):
    pcloud_action=utils.read_object(in_path)
    out_path=out_path.replace(".cloud",".img/")
    print(out_path)
    pcloud_action.save_projection(out_path)

def img_to_pca(in_path,out_path):
    action=td.read_im_action(in_path+"/")
    out_path=out_path.replace(".img","")
    pca=action.to_pca()
    eigen=td.to_time_serie(pca)
    img=td.to_img(eigen)
    utils.save_img(out_path,img)

if __name__ == "__main__":
    binary_path="../raw/"
    raw_path="../raw_actions/"
    cloud_path="../cloud_actions/"
    img_path="../img_actions/"
    pca_path="../pca_actions/"
    print("ok")
    transform_files(img_path,pca_path,img_to_pca,True)
    #transform_files(binary_path,raw_path,binary_to_raw)
    #transform_files(raw_path,cloud_path,raw_to_pcloud)
    #transform_files(cloud_path,img_path,pcloud_to_img)