#
def get_p_distance (list1, list2):
    if len (list1)!= len (list2):
        raise ValueError ("both list must be of the same length")
    difference = sum (1 for a, b in zip (list1, list2) if a !=b)
    p_distance = difference/len (list1)
    return p_distance

def get_p_distance_matrix (dna_lists):
    n= len(dna_lists)
    p_distance_matrix = [[0] *n for _ in range(n)]

    for i in range (n):
        for j in range (i, n):
            p_dist = get_p_distance(dna_lists [i], dna_lists [j])
            p_distance_matrix [i][j]= p_dist
            p_distance_matrix [j][i] = p_dist
    return p_distance_matrix