def copy_paste(text):

    items = text.split()
    
    clipboard = ""
    result_list = []
    
    i = 0
    while i < len(items):
        item = items[i]
        
        if item == 'Ctrl' and i + 2 < len(items) and items[i+1] == '+' and items[i+2] == 'C':
            clipboard = " ".join(result_list)
            i += 3
        
        elif item == 'Ctrl' and i + 2 < len(items) and items[i+1] == '+' and items[i+2] == 'V':
            
            if clipboard:
                result_list.append(clipboard)
            i += 3 
            
        else:
            result_list.append(item)
            i += 1
            
    return " ".join(result_list)