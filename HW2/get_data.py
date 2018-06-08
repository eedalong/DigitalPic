#import httplib
import json
import urllib
import hashlib
import requests
import base64
import time
import urllib2

def genSignString(quest,app_key):
    uri_str = ''
    for key in sorted(quest.keys()):
        if quest[key] == '':
            continue
        uri_str += "%s=%s&" % (key, urllib.quote(str(quest[key]), safe = ''))
    sign_str = uri_str + 'app_key=' + app_key

    hash_md5 = hashlib.md5(sign_str.encode('utf-8'))
    return hash_md5.hexdigest().upper()


def invoke(quest):
    url = 'https://api.ai.qq.com/fcgi-bin/ptu/ptu_facecosmetic';
    url_data = urllib.urlencode(quest);
    req = urllib2.Request(url,url_data);
    rsp = urllib2.urlopen(req);
    str_rsp = rsp.read();
    dict_rsp = json.loads(str_rsp);
    #print(dict_rsp);
    return dict_rsp;
def get_base64code(image_path):
    with open(image_path,'rb') as  imageFile:
        code =  base64.b64encode(imageFile.read());
        return str(code);
def GetData(image_path,save_path = ''):
    print('dalong log L: into GetData function');
    print('dalong log : check image path {}'.format(image_path));
    image_code =get_base64code(image_path);
    cosmetic = 10;
    app_id = 1106900434;
    app_key = 'UUMP15CWMoF2J60b';
    quest ={};
    quest['cosmetic'] = int(cosmetic);
    quest['time_stamp'] = int(time.time());
    quest['nonce_str'] = int(time.time());
    quest['app_id'] = app_id;
    quest['image'] = image_code;
    quest['sign'] =  genSignString(quest,app_key);
    #print(quest['sign']);
    response_json = invoke(quest);
    print(response_json);
    if response_json[u'ret'] == 0:
        print('successssssssssssssssssssss\n');
        if save_path == '':
            return response_json[u'data'][u'image'];
        image = base64.b64decode(response_json[u'data'][u'image']);
        tmp_file = open(save_path,'wb');
        tmp_file.write(image);
        tmp_file.close();
        return 1;

	print('Faillllllllll');
    return 0;
def main(image_path = '',save_path = '' ):
    image_path = './demo_input.jpg';
    save_path = './result.jpg';
    GetData(image_path,save_path);
    return ;
if __name__ == '__main__':
    main();
