# FINDING SURNAMES AND FIRST NAMES
from pyscript import display, document

def name_finder(e):
    document.getElementById("result").innerHTML = " "
    last_name = document.getElementById("surname").value.title().strip()
    first_name = document.getElementById("first").value.title().strip()
    combine_names = first_name + " " + last_name
    seeker_members = ['Alex Bueno', 'Eliana De La Cruz', 'Helena Magsino', 'Frances Torculas', 'Gudz Gudz', 'Lord Starscream']
    club_cheker = combine_names in seeker_members
    display_message = (f'{combine_names} is not in the list.', f'{combine_names} is in the list.')
    display(display_message[club_cheker], target='result')  
