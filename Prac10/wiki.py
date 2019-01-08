import wikipedia

def search_in_wiki():
    search_word = input("Input search phrase:")
    my_flag = False
    while my_flag:
        if search_word =="":
            my_flag = False
        else:
            my_flag = True
            print(wikipedia.search(search_word))
search_in_wiki()