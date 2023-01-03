import itertools

def get_distance(w1, w2, item):
    if w1 in item and w2 in item:
        w1_indexes = [index for index, value in enumerate(item) if value == w1]    
        w2_indexes = [index for index, value in enumerate(item) if value == w2]    
        distances = [abs(item[0] - item[1]) for item in itertools.product(w1_indexes, w2_indexes)]
        return {'min': min(distances), 'avg': sum(distances)/float(len(distances))}
    else:
        return {'min': 100, 'avg': 100}
def get_proximity(distance):
    return 1 / (distance*distance)