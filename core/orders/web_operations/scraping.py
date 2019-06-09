from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from random import randint


def scrapYoutubeWatchURL(order, cutter="música"):
    # from order string we only get what we need splitting by cutter
    # (its gonna be at pos[1] most of cases like ---> "pon [Bob Marley]" or pon música [de Bob Dylan])
    realPetition = order.split(cutter)[1].strip()

    # then we build the real search YouTube part of URL (from "pon Bob Marley" to youtube.com/results?search_query=bob+marley)
    searchQuery = "+".join(realPetition.split(" "))
    url = "https://www.youtube.com/results?search_query=" + searchQuery

    # its needed to remove some spanish characters to be sure that the URL is going to work
    trans = str.maketrans("áéíóúüñ", "aeiouun")
    url = url.translate(trans)

    # after that we need to send a request with the URL to make scrapping with urlopen() method from urllib.request
    # this is because from "search_query=bob+marley" we need to get "watch?v=AAA3KTsUQig" (that AAA3K... code)
    uClient = urlopen(url, None, 1000)
    # so we read it and close it
    page = uClient.read()
    uClient.close()

    # after getting the page info we start scrapping with BeautifulSoup() method from bs4 library
    soupPage = soup(page, "html.parser")
    links = soupPage.findAll("a")

    # once we got all <a href=""> labels from YouTube<html code> we need to find the one with "watch" in href attribute
    # we are going to get "/watch?v=AAA3KTsUQig" here
    link = ""
    for l in links:
        if "watch" in l["href"]:
            link = l["href"]
            break

    # now we are ready to return our final URL to play some music or videos from YouTube in our browser
    # so we build the URL we are going to use "https://www.youtube.com/watch?v=AAA3KTsUQig"
    return "https://www.youtube.com" + link


def getLabel(startingUrl, buildedOrder, label, labelObj, sufix="", mode="single"):

    # this is a generic function based on the scrapYoutubeWatchURL() example, so we procede as before

    trans = str.maketrans("áéíóúüñ", "aeiouun")
    startingUrl += buildedOrder

    # in this case I decided to add a sufix so we can build more complex URLs
    startingUrl = startingUrl.translate(trans) + sufix

    # I also add a header so we can do scrapping without having forbidden error for some domains
    hdr = {"User-Agent": "Mozilla/5.0"}
    req = Request(startingUrl, headers=hdr)
    page = urlopen(req)
    soupPage = soup(page, "html.parser")

    # instead returning a URL fully builded, I return the wanted label so we can work with it later
    if "single" in mode:
        targetLabel = soupPage.find(label, labelObj)
    else:
        targetLabel = soupPage.find_all(label, labelObj)
    return targetLabel


def findInDictionary(label):
    result = label.li.text.split(". ")[1].split(":")[0].split(".")[0].lower() + " "
    if "inform" in result:
        result = label.li.text.split("inform.")[1].split(":")[0] + " "
    if "y f " in result:
        result = label.li.text.split("f. ")[1].split(":")[0].split(".")[0].lower()
    return result


def findWeather(label):
    return label["data-temp"]


def findJoke(labels):
    return labels[randint(0, len(labels) - 1)].text
