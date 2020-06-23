import sys
path = "/home/s1810235/part_time/PtNafion/"
sys.path.insert(0, path)
from plot import *
from opt_GMM_2 import *
import numpy as np
import os 
import time

# dir_list = os.listdir(path) 
# print(dir_list)

def diff_t(p,v,t1,t2,task):
    sub_path = path + p +"/" 
    count = 0
    for feature in os.listdir(sub_path):
        if not feature.endswith(".DS_Store"):
            if(task=="task1"):
                Pt1 = np.(np.loadtxt(sub_path+ str(feature)+"/" + t1 + v + "_" + str(feature)+".txt"))
                Pt2 = np.(np.loadtxt(sub_path+ str(feature)+"/" + t2 + v + "_" + str(feature)+".txt"))
                Pt1_t2 = np.subtract(Pt1,Pt2)
                print(Pt1_t2)
                os.makedirs(path + "image/task1/" + "diff_t",exist_ok=True)
                plot_density(Pt1_t2,path + "image/task1/" + "diff_t/" + "{Params}_{feature1}____{feature2}".format(Params=str(p + v + feature),feature1 = str(t1),feature2 = str(t2)),"{Params}_{feature1}____{feature2}".format(Params=str(p + v + feature),feature1 = str(t1),feature2 = str(t2),cmap_name="bwr", vmin=None, vmax=None))
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print(result, end="", flush=True)
                print("\r", end="", flush=True)
                
                
                os.makedirs(path + "feature/task1/" + "diff_t" ,exist_ok=True)
                np.savetxt(path + "feature/task1/" + "diff_t/" + "{Params}_{feature1}____{feature2}.txt".format(Params=str(p + v + feature),feature1 = str(t1),feature2 = str(t2)),Pt1_t2,delimiter="  ")
            else:
                # count +=1 
                Pt1 = np.ravel(np.loadtxt(sub_path+ str(feature)+"/" + t1 + v + "_" + str(feature)+".txt"))
                Pt2 = np.ravel(np.loadtxt(sub_path+ str(feature)+"/" + t2 + v + "_" + str(feature)+".txt"))
                ######task5_section3######
                min_x = np.min(Pt1) ######x tmp[0],y=temp[1]
                max_x = np.max(Pt1)
                min_y = np.min(Pt2) ######x tmp[0],y=temp[1]
                max_y = np.max(Pt2)
                start = time.time()
                os.makedirs(path + "image/task5/joint_diff/",exist_ok=True)
                print(feature)
                print("processing.........")
                joint_plot_fill(Pt1, Pt2, "{}_{}_{}_{}".format(feature,p,t1,v), "{}_{}_{}_{}".format(feature,p,t2,v), path + "image/task5/joint_diff/{}___{}.pdf".format("{}_{}_{}_{}".format(feature,p,t1,v), "{}_{}_{}_{}".format(feature,p,t2,v)) , min_x ,max_x,min_y,max_y )
                print("finish............" + "Time take:{}".format(time.time()-start)+"to run"+"file num:{}".format(count)) 
                ######task5######
                
                
def diff_p(t,v,p1,p2):
    sub_path_p1 = path + p1 + "/"
    sub_path_p2 = path + p2 + "/"
    
    for feature in os.listdir(sub_path_p1):
        if not feature.endswith(".DS_Store"):
            if(task=="task1")
                Pp1 = np.(np.loadtxt(sub_path_p1 + str(feature) + "/" + t + v + "_" + str(feature)+ ".txt"))
                Pp2 = np.(np.loadtxt(sub_path_p2 + str(feature) + "/" + t + v + "_" + str(feature)+ ".txt"))
                Pp2_p1 = np.subtract(Pp2,Pp1)
                os.makedirs(path + "image/task1/" + "diff_p",exist_ok=True)
                plot_density(Pp2_p1,path + "image/task1/" + "diff_p/"+"{Param}_{feature1}____{feature2}".format(Param = str(t + v + feature),feature1 = str(p1),feature2 = str(p2)),"{Param}_{feature1}____{feature2}".format(Param = str(t + v + feature),feature1 = str(p1),feature2 = str(p2)),cmap_name="bwr", vmin=None, vmax=None)
                os.makedirs(path + "feature/task1/" + "diff_p",exist_ok=True)
                np.savetxt(path + "feature/task1/" + "diff_p/"+"{Param}_{feature1}____{feature2}.txt".format(Param = str(t + v + feature),feature1 = str(p1),feature2 = str(p2)),Pp2_p1,delimiter="  ")
                ######task5_section3######
            else:
                Pp1 = np.ravel(np.loadtxt(sub_path_p1 + str(feature) + "/" + t + v + "_" + str(feature)+ ".txt"))
                Pp2 = np.ravel(np.loadtxt(sub_path_p2 + str(feature) + "/" + t + v + "_" + str(feature)+ ".txt"))
                min_x = np.min(Pp1) ######x tmp[0],y=temp[1]
                max_x = np.max(Pp1)
                min_y = np.min(Pp2) ######x tmp[0],y=temp[1]
                max_y = np.max(Pp2)
                start = time.time()
                os.makedirs(path + "image/task5/joint_diff/",exist_ok=True)
                print("processing.........")
                joint_plot_fill(Pp1, Pp2, "{}_{}_{}_{}".format(feature,p1,t,v), "{}_{}_{}_{}".format(feature,p2,t,v), path + "image/task5/joint_diff/{}___{}.pdf".format("{}_{}_{}_{}".format(feature,p1,t,v), "{}_{}_{}_{}".format(feature,p2,t,v)) , min_x ,max_x,min_y,max_y )
                print("finish............" + "Time take:{}".format(time.time()-start)+"to run"+"file num:{}".format(count))

