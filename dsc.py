import utils
import preproc

def transform_files(in_path,out_path,transform):
    utils.make_dir(out_path)
    names=utils.get_files(in_path)    
    for name in names:
        full_in_path=in_path+name
        full_out_path=out_path+name
        binar_to_raw(full_in_path,full_out_path)

def binar_to_raw(in_path,out_path):
    raw_action=preproc.read_binary(in_path)
    out_path=out_path.replace(".bin",".raw")
    print(out_path)
    utils.save_object(raw_action,out_path)

if __name__ == "__main__":
    in_path="../raw/"
    out_path="../raw_actions/"
    transform_files(in_path,out_path,binar_to_raw)