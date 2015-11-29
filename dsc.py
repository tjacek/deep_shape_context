import utils
import preproc
import point_cloud
import action
import time_series as td
import projections as pr

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

def img_to_final(in_path,out_path):
    print(in_path+"/")
    final=td.read_im_action(in_path+"/")
    out_path=out_path.replace(".img",".final")
    print(out_path)
    utils.save_object(final,out_path)

def final_to_pca(in_path,out_path):
    #action=td.read_im_action(in_path+"/")
    action=utils.read_object(in_path)
    out_path=out_path.replace(".final",".pca")
    pca=action.to_pca()
    eigen=td.to_time_serie(pca)
    img=td.to_img(eigen)
    utils.save_img(out_path,img)

def smooth_imgs(in_path,out_path):
    action=pr.read_img_action(in_path+"/")
    action.smooth()
    print(out_path)
    action.save(out_path)

def diff_imgs(in_path,out_path):
    action=pr.read_img_action(in_path+"/")
    diff_action=action.diff()
    print(out_path)
    diff_action.save(out_path)

if __name__ == "__main__":
    binary_path="../raw/"
    raw_path="../raw_actions/"
    cloud_path="../cloud_actions/"
    img_path="../hands/img_actions/"
    final_path="../hands/final_actions/"
    pca_path="../hands/pca/"
    smooth_path="../hands/smooth_actions/"
    diff_path="../hands/diff_actions/"
    print("ok")
    #transform_files(img_path,pca_path,img_to_pca,True)
    #transform_files(binary_path,raw_path,binary_to_raw)
    #transform_files(raw_path,cloud_path,raw_to_pcloud)
    #transform_files(cloud_path,img_path,pcloud_to_img)
    #transform_files(diff_path,final_path,img_to_final,True)
    transform_files(final_path,pca_path,final_to_pca)
    #transform_files(img_path,smooth_path,smooth_imgs,True)
    #transform_files(smooth_path,diff_path,diff_imgs,True)