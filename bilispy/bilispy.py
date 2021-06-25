# BiliSPY Beta 1.0f
import requests,random,time,codecs,os

def get_avid(bvid):#Get Avid form Bvid (Using Bilibili API)
    bvid_url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + bvid
    content_bvid_url = codecs.decode(requests.get(bvid_url).content, "utf-8").split("\"")
    if int(content_bvid_url[2][1:-1]) != 0:
        print('Could not find a video matching your BV ID.')
        return -1
    return int(content_bvid_url[16][1:-1])

def get_avid_data(avid):#Get Video Info from Avid (Using Bilibili API)
    vdata_url = 'https://api.bilibili.com/archive_stat/stat?aid=' + avid
    vdatar = codecs.decode(requests.get(vdata_url).content, "utf-8").split("\"")
    vdata = [vdatar[14][1:-1],vdatar[16][1:-1],vdatar[18][1:-1],vdatar[20][1:-1],vdatar[22][1:-1],vdatar[24][1:-1],vdatar[30][1:-1]]
    #vdata = [view,danmu,com,fav,coin,share,like]
    return vdata

def create_path(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return 1
    return 0
    
while(1):
    bv = input('Please enter your BV ID number:')
    av = get_avid(bv)
    if av == -1:    continue
    current_vdata = get_avid_data(str(av))
    print('------\nSuccessfully acquired your video data. \n------\nBV:%s,Avid:%s.\nTotal Views:%s,DanmuCounts:%s,Comments:%s.\nLikes:%s,coins:%s,Favourites:%s,Shares:%s.\n------\nHow many times would you like to reload your video data?' % (bv,av,current_vdata[0],current_vdata[1],current_vdata[2],current_vdata[6],current_vdata[4],current_vdata[3],current_vdata[5]))
    repeat_times = input ('Repeat times you want to:')
    interval_times = input ('Intervals between two acquirys(seconds):')
    attempt_time = 0
    file_path = os.getcwd() + '\\Results\\'+ bv + '\\'
    create_path(file_path)
    file_name = file_path + str(int(time.time())) + '.txt'
    with open(file_name,'a') as file_object:
        file_object.write('Intervals:【 %s 】Seconds---\n' % (interval_times))
    while(int(repeat_times) > 0):
        attempt_time = attempt_time + 1
        current_vdata = get_avid_data(str(av))
        print('This is %s/%s attempts.\n------\nBV:%s,Avid:%s.\nTotal Views:%s,DanmuCounts:%s,Comments:%s.\nLikes:%s,coins:%s,Favourites:%s,Shares:%s.\n------\n' % (attempt_time,repeat_times,bv,av,current_vdata[0],current_vdata[1],current_vdata[2],current_vdata[6],current_vdata[4],current_vdata[3],current_vdata[5]))
        write_data = (str(attempt_time) +'/'+ str(repeat_times) +' '+ bv +' '+ str(current_vdata[0]) +' '+ str(current_vdata[1]) +' '+ str(current_vdata[2]) +' '+ str(current_vdata[6]) +' '+ str(current_vdata[4]) +' '+ str(current_vdata[3]) +' '+ str(current_vdata[5]) +'\n')
        with open(file_name,'a') as file_object:    file_object.write(write_data)
        time.sleep(int(interval_times))
        repeat_times = int(repeat_times) - 1
    print('------\nSuccessfully grabbed all of your video data!\n------\nAll files saved to:%s\n Wanna try another time?' % (file_name))
