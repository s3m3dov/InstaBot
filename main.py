import os, random
from time import sleep
from bot import acc_obj_all, acc_obj_01, personal, professional1, igbot_01, igbot_02, ortak1, ortak2
from modules.accs import flw_unf
#Actions & Tasks
if __name__ == '__main__':
    acc_obj_01[0].login()
    acc_obj_01[1].login()
    for _ in flw_unf['user']:
        acc_obj_01[0].follow(_)
        acc_obj_01[1].follow(_)
    for _ in flw_unf['org']:
        acc_obj_01[0].follow(_)
        acc_obj_01[1].follow(_)
    sleep(300)
    for _ in flw_unf['user']:
        acc_obj_01[0].unfollow_user(_)
        acc_obj_01[1].unfollow_user(_)
    for _ in flw_unf['org']:
        acc_obj_01[0].unfollow_org(_)
        acc_obj_01[1].unfollow_org(_)
    print('Session finished!\n\n')