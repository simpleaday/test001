import re
import linecache
import os
import math
import pandas as pd
from decimal import Decimal

file = open('SWMMgis.inp', 'r')  # 打开文件名称
output = open('SWMMgis_out.inp', 'w')  # 输出文件名称
line_idx = 0
global file2
global START_DATE
global START_TIME
global END_DATE
global END_TIME

# 根据用户的输入选定雨型进行计算
# 雨型：RealTime Chicago SCS1 SCS1A SCS2 SCS3 yiwuHis
with open('inputData.txt', 'r') as inputFile:
    inputData = inputFile.readlines()
    inputData = inputData[1].split()
    NAME = inputData[0]
    DATE = inputData[1]
    timeStart = inputData[2]
    totalTime = int(inputData[3])
    totalPrep = float(inputData[4])  # 降雨量
    rainModel = inputData[5] # 雨型

# 用户选择根据给定的雨型进行模拟计算 //////////////////////////////////////////////////////////
if rainModel == 'RealTime':
    file2 = open('rainfall-TimeS.txt', 'r')  # 打开文件名称
    rainFall_file = 'rainfall-TimeS.txt'

# 使用SCS1雨型进行计算 ///////////////////////////////////////////////////////////////////
elif rainModel == 'SCS1':
    # SCS1雨型计算
    outputFile = open('RainProjectSCS1Data.txt', 'w', encoding='utf-8', newline='' "")  # 存储最后的txt数据
    try:
        timeList = [0, 2.0, 4.0, 6.0, 7.0, 8.0, 8.5, 9.0, 9.5, 9.75, 10.0, 10.5, 11.0, 11.5, 11.75, 12.0, 12.5,
                    13.0, 13.5, 14.0, 16.0, 20.0, 24.0]
        ratioList = [0, 0.035, 0.076, 0.125, 0.156, 0.194, 0.219, 0.254, 0.303, 0.362, 0.515, 0.583, 0.624, 0.654,
                     0.669, 0.682, 0.706, 0.727, 0.748, 0.767, 0.830, 0.926, 1.000]
        valueList = []
        for i in range(len(ratioList)):
            if i == 0:
                valueList.append('0')
            else:
                valueList.append(str(Decimal(str(totalPrep)) * (Decimal(str(ratioList[i])) - Decimal(str(ratioList[i-1])))))
        for i in range(len(timeList)):
            dataWrite = NAME + '  ' + DATE + '  ' + str(timeList[i]) + '    ' + str(valueList[i])
            dataWrite = dataWrite + ('\n')
            outputFile.write(dataWrite)
    finally:
        outputFile.close()
        file2 = open('RainProjectSCS1Data.txt', 'r')
        rainFall_file = 'RainProjectSCS1Data.txt'

# 使用SCS1A雨型进行计算 ///////////////////////////////////////////////////////////////////
elif rainModel == 'SCS1A':
    # SCS1A雨型计算
    outputFile = open('RainProjectSCS1AData.txt', 'w', encoding='utf-8', newline='' "")  # 存储最后的txt数据
    try:
        timeList = [0, 2.0, 4.0, 6.0, 7.0, 8.0, 8.5, 9.0, 9.5, 9.75, 10.0, 10.5, 11.0, 11.5, 11.75, 12.0, 12.5,
                    13.0, 13.5, 14.0, 16.0, 20.0, 24.0]
        ratioList = [0, 0.050, 0.116, 0.206, 0.268, 0.425, 0.480, 0.520, 0.550, 0.564, 0.577, 0.601, 0.624, 0.645,
                     0.655, 0.664, 0.683, 0.701, 0.719, 0.736, 0.800, 0.906, 1.000]
        valueList = []
        for i in range(len(ratioList)):
            if i == 0:
                valueList.append('0')
            else:
                valueList.append(str(Decimal(str(totalPrep)) * (Decimal(str(ratioList[i])) - Decimal(str(ratioList[i-1])))))
        for i in range(len(timeList)):
            dataWrite = NAME + '  ' + DATE + '  ' + str(timeList[i]) + '    ' + str(valueList[i])
            dataWrite = dataWrite + ('\n')
            outputFile.write(dataWrite)
    finally:
        outputFile.close()
        file2 = open('RainProjectSCS1AData.txt', 'r')
        rainFall_file = 'RainProjectSCS1AData.txt'

