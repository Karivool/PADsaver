import urllib.request

def getPic(start, end):
    for picNumber in range(start, end):
        try:
            urllib.request.urlretrieve('https://f002.backblazeb2.com/file/dadguide-data/media/portraits/' + '0' + str(picNumber) + '.png', 'Images/' + str(picNumber) + '.png')
        except urllib.error.HTTPError:
            print('Image ' + str(picNumber) + ' is missing! :(')

start = input("Monster number to start on: ")
end = input("Monster number to end on: ")
getPic(int(start), int(end) + 1)
