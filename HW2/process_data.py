import get_data
import skimage.io as io
import time
import os
import cv2
read_root= '/home/yuanxl/photo';
save_root = '/home/yuanxl/photos_dalong'
file_path = '/home/yuanxl/photo/imgs';
input_file =  open(file_path);

index = 0;
for img_index in input_file.readlines():
    img_index = img_index[:-1];
    save_path = os.path.join(save_root,img_index);
    read_path = os.path.join(read_root,img_index);
    #get_data.main(read_path,save_path);
    get_data.GetData(read_path,save_path);
    print('dalong log : check index now  = {}'.format(index));
    index = index + 1;
input_file.close();
print('dalong log : demo finished ');




