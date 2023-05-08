import pandas as pd
import os
import re
import csv
import glob

csvFile = open("AUS_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\AUS\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("AUT_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\AUT\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("BEL_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\BEL\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("BGR_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\BGR\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("BLR_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\BLR\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("CAN_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\CAN\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("CHE_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\CHE\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("CHL_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\CHL\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("CZE_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\CZE\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("DEUTE_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\DEUTE\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("DEUTNP_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\DEUTNP\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("DEUTW_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\DEUTW\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("DNK_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\DNK\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("ESP_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\ESP\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("EST_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\EST\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("FIN_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\FIN\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("FRACNP_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\FRACNP\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("FRATNP_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\FRATNP\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("GBR_NIR_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\GBR_NIR\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("GBR_NP_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\GBR_NP\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("GBR_SCO_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\GBR_SCO\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("GBRCENW_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\GBRCENW\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("GBRTENW_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\GBRTENW\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("GRC_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\GRC\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("HKG_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\HKG\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("HRV_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\HRV\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("HUN_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\HUN\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("IRL_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\IRL\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("ISL_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\ISL\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()
csvFile = open("ISR_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\ISR\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("ITA_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\ITA\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("JPN_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\JPN\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("KOR_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\KOR\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("LTU_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\LTU\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("LUX_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\LUX\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open("LVA_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open("hmd_countries_20230317\LVA\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"NLD_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\NLD\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"NOR_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\NOR\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"NZL_MA_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\NZL_MA\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"NZL_NM_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\NZL_NM\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"NZL_NM_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\NZL_NM\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"NZL_NP_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\NZL_NP\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"POL_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\POL\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"PRT_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\PRT\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"SVK_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\SVK\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"SVN_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\SVN\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"SWE_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\SWE\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"TWN_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\TWN\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"UKR_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\UKR\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

csvFile = open(r"USA_Deaths_1x1.csv", 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
csvRow = []

f = open(r"hmd_countries_20230317\USA\STATS\Deaths_1x1.txt", 'r', encoding='GB2312')
for line in f:
    csvRow = line.split()
    writer.writerow(csvRow)

f.close()
csvFile.close()

path = r".\csv"

FileNames = os.listdir(path)
df = pd.DataFrame(data=None,columns=['Year','Age','Female','Male','Total'])
for fn in FileNames:
    country = ''
    for word in fn:
        if word == '_':
            break
        else:
           country += word
    if re.search(r'\.csv$', fn):
        fullfilename = os.path.join(path, fn)
        df_temp = pd.read_csv(fullfilename,encoding='ISO-8859-1',on_bad_lines='skip')
        df_temp.insert(loc=0, column='country', value=country)
        df = pd.concat([df,df_temp])

df.to_csv('result.csv', index=False)

folder_path = ""

csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

for file in csv_files:
    if os.path.basename(file) != "result.csv":
        os.remove(file)