# 使用SCS2雨型进行计算 ///////////////////////////////////////////////////////////////////
elif rainModel == 'SCS2':
    # SCS2雨型计算
    outputFile = open('RainProjectSCS2Data.txt', 'w', encoding='utf-8', newline='' "")  # 存储最后的txt数据
    try:
        timeList = [0, 2.0, 4.0, 6.0, 7.0, 8.0, 8.5, 9.0, 9.5, 9.75, 10.0, 10.5, 11.0, 11.5, 11.75, 12.0, 12.5,
                    13.0, 13.5, 14.0, 16.0, 20.0, 24.0]
        ratioList = [0, 0.022, 0.048, 0.080, 0.098, 0.120, 0.133, 0.147, 0.163, 0.172, 0.181, 0.204, 0.235, 0.283,
                     0.357, 0.663, 0.735, 0.772, 0.799, 0.820, 0.880, 0.952, 1.000]
        valueList = []
        for i in range(len(ratioList)):
            if i == 0:
                valueList.append('0')
            else:
                valueList.append(str(Decimal(str(totalPrep)) * (Decimal(str(ratioList[i])) - Decimal(str(ratioList[i-1])))))
        for i in range(len(timeList)):
            dataWrite = NAME + '  ' + DATE + '  ' + str(timeList[i]) + '    ' + str(valueList[i])
            dataWrite = dataWrite + ('\n')
            outputFile.write(dataWrite)
    finally:
        outputFile.close()
        file2 = open('RainProjectSCS2Data.txt', 'r')
        rainFall_file = 'RainProjectSCS2Data.txt'

# 使用SCS3雨型进行计算 ///////////////////////////////////////////////////////////////////
elif rainModel == 'SCS3':
    # SCS3雨型计算
    outputFile = open('RainProjectSCS3Data.txt', 'w', encoding='utf-8', newline='' "")  # 存储最后的txt数据
    try:
        timeList = [0, 2.0, 4.0, 6.0, 7.0, 8.0, 8.5, 9.0, 9.5, 9.75, 10.0, 10.5, 11.0, 11.5, 11.75, 12.0, 12.5,
                    13.0, 13.5, 14.0, 16.0, 20.0, 24.0]
        ratioList = [0, 0.020, 0.043, 0.072, 0.089, 0.115, 0.130, 0.148, 0.167, 0.178, 0.189, 0.216, 0.250, 0.298,
                     0.339, 0.500, 0.702, 0.751, 0.785, 0.811, 0.886, 0.957, 1.000]
        valueList = []
        for i in range(len(ratioList)):
            if i == 0:
                valueList.append('0')
            else:
                valueList.append(str(Decimal(str(totalPrep)) * (Decimal(str(ratioList[i])) - Decimal(str(ratioList[i-1])))))
        for i in range(len(timeList)):
            dataWrite = NAME + '  ' + DATE + '  ' + str(timeList[i]) + '    ' + str(valueList[i])
            dataWrite = dataWrite + ('\n')
            outputFile.write(dataWrite)
    finally:
        outputFile.close()
        file2 = open('RainProjectSCS3Data.txt', 'r')
        rainFall_file = 'RainProjectSCS3Data.txt'

