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

def edge_imgs(in_path,out_path):
    action=pr.read_img_action(in_path+"/")
    action.detect_edges()
    print(out_path)
    action.save(out_path)

def skew_imgs(in_path,out_path):
    action=utils.read_object(in_path)
    skew=action.skew()
    skew_ts=td.to_time_serie(skew)
    print(out_path)
    td.visualize(out_path,skew_ts)

def sd_imgs(in_path,out_path):
    action=utils.read_object(in_path)
    sd=action.skew()
    sd_ts=td.to_time_serie(sd)
    print(out_path)
    td.visualize(out_path,sd_ts)

def feat_imgs(in_path,out_path):
    action=utils.read_object(in_path)
    sd=action.features()
    sd_ts=td.to_time_serie(sd)
    print(out_path)
    td.visualize(out_path,sd_ts)

def diff_imgs(in_path,out_path):
    action=pr.read_img_action(in_path+"/")
    diff_action=action.diff()
    print(out_path)
    diff_action.save(out_path)

if __name__ == "__main__":
    binary_path="../raw/"
    raw_path="../raw_actions/"
    cloud_path="../cloud_actions/"
    img_path="../img_actions/"
    #pca_path="../hands/pca/"
    sd_path="../hands/sd/"
    skew_path="../hands/skew/"
    feat_path="../hands/features/"
    smooth_path="../smooth_actions/"
    edge_path="../hands/edge_actions/"
    final_path="../hands/final_actions/"
    diff_path="../hands/diff_actions/"
    #transform_files(binary_path,raw_path,binary_to_raw)
    #transform_files(raw_path,cloud_path,raw_to_pcloud)
    #transform_files(cloud_path,img_path,pcloud_to_img)
    #transform_files(final_path,pca_path,final_to_pca)
    #transform_files(img_path,smooth_path,smooth_imgs,True)
    #transform_files(smooth_path,edge_path,edge_imgs,True)
    #transform_files(edge_path,final_path,img_to_final,True)
    #transform_files(final_path,sd_path,sd_imgs)
    #transform_files(final_path,skew_path,skew_imgs)
    transform_files(final_path,feat_path,feat_imgs)
    #transform_files(img_path,diff_path,diff_imgs,True)
    #transform_files(diff_path,final_path,img_to_final,True)