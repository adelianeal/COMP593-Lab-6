import requests
from sys import argv

def main():
    pokemon = argv[1]
    dict = get_poke_info(pokemon)
    if dict:
        poke_strings = get_poke_strings(dict)
        pastebin_url = post_to_pastebin(poke_strings[0], poke_strings[1])
        print(pastebin_url)

def post_to_pastebin(title, body):
    print('Posting to PateBin...', end='')
    params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    }

    resp_msg = requests.post("https://pastebin.com/api/api_post.php", data=params)
    
    if resp_msg.status_code  == 200:
        print('success')
        return resp_msg.text
    else:
        print('failed. Code:', resp_msg.status_code)
        return str(resp_msg.status_code)

def get_poke_strings(dict):
        title = str.capitalize(dict['name']) + "'s Abilities"
        body_text = ''
        for poke_abilities in dict['abilities']:
            body_text += '-' + poke_abilities['ability']['name'] + '\n'
            
        return (title, body_text)

def get_poke_info(pokemon):
    print('Getting Pokemon Information...', end='')

    resp_msg = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon)

    if resp_msg.status_code == 200:
        print('success')
        return resp_msg.json()   
    else:
        print('failed. Code:', resp_msg.status_code)
        return
    
main()