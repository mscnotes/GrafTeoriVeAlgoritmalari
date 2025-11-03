import itertools

def independence_number(V, E):
    """
    V: düğüm listesi, örn. [1, 2, 3, 4]
    E: kenar listesi, örn. [(1,2), (2,3)]
    """
    n = len(V)
    max_independent_set = []
    
    # 1'den n'e kadar tüm düğüm kombinasyonlarını dene
    for r in range(1, n + 1):
        for subset in itertools.combinations(V, r):
            # Bu altküme bağımsız mı?
            independent = True
            for (u, v) in E:
                if u in subset and v in subset:
                    independent = False
                    break
            if independent and len(subset) > len(max_independent_set):
                max_independent_set = subset
    
    beta = len(max_independent_set)
    return beta, max_independent_set


# V = [1, 2, 3, 4,5,6,7]
# E = [(1, 2), (1,3),(2,4),(2,5),(2,6),(3,5),(4,5),(5,7),(6,7)]

V = ["C1","C2","R1","R2","wR3","S1","S2","Serv1","Serv2","Serv3","Serv4","Serv5","Serv6","PC1","PC2","PC3","PC4","L1","L2"]
E = [("C1","R1"),("C2","R2"),("R1","R2"),("R1","wR3"),("R1","PC1"),("R1","Serv1"),("R1","S1"),("R1","L1"),("wR3","PC2"),("wR3","L1"),("PC2","PC3"),("S1","Serv2"),("S1","Serv3"),("S1","Serv4"),("S1","Serv5"),("S2","L2"),("S2","PC4"),("S2","PC3"),("R2","S2"),("Serv6","S1")]
beta, indep_set = independence_number(V, E)

print(f"Bağımsızlık sayısı (β): {beta}")
print(f"Herhangi Bir Bağımsız küme: {indep_set}")
