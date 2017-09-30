"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import data_processing as dp
import matplotlib.patches as mpatches
import ast

def curve(input_list,title,statistics):	
    output_list=[]

    ##set subplot position 
    rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
    rect_table = [0.1, 0.2 ,0.8, 0.8]

    ##curve
    curve = plt.axes(rect_curve)
    x = np.linspace(0, len(input_list),len(input_list))
    with plt.style.context('fivethirtyeight'):
        line=curve.plot(x,input_list)	
        plt.setp(line, linewidth=2)
    curve.axes.set_xlabel("sampling")
    curve.axes.set_ylabel("different with exhausted method")
    curve.axes.set_title(title)
    plt.ylim([0,40])
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 20}
    plt.rc('font',**font)

    #table
    axTable = plt.axes(rect_table, frameon =False)
    axTable.axes.get_xaxis().set_visible(False)
    axTable.axes.get_yaxis().set_visible(False)

    table_columns = ('Mean', 'Standard Deviation')
    cell_text=statistics
        
    table_size=axTable.table(cellText=statistics, loc='bottom',
    	colLabels=table_columns)

    ## set table size and font
    table_size.set_fontsize(40)
    table_size.scale(1.2,3)


    plt.show()
def multicurve(input_list,title,statistics):	
    output_list=[]

    ##set subplot position 
    rect_curve = [0.1, 0.3, 0.8, 0.6]#left,bottom,width,height
    rect_table = [0.15, 0.2 ,0.8, 0.8]

    legeng_label=['0Mbit','100Mbit','500Mbit']
    ##curve
    curve = plt.axes(rect_curve)
    for i in range(0,len(input_list)):
        x = np.linspace(0, len(input_list[i]),len(input_list[i]))
        with plt.style.context('fivethirtyeight'):
            line=curve.plot(x,input_list[i])#,label=legeng_label[i])	
            plt.setp(line, linewidth=2)
    
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 20}
    plt.rc('font',**font)
    
    curve.axes.set_xlabel("sampling")
    curve.axes.set_ylabel("different of weight")
    curve.axes.set_title(title)


    #table
    axTable = plt.axes(rect_table, frameon =False)
    axTable.axes.get_xaxis().set_visible(False)
    axTable.axes.get_yaxis().set_visible(False)

    table_rows=('select','exhausted','different of weight')
    table_columns = ('Mean', 'Standard_deviation')
    cell_text=statistics
        
    table_size=axTable.table(cellText=statistics, loc='bottom',
        colLabels=table_columns,rowLabels=table_rows)

    ## set table size and font
    table_size.set_fontsize(20)
    table_size.scale(1,1)

    ##set legend position
    curve.legend(bbox_to_anchor=(1.05, 1.05))
    
    plt.show()


if __name__=="__main__":
    ## main code for multicurve
    print "draw.py"
    title  = "10 node,weight 0~20, deadline = 128+c+0~500,arrival = 0~1000"
    fileRead = open("1.txt",'r')
    fileData = []
    for line in fileRead:
    	fileData.append(line)
    select = ast.literal_eval(fileData[0])
    exhausted = ast.literal_eval(fileData[1])

    diffdata = ast.literal_eval(fileData[2])
    print diffdata

    #select = [45.0, 52.0, 55.0, 38.0, 28.0, 59.0, 33.0, 52.0, 55.0, 45.0, 43.0, 43.0, 27.0, 53.0, 50.0, 42.0, 46.0, 50.0, 43.0, 48.0, 47.0, 42.0, 56.0, 45.0, 46.0, 41.0, 44.0, 45.0, 53.0, 52.0, 41.0, 54.0, 67.0, 51.0, 51.0, 66.0, 46.0, 54.0, 45.0, 38.0, 59.0, 65.0, 71.0, 27.0, 46.0, 43.0, 53.0, 47.0, 42.0, 40.0, 36.0, 39.0, 44.0, 32.0, 45.0, 67.0, 53.0, 36.0, 52.0, 44.0, 39.0, 53.0, 44.0, 39.0, 36.0, 68.0, 44.0, 50.0, 40.0, 51.0, 48.0, 74.0, 49.0, 44.0, 52.0, 55.0, 50.0, 37.0, 46.0, 35.0, 63.0, 44.0, 50.0, 29.0, 56.0, 45.0, 36.0, 30.0, 48.0, 41.0, 55.0, 45.0, 49.0, 34.0, 55.0, 50.0, 37.0, 43.0, 50.0, 28.0]
    #exhausted = [45.0, 52.0, 55.0, 42.0, 28.0, 59.0, 38.0, 61.0, 58.0, 45.0, 47.0, 43.0, 27.0, 66.0, 52.0, 42.0, 48.0, 50.0, 43.0, 48.0, 47.0, 42.0, 56.0, 53.0, 47.0, 41.0, 51.0, 51.0, 53.0, 52.0, 49.0, 54.0, 67.0, 54.0, 51.0, 66.0, 48.0, 57.0, 45.0, 43.0, 59.0, 65.0, 71.0, 36.0, 46.0, 43.0, 57.0, 47.0, 55.0, 42.0, 36.0, 43.0, 44.0, 32.0, 46.0, 67.0, 53.0, 45.0, 52.0, 44.0, 39.0, 53.0, 47.0, 39.0, 50.0, 68.0, 50.0, 63.0, 50.0, 56.0, 53.0, 74.0, 49.0, 47.0, 57.0, 58.0, 51.0, 37.0, 46.0, 42.0, 69.0, 44.0, 58.0, 31.0, 56.0, 46.0, 40.0, 32.0, 52.0, 41.0, 55.0, 45.0, 51.0, 34.0, 55.0, 54.0, 42.0, 45.0, 52.0, 32.0]
    #diffdata = [0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 5.0, 9.0, 3.0, 0.0, 4.0, 0.0, 0.0, 13.0, 2.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 8.0, 1.0, 0.0, 7.0, 6.0, 0.0, 0.0, 8.0, 0.0, 0.0, 3.0, 0.0, 0.0, 2.0, 3.0, 0.0, 5.0, 0.0, 0.0, 0.0, 9.0, 0.0, 0.0, 4.0, 0.0, 13.0, 2.0, 0.0, 4.0, 0.0, 0.0, 1.0, 0.0, 0.0, 9.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 14.0, 0.0, 6.0, 13.0, 10.0, 5.0, 5.0, 0.0, 0.0, 3.0, 5.0, 3.0, 1.0, 0.0, 0.0, 7.0, 6.0, 0.0, 8.0, 2.0, 0.0, 1.0, 4.0, 2.0, 4.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 4.0, 5.0, 2.0, 2.0, 4.0]
  

    diffSt=dp.compute_statistics(diffdata)    
    exhaustedSt = dp.compute_statistics(exhausted)
    selectSt = dp.compute_statistics(select)

    curve(diffdata,title,[diffSt])
    #multicurve([select,exhausted,diffdata],title,[selectSt,exhaustedSt,diffSt])