# 使用yiwuHis雨型进行计算 ///////////////////////////////////////////////////////////////////
elif rainModel == 'yiwuHis':
    # yiwuHis雨型计算
    outputFile = open('RainProjectyiwuHisData.txt', 'w', encoding='utf-8', newline='' "")  # 存储最后的txt数据
    try:
        timeList = [0, 2.0, 4.0, 6.0, 7.0, 8.0, 8.5, 9.0, 9.5, 9.75, 10.0, 10.5, 11.0, 11.5, 11.75, 12.0, 12.5,
                    13.0, 13.5, 14.0, 16.0, 20.0, 24.0]
        ratioList = [0, 0.020, 0.043, 0.072, 0.110, 0.115, 0.135, 0.148, 0.157, 0.178, 0.189, 0.206, 0.245, 0.278,
                     0.339, 0.400, 0.692, 0.701, 0.705, 0.850, 0.876, 0.927, 1.000]
        valueList = []
        for i in range(len(ratioList)):
            if i == 0:
                valueList.append('0')
            else:
                valueList.append(str(Decimal(str(totalPrep)) * (Decimal(str(ratioList[i])) - Decimal(str(ratioList[i-1])))))
        for i in range(len(timeList)):
            dataWrite = NAME + '  ' + DATE + '  ' + str(timeList[i]) + '    ' + str(valueList[i])
            dataWrite = dataWrite + ('\n')
            outputFile.write(dataWrite)
    finally:
        outputFile.close()
        file2 = open('RainProjectyiwuHisData.txt', 'r')
        rainFall_file = 'RainProjectyiwuHisData.txt'
