import itertools;
import requests;



def get_all_players() -> list:
    response = requests.get("https://mach-eight.uc.r.appspot.com")
    res_body = response.json()['values']
    return res_body

def get_inches_pairs_ids(players:list, threshold:int) -> set:
    get_inches = [int(player['h_in']) for player in players]
    couples = set()
    for c_heights in itertools.combinations(get_inches,2):
        if sum(c_heights) == threshold:
            couples.add(tuple([get_inches.index(c_height) for c_height in c_heights]))
    return couples

def search_players(in_pairs:set, pl:list) -> None:
    for c in in_pairs:
	    c_1 = pl[c[0]]
	    c_2 = pl[c[1]]
	    couples = f'{c_1["first_name"]} {c_1["last_name"]} - {c_2["first_name"]} {c_2["last_name"]}'
	    print(couples)

def main(threshold:int)-> None:
    player_list = get_all_players()
    all_inches = get_inches_pairs_ids(player_list,threshold)
    if len(all_inches) != 0:
        print(f'{len(all_inches)} pairs of players found!')
        search_players(all_inches,player_list)
    else:
        print("No matches found!")

if __name__ == "__main__":
    threshold = 180
    main(threshold)