#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        d_key = list(a_dictionary)[0]
        highest = (a_dictionary[d_key], d_key)
        for i, v in a_dictionary.items():
            if highest[0] < v:
                highest = v, i
        return highest[1]
    else:
        return None


if __name__ == '__main__':
    best_score({})