# 使用芝加哥雨型进行计算 ///////////////////////////////////////////////////////////////////
else :
    # 芝加哥雨型计算
    global P  # 重现期
    totalTime = int(inputData[3]) * 5 # 暂定的总时间
    df = pd.read_excel('P_collect.xlsx')
    outputFile = open('RainProjectChicagoData.txt', 'w', encoding='utf-8', newline='' "")  # 存储最后的txt数据
    try:
        # 查找重现期P
        t_values = df.columns.values
        for i in range(len(t_values)):
            if t_values[i] == totalTime:
                rainfall_values = df.iloc[:, i].values
                index_P = 0
                # 得到重现期P的索引
                for j in range(len(rainfall_values)):
                    if rainfall_values[j] == totalPrep:
                        index_P = j
                    elif j == len(rainfall_values) - 1:  # 查找到最后一个元素
                        if rainfall_values[j] == totalPrep:
                            index_P = j
                        elif rainfall_values[j] != totalPrep:  # 若rainfall处于两个值中间，则选择较大的那个重现期
                            rainfallSort = sorted(rainfall_values)  # 对数组进行排序
                            for k in range(len(rainfallSort)):
                                if totalPrep > rainfallSort[k - 1] and totalPrep < rainfallSort[k]:
                                    rainfall_max = rainfallSort[k]
                                    for l in range(len(rainfall_values)):
                                        if rainfall_values[l] == rainfall_max:
                                            index_P = l
                                elif totalPrep < rainfallSort[0]:
                                    rainfall_min = rainfallSort[0]
                                    for l in range(len(rainfall_values)):
                                        if rainfall_values[l] == rainfall_min:
                                            index_P = l
                                elif totalPrep > rainfallSort[len(rainfallSort) - 1]:
                                    rainfall_max = rainfallSort[len(rainfallSort) - 1]
                                    for l in range(len(rainfall_values)):
                                        if rainfall_values[l] == rainfall_max:
                                            index_P = l

                P_values = df.iloc[:, 0].values
                P = P_values[index_P]  # 得到重现期P

        # 芝加哥雨型计算
        A = 7015.518  # 定义需要的常数
        C = 0.802
        b = 20.951
        c = 0.96
        r = 0.4
        # print(P)
        a = A * (1 + c * math.log(P)) / 166.7

        # 函数计算
        tm = totalTime * r
        t_list = []
        i_list = []
        data_list = []
        final_list = []
        t_listFinal = []
        for i in range(totalTime):  # 将用户输入的t以分钟为间隔排成一列
            t_list.append(i)
        t_list.append(totalTime)
        for t_value in t_list:  # 如果ti＜=tm，则tb=tm-ti; 如果ti＞tm，tb=ti-tm
            if t_value <= tm:
                tb = tm - t_value
                i_tb = a * ((1 - c) * tb / r + b) / (tb / r + b) ** (1 + c)  # 使用对应公式计算i(tb)
                i_list.append(i_tb)
            else:
                ta = t_value - tm
                i_ta = a * ((1 - c) * ta / (1 - r) + b) / (ta / (1 - r) + b) ** (1 + c)  # 使用对应公式计算i(ta)
                i_list.append(i_ta)
        for t_value in i_list:
            data_list.append(t_value * totalPrep / sum(i_list))  # 计算得到第三列数据

        # 将时间以10分钟为间隔组成数组
        t_listFinal.append(timeStart)
        tt = timeStart.split(':')
        for i in range(10, totalTime + 10, 10):
            minute = int(tt[1]) + i
            if minute % 60 != 0:
                time = str(int(tt[0]) + int(minute // 60)) + ':' + str(minute % 60)
            else:
                time = str(int(tt[0]) + int(minute // 60)) + ':00'
            t_listFinal.append(time)
        index = 0
        sumData = 0
        final_list.append(data_list[0])  # 将第一个时刻的数据作为第一个数据
        del data_list[0]
        # 以10分钟为一个间隔对数据求和
        for data in data_list:
            if index < 10:
                sumData += data
                index += 1
                if index == 10:
                    final_list.append(sumData)
            else:
                index = 1
                sumData = data
        # 写入txt文件
        # print(t_listFinal)
        for i in range(len(t_listFinal)):
            dataWrite = NAME + '  ' + DATE + '  ' + t_listFinal[i] + '    ' + str(final_list[i])
            dataWrite = dataWrite + ('\n')
            outputFile.write(dataWrite)
    finally:
        outputFile.close()
        file2 = open('RainProjectChicagoData.txt', 'r')
        rainFall_file = 'RainProjectChicagoData.txt'


global searchObj
try:
    # 跳过[TIMESERIES]前面的部分
    text_line = file.readline()
    line_idx = line_idx + 1  # 记录行号用于定位分析
    while text_line:
        output.writelines(text_line)
        searchObj = re.search(r'\[TIMESERIES\]', text_line)
        if searchObj:
            break
        text_line = file.readline()
        line_idx = line_idx + 1

    # 替换[TIMESERIES]区域数据
    text_line = file.readline()
    line_idx = line_idx + 1  # 记录行号用于定位分析
    flag = 0
    while text_line:
        searchObj = re.search(r'(\d+\s+)(\S+\s+)(\S+\s+)(\d+)', text_line)
        if searchObj:
            flag += 1
            if flag == 1:
                substr = file2.readline()
                symbal = 0
                line_num = 0
                while len(substr) != 0:  #降雨文件中的数据未读取完毕
                    line_num += 1
                    symbal += 1
                    searchObj_rainFall = re.search(r'(\d+\s+)(\S+\s+)(\S+\s+)(\S+)', substr)
                    if symbal == 1:  # 获取起始时间
                        START_DATE = searchObj_rainFall.group(2)
                        START_TIME = searchObj_rainFall.group(3)
                    if searchObj_rainFall == None:
                        endData = linecache.getline(rainFall_file, line_num - 1)  # 获取结束时间
                        endDataSp = endData.split()
                        END_DATE = endDataSp[1]
                        END_TIME = endDataSp[2]
                        break
                    sub_out0 = re.sub(searchObj.group(1), searchObj_rainFall.group(1), searchObj.group(1))
                    sub_out1 = re.sub(searchObj.group(2), searchObj_rainFall.group(2), searchObj.group(2))
                    sub_out2 = re.sub(searchObj.group(3), searchObj_rainFall.group(3), searchObj.group(3))
                    sub_out3 = re.sub(searchObj.group(4), searchObj_rainFall.group(4), searchObj.group(4))
                    text_out = sub_out0 + sub_out1 + sub_out2 + sub_out3 + '\n'  # 降雨文件中取出的后三列与inp文件进行重新拼接
                    output.writelines(text_out)
                    substr = file2.readline()
                if len(substr) == 0:
                    endData = linecache.getline(rainFall_file, line_num)  # 获取结束时间
                    endDataSp = endData.split()
                    END_DATE = endDataSp[1]
                    END_TIME = endDataSp[2]
        else:
            output.writelines(text_line)
        text_line = file.readline()
        line_idx = line_idx + 1

    # 复制[TIMESERIES]后面的部分
    # 跳过[TIMESERIES]前面的部分
    text_line = file.readline()
    line_idx = line_idx + 1  # 记录行号用于定位分析
    while text_line:
        output.writelines(text_line)
        text_line = file.readline()
        line_idx = line_idx + 1

finally:
    file.close()
    file2.close()
    output.close()
    # 对开始和结束日期数据进行修改
    # 重新打开输出文件进行日期的更改并存储为一个新文件
    output1 = open('SWMMgis_out1.inp', 'w')  # 输出文件名称
    with open('SWMMgis_out.inp', 'r') as f:
        for text_line in f:
            searchObj_startDate = re.search(r'START_DATE', text_line)
            searchObj_startTime = re.search(r'START_TIME', text_line)
            searchObj_reportStartDate = re.search(r'REPORT_START_DATE', text_line)
            searchObj_reportStartTime = re.search(r'REPORT_START_TIME', text_line)
            searchObj_endDate = re.search(r'END_DATE', text_line)
            searchObj_endTime = re.search(r'END_TIME', text_line)
            if searchObj_startDate:
                if searchObj_reportStartDate:
                    text_line = text_line[0:21] + START_DATE + '\n'
                    output1.writelines(text_line)
                else:
                    text_line = text_line[0:21] + START_DATE + '\n'
                    output1.writelines(text_line)
            elif searchObj_startTime:
                if searchObj_reportStartTime:
                    text_line = text_line[0:21] + START_TIME + '\n'
                    output1.writelines(text_line)
                else:
                    text_line = text_line[0:21] + START_TIME + '\n'
                    output1.writelines(text_line)
            elif searchObj_endDate:
                text_line = text_line[0:21] + END_DATE + '\n'
                output1.writelines(text_line)
            elif searchObj_endTime:
                text_line = text_line[0:21] + END_TIME + '\n'
                output1.writelines(text_line)
            else:
                output1.writelines(text_line)
    output1.close()
    os.remove('SWMMgis_out.inp') #删除中间文件SWMMgis_out.inp，得到了一个修改完成的WMMgis_out1.inp文件

'''///////////////////////////////////////////////////////////'''
# 调用SWMM运行修改[TIMESERIES]后的.inp文件，并输出.rpt文件
desfile='SWMMgis.inp'
os.remove(desfile)
srcfile='SWMMgis_out1.inp'
os.rename(srcfile,desfile) #将生成的Out文件改名为原来的文件名
os.system(r'D:\Study\SWMM\SWMM-ENG\EPA_SWMM_5.1.015\swmm5.exe SWMMgis.inp SWMMgis.rpt') #调用模拟软件生成rpt文件

'''///////////////////////////////////////////////////////////'''
# 将.rpt文件中需要的部分提取出来.txt
# 找到并截取出Node Depth Summary部分的内容
file = open(r'SWMMgis.rpt', 'r')
output = open(r'SWMMgis.csv', 'w+')

try:
    text = file.read()

    # 找到并截取出Node Summary部分的内容
    start = re.search('Node Depth Summary', text).span()[1]
    end = re.search('Node Inflow Summary', text).span()[0]
    nodesummary = text[start:end]

    # 去除表头多余的内容
    start2 = re.search(' ---------------------------------------------------------------------------------', nodesummary).span()[1]
    nodesummary2 = nodesummary[start2:][1:]
    start3 = re.search(' ---------------------------------------------------------------------------------', nodesummary2).span()[1]
    nodesummary3 = nodesummary2[start3:][1:]
    # print(nodesummary3)
    # 去除末尾多余的内容
    end2 = re.search('\n  \n  \n', nodesummary3).span()[0]
    data = nodesummary3[0:end2]
    # print(data)

    # 查找flood的对应内容
    startFlood = re.search('Node Flooding Summary', text).span()[1]
    endFlood = re.search('Outfall Loading Summary', text).span()[0]
    nodesummaryFlood = text[startFlood:endFlood]
    # print(nodesummaryFlood)

    insertDataArrary = []  # 该数组用于存储取出来的flood volume
    if re.search('  No nodes were flooded.',nodesummaryFlood):
        i = 2
        while i < len(data):
            insertDataArrary.append(0)
            i += 84
    else:
        # 去除表头多余的内容
        start2Flood = re.search('  --------------------------------------------------------------------------', nodesummaryFlood).span()[1]
        nodesummary2Flood = nodesummaryFlood[start2Flood:][1:]
        start3Flood = re.search('  --------------------------------------------------------------------------', nodesummary2Flood).span()[1]
        nodesummary3Flood = nodesummary2Flood[start3Flood:][1:]
        # 去除末尾多余的内容
        end2Flood = re.search('\n  \n  \n', nodesummary3Flood).span()[0]
        dataFlood = nodesummary3Flood[0:end2Flood]

        # insertDataArrary = [] #该数组用于存储取出来的flood volume
        i = 2; j = 6
        while j < len(data):
            findData = data[i:j]
            m = 2; n = 6
            flag = 0 # 记录depth中的节点是否在flood中
            while n < len(dataFlood):
                floodData = dataFlood[m:n]
                if findData == floodData:
                    flag = 1 # depth中的节点在flood中
                    insertData = dataFlood[m+59:m+64]
                    insertDataArrary.append(int(float(insertData)*1000)) # 将相应的值取出来并乘以1000
                m += 77; n += 77
            if flag == 0:
                insertDataArrary.append(0)
            i += 84; j += 84

    # 在内容顶部补充新的表头
    header = '  Name                 Type                 AveDepth     MaxDepth      MaxHGL    DaysMax    HrsMax   RptMax   OFlowV(m3)\n'
    result = header+data

    # 将多个空格替换为一个空格
    result = re.sub(' +', ' ', result)

    # 输出为为本地文件
    outputdata = []
    resultArray = result.split('\n')
    i = 0
    for line in resultArray:
        line = line.lstrip() # 截取掉每一行最左边的空格
        linearray = line.split(' ')
        # 第一行是表头，需要剔除出来
        if i == 0:
            outputdata.append(','.join(linearray)+'\n')
        else:
            outputdata.append(','.join(linearray)+','+str(insertDataArrary[i-1])+'\n')
        i += 1
    output.writelines(outputdata)
finally:
    file.close()
    output.close()

# 读取rpt文件，生成数据序列//////////////////////////////////////////////////////////
file = open(r'SWMMgis.rpt', 'r')
outputDataSeries = open(r'DataSeries.csv', 'w+')
try:
    text = file.read()
    # 找到并截取出Node Results部分的内容
    start = re.search('Node Results', text).span()[1]
    end = re.search('Analysis begun on', text).span()[0]
    nodesummary = text[start:end]
    nodenum = re.findall('<<<.*>>>',nodesummary)  # 获取到所有的节点
    # header = 'nodeName   date   time   FloodingCMS   Depthmeters   Headmeters'
    # 存储节点名称
    nodeNameSeries = []
    # 存储日期
    dateSeries = []
    # 存储时间
    timeSeries = []
    # 存储Flooding CMS 数据
    floodingSeries = []
    # 存储Depth meters 数据
    depthSeries = []
    # 存储Head meters 数据
    headSeries = []
    typeSeries = []
    AveDepthSeries = []
    DaysMaxSeries = []
    HrsMaxSeries = []
    # 单独存储日期和时间
    date = []
    time = []
    for i in range(len(nodenum)):
        # print(i)
        nameNode = nodenum[i][9:len(nodenum[i])-3]  # 获取节点名称
        nameNode = "{:<5}".format(nameNode)
        if i == len(nodenum)-1:
            nodestart = re.search(nodenum[i], nodesummary).span()[1]
            nodedata = nodesummary[nodestart:]  # 获取到每个节点的相应数据
        else:
            nodestart = re.search(nodenum[i], nodesummary).span()[1]
            nodeend = re.search(nodenum[i + 1], nodesummary).span()[0]
            nodedata = nodesummary[nodestart:nodeend]  # 获取到每个节点的相应数据
        # 去除节点数据的多余部分
        start2 = re.search(' ----------------------------------------------------------------',nodedata).span()[1]
        nodedata2 = nodedata[start2:][1:]
        start3 = re.search(' ----------------------------------------------------------------',nodedata2).span()[1]
        nodedata3 = nodedata2[start3:][1:]
        # 去除节点数据后边的空行
        nodeend2 = re.search('\n  \n', nodedata3).span()[0]
        dataNode = nodedata3[0:nodeend2]
        # print(dataNode)
        # 相应数据在文件中的位置
        date_start = 3; date_end = 13
        time_start = 14; time_end = 22
        flooding_start = 37; flooding_end = 43
        depth_start = 47; depth_end = 53
        head_start = 57; head_end = 63
        dateNum = 0
        while date_start < len(dataNode):  # 一行数据长度为63
            dateNum += 1
            nodeNameSeries.append(nameNode)
            dateSeries.append(dataNode[date_start:date_end])
            timeSeries.append(dataNode[time_start:time_end])
            floodingSeries.append(dataNode[flooding_start:flooding_end])
            depthSeries.append(dataNode[depth_start:depth_end])
            headSeries.append(dataNode[head_start:head_end])
            typeSeries.append('JUNCTION')
            AveDepthSeries.append('0.001')
            DaysMaxSeries.append('0.001')
            HrsMaxSeries.append('0.001')
            date_start += 64
            date_end += 64
            time_start += 64
            time_end += 64
            flooding_start += 64
            flooding_end += 64
            depth_start += 64
            depth_end += 64
            head_start += 64
            head_end += 64
        date = dateSeries[0:dateNum]
        time = timeSeries[0:dateNum]
    dataWrite = '  date  ' + ',' + '    time  ' + ',' + 'Name ' + ',' + '   Type' + ',' + ' AveDepth' + ',' + ' MaxDepth' + ',' + \
                ' MaxHGL' + ',' + ' DaysMax' + ',' + ' HrsMax' + ',' + ' RptMax' + ',' + ' OFlowV(m3)' + '\n'
    for i in range(len(date)):
        for j in range(len(dateSeries)):
            if dateSeries[j] == date[i] and timeSeries[j] == time[i]:
                dataWrite += dateSeries[j] + ',' + timeSeries[j] + ',' + nodeNameSeries[j] + ',' + typeSeries[j] + ',' + AveDepthSeries[j] + ','+ depthSeries[j] + ',' + headSeries[j] + ',' + DaysMaxSeries[j] + ',' + HrsMaxSeries[j] + ',' + depthSeries[j] + ',' + floodingSeries[j] + '\n'
    outputDataSeries.writelines(dataWrite)
finally:
    file.close()
    outputDataSeries .close()




