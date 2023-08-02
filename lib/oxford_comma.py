def oxford_comma(items):
    if len(items)==2:
        new_string=" and ".join(items);
        return new_string;
    elif len(items)==3:
        new_string=", ".join(items[0:2])
        new_string=new_string+", and "+ items[2]
        #new_string=new_string + " and " + items[3]
        return new_string
    elif len(items)>3:
        new_string=", ".join(items[0:-1])
        new_string=new_string+", and "+ items[-1]
        return new_string
    else:
        new_string=", ".join(items);
        return new_string;
