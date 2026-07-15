import requests
#base url (MAL DATA)

BASE_URL = "https://api.jikan.moe/v4"


#anime search

def search_anime(query):
    """
    Search anime by name.
    'query' search result user typed
    Returns a list of anime results.
    """
    url = f"{BASE_URL}/anime"
    params = {
        "q": query,
        "limit": 10,                 # Limit to 10 results
        "order_by": "popularity",    # Order by popularity
        "sort": "asc"                #sort ascending
        }              
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print ("Something went wrong, (API Error)")
        return []

    data = response.json()
    return data["data"]               #anime list


#anime title

def get_display_title(anime):
    """
    Best title for user
    Mainly English title,else romaji title
    """
    if anime.get("title_english"):
        return anime["title_english"]
    else:
        return anime["title"]


#anime trailer

def get_trailer_info(anime):
    """
    Get trailer information for an anime.
    Returns the trailer URL and YouTube ID, or None if not available.
    """
    trailer = anime.get("trailer")
    if not trailer or not trailer.get("youtube_id"):
        return None

    return {
        "url:": trailer.get("url"), 
        "youtube_id": trailer.get("youtube_id")
    }

#test
if __name__ == "__main__":
    results = search_anime("attack on titan")
    for i, anime in enumerate(results, start=1):
        title = get_display_title(anime)
        print(f"{i}. {title}")
        print(f"   trailer field: {anime.get('trailer')}")
        print()
