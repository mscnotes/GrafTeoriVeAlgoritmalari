import itertools

def domination_number(V, E):
    """
    V: düğüm listesi, örn. [1, 2, 3, 4]
    E: kenar listesi, örn. [(1,2), (2,3)]
    """
    n = len(V)
    delta = n  # başlangıçta maksimum değer
    
    # Her düğümün komşularını bul
    neighbors = {v: set() for v in V}
    for (u, v) in E:
        neighbors[u].add(v)
        neighbors[v].add(u)
    
    # 1'den n'e kadar tüm düğüm kombinasyonlarını dene
    for r in range(1, n + 1):
        for subset in itertools.combinations(V, r):
            dominated = set(subset)  # kümenin kendisi baskın
            for v in subset:
                dominated |= neighbors[v]  # komşular da kapsanır
            if dominated == set(V):  # tüm düğümler kapsandı mı?
                return r, subset  # en küçük baskın küme bulundu
    
    return delta, None


V = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16]
E = [(1, 2), (1, 5), (2, 3),(2,6),(3,4),(3,7),(4,8),(5,6),(5,9),
     (6,10),(6,7),(7,8),(7,11),(8,12),(9,10),(9,13),
     (10,11),(10,14),(11,12),(11,15),(12,16),(13,14),(14,15),(15,16)]

delta, dom_set = domination_number(V, E)

print(f"Baskınlık sayısı (δ): {delta}")
print(f"Baskın küme: {dom_set}")
