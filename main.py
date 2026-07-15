from api import search_anime, get_display_title, get_trailer_info

print ("Welcome to the Anime Search CLI!")


def display_results(results):
    """List of anime results"""
    for i, anime in enumerate(results, start=1):
        title = get_display_title(anime)
        episodes = anime.get("episodes") or "NONE"
        year = anime.get("year") or "NONE"
        print(f"{i}. {title} ({year}) - Episodes: {episodes}")



def get_user_choice(results):
    """Pick a number from the list of results
    Returns the selected anime or None if invalid choice.
    """
    while True:
        choice = input("\nPick a number from the list (or 'q' to quit): ")
        
        if choice.lower() == 'q':
            return None
        if  choice.isdigit() and 1<= int(choice) <= len(results):
           return results[int(choice) - 1]
        
        print("Invalid choice. Please try again.")



#main function (result, selection and trailer link )

def main():
    query = input("\nEnter anime name to search: ")   
    results = search_anime(query)



    if not results:
            print("No results found.")
            return

    display_results(results)
    selected_anime = get_user_choice(results)

    if selected_anime is None:       
        print("No anime selected. Exiting.")
        return
    
    title = get_display_title(selected_anime)
    print(f"\nYou selected: {title}")


    trailer_info = get_trailer_info(selected_anime)

    if not trailer_info:
        print("No trailer available for this anime.")
        return
    
    print(f"Trailer URL: {trailer_info['url:']}")
if __name__ == "__main__":
    main()


print("\n'None' mainly means not aired yet, ongoing or Just announced :)")     #help for status