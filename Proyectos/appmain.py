# appmain.py
from grafos_dirigidos import Grafo

def main():
    print("=== Grafo Dirigido ===")
    g_dir = Grafo(dirigido=True)
    g_dir.agregar_arista("A", "B")
    g_dir.agregar_arista("A", "C")
    g_dir.agregar_arista("B", "C")
    g_dir.mostrar()

    print("\n=== Grafo No Dirigido ===")
    g_no_dir = Grafo(dirigido=False)
    g_no_dir.agregar_arista("A", "B")
    g_no_dir.agregar_arista("A", "C")
    g_no_dir.agregar_arista("B", "C")
    g_no_dir.mostrar()

if __name__ == "__main__":
    main()
