import urllib.request
# 1-5044
# Missing: 1340-1341, 1708, 1892-1895, 2573, 3310-3311, 4078, 4081, 4084, 4087,
# 4090, 4093, 4123-4124, 4126, 4228-4230, 4354-4356, 4577, 4630-4633, 4683-4686,
# 4689-4691, 4699-4706, 4712-4715, 4722-4723, 4792, 4834-4843, 4900-4902,
# 4998-5026, 5033-5035, 5045-

def getPic(start, end):
    for picNumber in range(start, end):
        try:
            urllib.request.urlretrieve('https://storage.googleapis.com/mirubot/padimages/jp/full/' + str(picNumber) + '.png', 'Images/' + str(picNumber) + '.png')
        except urllib.error.HTTPError:
            print('Image ' + str(picNumber) + ' is missing! :(')

start = input("Monster number to start on: ")
end = input("Monster number to end on: ")
getPic(int(start), int(end) + 1)
