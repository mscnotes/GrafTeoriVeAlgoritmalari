
import itertools

def all_independent_sets(V, E):
    """
    V: düğüm listesi, örn. [1,2,3,4]
    E: kenar listesi, örn. [(1,2), (2,3)]
    """
    n = len(V)
    independent_sets = []

    # Tüm altkümeleri dene (boş küme hariç)
    for r in range(1, n + 1):
        for subset in itertools.combinations(V, r):
            independent = True
            for (u, v) in E:
                if u in subset and v in subset:
                    independent = False
                    break
            if independent:
                independent_sets.append(subset)
    
    return independent_sets
V = ["C1","C2","R1","R2","wR3","S1","S2","Serv1","Serv2","Serv3","Serv4","Serv5","Serv6","PC1","PC2","PC3","PC4","L1","L2"]
E = [("C1","R1"),("C2","R2"),("R1","R2"),("R1","wR3"),("R1","PC1"),("R1","Serv1"),("R1","S1"),("R1","L1"),("wR3","PC2"),("wR3","L1"),("PC2","PC3"),("S1","Serv2"),("S1","Serv3"),("S1","Serv4"),("S1","Serv5"),("S2","L2"),("S2","PC4"),("S2","PC3"),("R2","S2"),("Serv6","S1")]
independent_sets = all_independent_sets(V, E)

print("Tüm bağımsız kümeler:")
for s in independent_sets:
    print(s)

# En büyük olanları (bağımsızlık sayısına eşit olanlar)
max_size = max(len(s) for s in independent_sets)
largest_sets = [s for s in independent_sets if len(s) == max_size]

print("\nEn büyük bağımsız kümeler:")
for s in largest_sets:
    print(s)
print(f"Bağımsızlık sayısı (β): {max_size}")
