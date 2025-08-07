items = [1, 2, 2, 3, 4, 4, 5]                   # original list with duplicates
unique_items = list(dict.fromkeys(items))      # remove duplicates, preserve order
print(unique_items)                            # display the list without repeats