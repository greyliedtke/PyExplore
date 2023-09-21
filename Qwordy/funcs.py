# imports

from PyDictionary import PyDictionary
dictionary=PyDictionary()


# parse guessed words and link to google
def guess_parser(guess_dict:dict):
    # file to convert guess dictionary into markdown list of items
    md_string = ""
    points = 0
    for k, v in guess_dict.items():
        try:
            points += int(v["points"])
            
            md_string += f"\n- [{k}](https://www.google.com/search?q={k}) ({v['points']})"
            v = dict(v["def"])
            for nva, nvav in v.items():
                md_string += f"\n       - {nva}: {nvav[0]}"
        except:
            continue
    return md_string, points

def guess_inc(guess_dict:dict):
    # file to convert guess dictionary into markdown list of items
    md_string = ""
    for k, v in guess_dict.items():
        md_string += f"\n- {k}"
    return md_string