def diff_v(t,p,v1,v2,task):
    sub_path = path + p + "/"
    count = 0

    for feature in os.listdir(sub_path):
        if not feature.endswith(".DS_Store"):
            if(task=="task1"):
                Pv04 = np.(np.loadtxt(sub_path + str(feature) + "/" + t + v1 + "_" + str(feature)+ ".txt"))
                Pv10 = np.(np.loadtxt(sub_path + str(feature) + "/" + t + v2 + "_" + str(feature)+ ".txt"))
                Pv04_v10 = np.subtract(Pv04,Pv10)
                os.makedirs(path +"image/task1/" + "diff_v",exist_ok=True)
                plot_density(Pv04_v10,path + "image/task1/" + "diff_v/"+"{Param}_{feature1}___{feature2}".format(Param = str(t + p + feature),feature1 = str(v1),feature2 = str(v2)),"{Param}_{feature1}_{feature2}".format(Param = str(t + p + feature),feature1 = str(v1),feature2 = str(v2)),cmap_name="bwr", vmin=None, vmax=None)
                os.makedirs(path +"feature/task1/" + "diff_v",exist_ok=True)
                np.savetxt(path + "feature/task1/" + "diff_v/"+"{Param}_{feature1}___{feature2}.txt".format(Param = str(t + p + feature),feature1 = str(v1),feature2 = str(v2)),Pv04_v10,delimiter="  ")
                
            else:
                ######task5_section3######
                Pv04 = np.ravel(np.loadtxt(sub_path + str(feature) + "/" + t + v1 + "_" + str(feature)+ ".txt"))
                Pv10 = np.ravel(np.loadtxt(sub_path + str(feature) + "/" + t + v2 + "_" + str(feature)+ ".txt"))
                min_x = np.min(Pv04) ######x tmp[0],y=temp[1]
                max_x = np.max(Pv04)
                min_y = np.min(Pv10) ######x tmp[0],y=temp[1]
                max_y = np.max(Pv10)
                os.makedirs(path + "image/task5/joint_diff/",exist_ok=True)
                start = time.time()
                print("processing.........")
                joint_plot_fill(Pv04, Pv10, "{}_{}_{}_{}".format(feature,p,t,v1), "{}_{}_{}_{}".format(feature,p,t,v2), path + "image/task5/joint_diff/{}___{}.pdf".format("{}_{}_{}_{}".format(feature,p,t,v1), "{}_{}_{}_{}".format(feature,p,t,v2)) , min_x ,max_x,min_y,max_y )
                print("finish............" + "Time take:{}".format(time.time()-start)+"to run"+"file num:{}".format(count))
                ######task5######
            

    

def main():
    # # #Different of parameter T
    diff_t("CCM-Nafion","1V","Fresh","ADT5k","task1")
    diff_t("CCM-Nafion","04V","Fresh","ADT5k","task1")
    diff_t("CCM-Nafion","1V","Fresh","ADT15k","task1")
    diff_t("CCM-Nafion","04V","Fresh","ADT15k","task1")
    diff_t("CCM-Nafion","1V","ADT5k","ADT15k","task1")
    diff_t("CCM-Nafion","04V","ADT5k","ADT15k","task1")

    diff_t("CCMcenter","1V","Fresh","ADT5k","task1")
    diff_t("CCMcenter","04V","Fresh","ADT5k","task1")
    diff_t("CCMcenter","1V","Fresh","ADT15k","task1")
    diff_t("CCMcenter","04V","Fresh","ADT15k","task1")
    diff_t("CCMcenter","1V","ADT5k","ADT15k","task1")
    diff_t("CCMcenter","04V","ADT5k","ADT15k","task1")

    #Different of parameter p
    diff_p("ADT5k","1V","CCM-Nafion","CCMcenter","task1")
    diff_p("ADT15k","1V","CCM-Nafion","CCMcenter","task1")
    diff_p("Fresh","1V","CCM-Nafion","CCMcenter","task1")
    diff_p("ADT5k","04V","CCM-Nafion","CCMcenter","task1")
    diff_p("ADT15k","04V","CCM-Nafion","CCMcenter","task1")
    diff_p("Fresh","04V","CCM-Nafion","CCMcenter","task1")
    #Different of paremeter V

    diff_v("ADT5k","CCM-Nafion","04V","1V","task1")
    diff_v("ADT15k","CCM-Nafion","04V","1V","task1")
    diff_v("Fresh","CCM-Nafion","04V","1V","task1")
    diff_v("ADT5k","CCMcenter","04V","1V","task1")
    diff_v("ADT15k","CCMcenter","04V","1V","task1")
    diff_v("Fresh","CCMcenter","04V","1V","task1")







if __name__ == "__main__":main()