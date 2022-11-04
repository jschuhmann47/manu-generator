from ast import arg
import sys
import webbrowser

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Error en la cantidad de argumentos")
        print("Ejemplo de uso: manu.py manu")
        return
    webbrowser.open("https://www.memegenerator.es/generator.php?id=45&texto1=" + args[0] + "+sos+un&texto2=hijo+de+remil+f&private=1")

if __name__ == "__main__":
    main()