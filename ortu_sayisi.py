import itertools

def minimum_vertex_cover(V, E):
    """
    V: düğüm listesi, örn. [1, 2, 3, 4]
    E: kenar listesi, örn. [(1,2), (2,3)]
    """
    n = len(V)
    min_cover_size = n  # maksimum olası boyuttan başla
    min_cover_set = None

    # 1'den n'e kadar tüm düğüm kombinasyonlarını dene
    for r in range(1, n + 1):
        for subset in itertools.combinations(V, r):
            # Bu küme tüm kenarları kapsıyor mu?
            covers_all = True
            for (u, v) in E:
                if not (u in subset or v in subset):
                    covers_all = False
                    break
            if covers_all:
                # Daha küçük bir örtü bulundu
                min_cover_size = r
                min_cover_set = subset
                return min_cover_size, min_cover_set  # En küçük bulunduğunda döndür
    
    return min_cover_size, min_cover_set


V = [1, 2, 3,4,5,6,7,8]
E = [(1, 2),(1,6), (2, 3),(2,4),(4,7),(4,5),(3,5),(5,8),(7,8),(6,7),(2,6)]

alpha, cover = minimum_vertex_cover(V, E)

print(f"Minimum örtü sayısı (α): {alpha}")
print(f"Örtü kümesi: {cover}")