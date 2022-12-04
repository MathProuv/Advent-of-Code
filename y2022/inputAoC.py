import private

def get_input(day, year=2022):
    """ return the personnal input of a day in Advent of Code """
    import requests
    cookies = private.cookies
    url = url_aoc(day,year) + "/input"
    try:
        requete = requests.get(url=url, cookies=cookies)
        input = requete.text[:-1]  # = requete.content.decode()[:-1]
        if input[:63] == "Please don't repeatedly request this endpoint before it unlocks":
            raise ImportError("Do you have a time machine? Because I don't")
        elif input[:28] == "Puzzle inputs differ by user":
            raise ImportError("You don't have the right cookie[\"session\"]")
        else:
            return input
    except requests.ConnectionError:
        print("No connection")


def get_input_file(day, year=2022, rewrite=False, name=None):
    """Return the content of the file "input/{year}_{day}.txt. 
    If the file doesn't exist: create and write the file

    :param rewrite: rewrite the file
    :param name: read/write/rewrite the file with the new name
    """

    if not name: name = name_file(day, year)
    try:
        if rewrite: raise FileNotFoundError
        file = open(name, "r")
        input = file.read()
    except FileNotFoundError:
        input = get_input(day, year)
        file = open(name, "w")
        file.write(input)
    file.close()
    return input

def name_file(day, year):
    return "../inputs/{y}_{d}.txt".format(y=str(year), d=str(day))
    return "{y}-day{d}.txt".format(y=str(year), d=str(day))

def url_aoc(day, year):
    return "https://adventofcode.com/" + str(year) + "/day/" + str(day)


###############################################################################
# TODO: le post de submit
def post_res(level, answer, day, year):
    import requests
    url = url_aoc(day, year)
    data = {
        "headers": {},
        "referrer": url,
        "referrerPolicy": "strict-origin-when-cross-origin",
        "body": "level="+str(level)+"&answer="+str(answer),
        "method": "POST",
        "mode": "cors",
        "credentials": "include"
    }
    data["headers"] = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }
    requete = requests.post(url+"/answer", data)
    return requete.text
