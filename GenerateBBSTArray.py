def GenerateBBSTArray(a):
    if len(a) < 1: return None
    array_sorted = sorted(a)
    def recursivBBSTArray(array_sorted,final_array=[None] * len(a), I=0):
        central_element = len(array_sorted) // 2
        if not array_sorted == []:
            final_array[I] = array_sorted[central_element]
            recursivBBSTArray(array_sorted[:central_element], final_array, 2*I+1)
            recursivBBSTArray(array_sorted[central_element+1:], final_array, 2*I+2)
        return final_array
    resultat = recursivBBSTArray(array_sorted)
    return resultat
