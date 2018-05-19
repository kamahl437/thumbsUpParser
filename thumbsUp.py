import json
import requests
headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer BQBziZTb7NCKnZi34FLgylbIyeYvwe5w0UQcw7NULVUVV7sacp4OC1Lk63Ga8791h9cq-Lbbu_I-boBLcKYG9nPJfE2ajlMHbGZPuoTobGvPkbqo6IyQj1Gj7Jc8OCVtRX-iqrJTEaADsGrmEBInEYxxUPVfB3CjtpISGzAn5gjwZA-FUYKeEy4KCYcs3h7-UF1bwmL90jCOqIXK7SFdiT0GLuPactOKhdUTSaZ36SjYkel3Prnl6vbtFALhsk5YEqH4jAfRI-00GFnX3loGrHXtSO_qq32IAOY',
    'origin': 'https://open.spotify.com',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
def getSongId(query):
    r = requests.get(f"https://api.spotify.com/v1/search?type=album%2Cartist%2Cplaylist%2Ctrack&q={query}*&decorate_restrictions=true&best_match=true&limit=50&anonymous=false&market=from_token", headers=headers)
    return r.json()

def addToThumbsUp(songId):
    r = requests.put(f"https://api.spotify.com/v1/me/tracks?ids={songId}", headers=headers)

songList = json.load(open('thumbsup.json'))

for song in songList[1][0]:
    songArtistCombo = song[1] + ' ' + song[3]
    response = getSongId(songArtistCombo)
    try:
        addToThumbsUp(response["tracks"]["items"][0]["id"])
    except:
        print(f"following combo got no results {songArtistCombo}")


