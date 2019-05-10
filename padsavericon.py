import urllib.request

def getPic(start, end):
    for picNumber in range(start, end):
        try:
            urllib.request.urlretrieve('https://storage.googleapis.com/mirubot/padimages/jp/portrait/' + str(picNumber) + '.png', 'IconImages/' + str(picNumber) + '.png')
        except urllib.error.HTTPError:
            print('Image ' + str(picNumber) + ' is missing! :(')

start = input("Monster number to start on: ")
end = input("Monster number to end on: ")
getPic(int(start), int(end) + 1)
