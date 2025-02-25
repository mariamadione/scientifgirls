# Documentation du Package d'Analyse de Graphes et de Détection de Communautés

## Présentation
Ce package permet de :
- Charger une matrice de similarité à partir d'un fichier CSV
- Calculer les métriques de centralité d'un graphe
- Prédire les liens entre les nœuds d'un graphe
- Détecter des communautés dans le graphe avec les méthodes Louvain et Girvan-Newman

## Prérequis
Avant d'utiliser le package, assurez-vous d'avoir installé les bibliothèques suivantes :

```python
pip install pandas networkx matplotlib python-louvain
```

## Structure du Package

### 1. Fonction `load_similarity_matrix(input_file)`

**Description :**
Charge une matrice de similarité depuis un fichier CSV.

**Paramètres :**
- `input_file` : Chemin du fichier CSV

**Retour :**
- `pd.DataFrame` : Matrice de similarité

### 2. Fonction `calculate_centrality_metrics(G)`

**Description :**
Calcule les métriques de centralité (degré, proximité, vecteur propre) pour un graphe donné.

**Paramètres :**
- `G` : Graphe NetworkX

**Retour :**
- `pd.DataFrame` : Métriques de centralité pour chaque nœud

### 3. Fonction `calculate_link_prediction_metrics(G, df_filtered)`

**Description :**
Calcule les métriques de prédiction de liens : allocation de ressources, coefficient de Jaccard, Adamic-Adar, attachement préférentiel.

**Paramètres :**
- `G` : Graphe NetworkX
- `df_filtered` : DataFrame des relations filtrées

**Retour :**
- `pd.DataFrame` : Métriques de prédiction de liens

### 4. Fonction `detect_louvain_communities(G, df_filtered)`

**Description :**
Applique la méthode Louvain pour la détection de communautés.

**Paramètres :**
- `G` : Graphe NetworkX
- `df_filtered` : DataFrame des relations filtrées

**Retour :**
- `pd.DataFrame` : DataFrame avec la colonne des communautés ajoutée

### 5. Fonction `girvan_newman_communities(input_file, threshold)`

**Description :**
Applique l'algorithme Girvan-Newman pour la détection de communautés.

**Paramètres :**
- `input_file` : Chemin du fichier CSV
- `threshold` : Seuil de similarité pour filtrer les relations

**Retour :**
- `pd.DataFrame` : Communautés détectées

### 6. Fonction `main()`

**Description :**
Pipeline principal qui enchaîne les différentes étapes de création de graphe, calcul de métriques et détection de communautés.

**Exemple d'utilisation :**

```python
input_file = "path/to/your/similarity_matrix.csv"
output_link_file = "path/to/link_prediction_results.csv"
output_centrality_file = "path/to/centrality_metrics_results.csv"
output_louvain_file = "path/to/louvain_community_results.csv"
output_girvan_newman_file = "path/to/girvan_newman_community_results.csv"

main(input_file, threshold=0.7, output_link_file=output_link_file, output_centrality_file=output_centrality_file, output_louvain_file=output_louvain_file, output_girvan_newman_file=output_girvan_newman_file)
```

## Tests du Package

Créez un fichier de test `test_package.py` :

```python
import pandas as pd
import networkx as nx
from your_package import load_similarity_matrix, calculate_centrality_metrics

def test_load_similarity_matrix():
    df = load_similarity_matrix("path/to/test_file.csv")
    assert not df.empty

def test_calculate_centrality_metrics():
    G = nx.Graph()
    G.add_edge("A", "B", weight=0.8)
    centrality_df = calculate_centrality_metrics(G)
    assert not centrality_df.empty

if __name__ == "__main__":
    test_load_similarity_matrix()
    test_calculate_centrality_metrics()
    print("Tous les tests sont passés avec succès!")
```

Exécutez les tests :

```bash
python test_package.py
```

**Sortie attendue :**
```
Tous les tests sont passés avec succès!
```

---

Cette documentation couvre les fonctionnalités principales du package et les étapes pour les tester.

