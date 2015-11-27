import utils
import preproc
import point_cloud
import action

def transform_files(in_path,out_path,transform):
    utils.make_dir(out_path)
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

if __name__ == "__main__":
    binary_path="../raw/"
    raw_path="../raw_actions/"
    cloud_path="../cloud_actions/"
    #transform_files(binary_path,raw_path,binary_to_raw)
    transform_files(raw_path,cloud_path,raw_to_pcloud)