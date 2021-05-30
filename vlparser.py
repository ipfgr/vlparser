from requests_html import HTMLSession
import re
session = HTMLSession()

obj = {}

lottery_type = 0
last_lottery_number = 0

# Open file for write results
file = open("results.txt", "w")

# Write results to file
def writeToFileResult(idx):
    res = session.get('http://www.vietlott.vn/en/trung-thuong/ket-qua-trung-thuong/' + str(lottery_type) + '?id=' + str(idx) + "&nocatche=1")
    num = res.html.find('.day_so_ket_qua_v2', first=True)
    if num:
        splitted = re.findall("..", num.text)
        obj[str(idx)] = splitted
        print(splitted)
        # file.writelines('\n' + "Result for " + str(idx) + " || ")
        # file.writelines(splitted)
    else:
        print("Error get numbers, please check url")


# Get last lottery number
def getLastLotteryNumber(num):
    res = session.get('http://www.vietlott.vn/en/trung-thuong/ket-qua-trung-thuong/' + str(num))
    last_lottery = res.html.find('div.chitietketqua_title > h5 > b', first=True)
    last_lottery_number = last_lottery.text[1:6]
    getResults(int(last_lottery_number))

# Get numbers and write to file
def getResults(num):
    for i in range (1, num +1 ):
        idx = ""
        if i < 10:
            idx = ("0000" + str(i))
        elif i< 100:
            idx = ("000" +str(i))
        elif i <= num:
            idx = ("00" +str(i))
        else:
            file.write(obj)
        print("Get results for lottery number " + idx)
        writeToFileResult(idx)

# Get user input
inp = input("Please enter 1 for 6/45 lottery or 2 for 6/55 lottery" + '\n')

# Convert input to integer
inp = int(inp)

# Check if user enter correct lottery type
if inp < 1 or inp > 2:
    print("Please enter correct lottery type:")
elif inp == 1:
    lottery_type = 645
    print("Get info for lottery 6/45")
    getLastLotteryNumber(645)
elif inp == 2:
    lottery_type = 655
    print("Get info for lottery 6/55")
    getLastLotteryNumber(655)




