from Pelicula import Pelicula
from Catalogo import Catalogo

def main():
    peliculas = [
        Pelicula("El Padrino", "Francis Ford Coppola", 1972),
        Pelicula("El Caballero Oscuro", "Christopher Nolan", 2008),
        Pelicula("Pulp Fiction", "Quentin Tarantino", 1994)
    ]
    
    catalogo = Catalogo()
    catalogo.mostrar_catalogo()
    
    

if __name__ == "__main__":
    main()