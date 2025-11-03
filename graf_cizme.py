# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 13:47:48 2025

@author: Spyderman
"""

import networkx as nx
import matplotlib.pyplot as plt
"""
V = ["C1","C2","R1","Router2","w-R3"]
E = [("Router2","C2"),("R1","Cloud1")]
"""
#V = ["C1","C2","R1","R2","wR3","S1","S2","Serv1","Serv2","Serv3","Serv4","Serv5","Serv6","PC1","PC2","PC3","PC4","L1","L2"]
#E = [("C1","R1"),("C2","R2"),("R1","R2"),("R1","wR3"),("R1","PC1"),("R1","Serv1"),("R1","S1"),("R1","L1"),("wR3","PC2"),("wR3","L1"),("PC2","PC3"),("S1","Serv2"),("S1","Serv3"),("S1","Serv4"),("S1","Serv5"),("S2","L2"),("S2","PC4"),("S2","PC3"),("R2","S2")]
V = ["C1","C2","R1","R2","wR3","S1","S2","Serv1","Serv2","Serv3","Serv4","Serv5","Serv6","PC1","PC2","PC3","PC4","L1","L2"]
E = [("C1","R1"),("C2","R2"),("R1","R2"),("R1","wR3"),("R1","PC1"),("R1","Serv1"),("R1","S1"),("R1","L1"),("wR3","PC2"),("wR3","L1"),("PC2","PC3"),("S1","Serv2"),("S1","Serv3"),("S1","Serv4"),("S1","Serv5"),("S2","L2"),("S2","PC4"),("S2","PC3"),("R2","S2"),("Serv6","S1")]
#V = ["C1","C2","R1","R2","wR3"]
#E = [("C1","R1"),("C2","R2"),("R1","R2"),("R1","wR3")]

# Yeni bir boş grafik oluştur
G = nx.Graph()

# Düğümleri ekle
G.add_nodes_from(V)

# Kenarları ekle
G.add_edges_from(E,length=50)

# Grafiği çiz
plt.figure(figsize=(8, 6))  # Görselin boyutlarını ayarlayabilirsin
nx.draw(G, with_labels=True,  node_size=1000,width=2.0, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")

# Başlık ekle
plt.title("Network Topoloji Grafı")

# Görseli bir dosyaya kaydet
plt.savefig("graph_output.png", format="PNG")