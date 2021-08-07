citizens - num_citizens # white_walkers
walkers - num_walkers   # white_walkers
number_of_doors - doors_count # Keymaker; чтобы отличить от переменной door_number
door_number - door_index    # Keymaker
A - sourse_sequence     # TransformTransform
B - transform_sequence  # TransformTransform
num_diff_symbols - diff_symbols_count   # # SherlockValidString
counts - diff_char_counts    # SherlockValidString
queue - Task_Queue # BastShoe
item_name_count - item_data/ item_info # ShopOLAP; неудачное имя - можно подумать, что переменная обозначает количество имен, а не данные имя/количество
item_name_count_array - item_data_array # ShopOLAP
report - sorted_items # ShopOLAP; неинформативное имя
num_max_votes_person - # MassVote; переменная вводила путаницу, заменил на функцию max(Votes)
max_count - leaders_count # MassVote; более точное определение
emeralds_s - first_char # squirrel