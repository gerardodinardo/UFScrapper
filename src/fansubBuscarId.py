def fansubBuscarId(fansubs_,fansubName):
   
    fansubs_id = []

    for i2 in fansubName:
        if i2 in fansubs_:
            fansubs_id.append(fansubs_[i2])
    
    return fansubs_id