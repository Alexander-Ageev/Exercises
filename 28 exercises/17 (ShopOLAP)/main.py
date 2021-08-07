def merge_items(item_name_count_array):
    db = {}
    for i in range(len(item_name_count_array)):
        item_name_count = item_name_count_array[i].split()
        if item_name_count[0] in db:
            db[item_name_count[0]] += int(item_name_count[1])
        else:
            db[item_name_count[0]] = int(item_name_count[1])
    grouped_items_array = list(db.items())
    return grouped_items_array

def sort_items_for_count(items):
    items = sorted( items, key = lambda items: items[1], reverse = True )
    for i in range(len(items)):
        items[i] = (items[i][1], items[i][0])
    return items

def sort_items_for_name(items):
    report = []
    i = 0
    while i < len(items):
        j = i + 1
        items_with_equal_count = [str(items[i][1]) + ' ' + str(items[i][0])]
        while j < len(items) and items[i][0] == items[j][0]:
            items_with_equal_count.append(str(items[j][1]) + ' ' + str(items[j][0]))
            j += 1
        items_with_equal_count = sorted(items_with_equal_count)
        report += items_with_equal_count
        i = j
    return report

def ShopOLAP(N, items_array):
    merged_items = merge_items(items_array)
    sorted_items = sort_items_for_count(merged_items)
    sales_report = sort_items_for_name(sorted_items)
    return sales_report
    
    