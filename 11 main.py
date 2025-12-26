def journey_ends(flights):
    from_cities = set()
    to_cities = set()
    
    for start, end in flights:
        from_cities.add(start)
        to_cities.add(end)
    
    # Начальный город — тот, откуда улетают, но никуда не прилетают
    start_city = (from_cities - to_cities).pop()
    # Конечный город — тот, куда прилетают, но ниоткуда не улетают
    end_city = (to_cities - from_cities).pop()
    
    return (start_city, end_city)




