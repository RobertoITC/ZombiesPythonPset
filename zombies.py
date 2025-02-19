from abc import ABC, abstractmethod

# --------------------------------------------------------------------
# 1. CLASE ABSTRACTA ZOMBIE
#    (con atributos Salud y Velocidad y métodos abstractos)
# --------------------------------------------------------------------
class Zombie(ABC):
    def __init__(self, salud, velocidad):
        self.salud = salud
        self.velocidad = velocidad

    @abstractmethod
    def ataque(self):
        pass

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def caminar(self):
        pass


# --------------------------------------------------------------------
# 2. CLASES HIJAS DE ZOMBIE
#    Cada uno implementa los métodos abstractos
#    y define un método nuevo propio.
# --------------------------------------------------------------------
class Zombie_perro(Zombie):
    def ataque(self):
        print("Zombie perro muerde con furia.")

    def hablar(self):
        print("Zombie perro emite un gruñido aterrador.")

    def caminar(self):
        print("Zombie perro se desplaza sobre cuatro patas.")

    # Método nuevo
    def correr_en_cuatro_patas(self):
        print("Zombie perro corre rápidamente en cuatro patas.")


class Zombie_chilango(Zombie):
    def ataque(self):
        print("Zombie chilango ataca lanzando garnachas.")

    def hablar(self):
        print("Zombie chilango dice: '¡La chamba, la chamba!'")

    def caminar(self):
        print("Zombie chilango camina al ritmo de la cumbia.")

    # Método nuevo
    def lanzar_guajolotas(self):
        print("Zombie chilango lanza guajolotas explosivas a sus víctimas.")


class Zombie_fit(Zombie):
    def ataque(self):
        print("Zombie fit hace un ataque con mancuernas.")

    def hablar(self):
        print("Zombie fit gruñe: 'Pro... te... ína...'")

    def caminar(self):
        print("Zombie fit trota con energía.")

    # Método nuevo
    def correr(self):
        print("Zombie fit corre a toda velocidad para entrenar.")


class Zombie_gentrificador(Zombie):
    def ataque(self):
        print("Zombie gentrificador incrementa la renta y ataca tu bolsillo.")

    def hablar(self):
        print("Zombie gentrificador se queja de la falta de opciones gourmet.")

    def caminar(self):
        print("Zombie gentrificador camina con aires de superioridad.")

    # Método nuevo
    def quejarse_del_ruido(self):
        print("Zombie gentrificador: '¿Podrían bajar el volumen? Estoy tomando mi matcha latte.'")


# --------------------------------------------------------------------
# 3. CLASE ABSTRACTA METRO
#    (solo métodos abstractos, sin atributos)
# --------------------------------------------------------------------
class Metro(ABC):
    @abstractmethod
    def avanzar(self):
        pass

    @abstractmethod
    def detenerse(self):
        pass

    @abstractmethod
    def abrir_puertas(self):
        pass

    @abstractmethod
    def cerrar_puertas(self):
        pass

    @abstractmethod
    def anunciar_parada(self):
        pass

    @abstractmethod
    def modo_panico(self):
        pass

    @abstractmethod
    def cambiar_via(self):
        pass


# --------------------------------------------------------------------
# 4. CLASE CONCRETA: METRO DE LA CDMX
# --------------------------------------------------------------------
class MetroDeCdmx(Metro):
    def avanzar(self):
        print("El Metro de la CDMX avanza hacia la siguiente estación.")

    def detenerse(self):
        print("El Metro de la CDMX se detiene en la estación.")

    def abrir_puertas(self):
        print("El Metro de la CDMX abre sus puertas.")

    def cerrar_puertas(self):
        print("El Metro de la CDMX cierra sus puertas.")

    def anunciar_parada(self):
        print("El Metro de la CDMX anuncia la siguiente parada.")

    def modo_panico(self):
        print("¡El Metro de la CDMX entra en modo pánico! Todo se vuelve un caos.")

    def cambiar_via(self):
        print("El Metro de la CDMX cambia de vía.")


# --------------------------------------------------------------------
# 5. CLASE ABSTRACTA VAGON
# --------------------------------------------------------------------
class Vagon(ABC):
    @abstractmethod
    def abrir_puertas(self):
        pass

    @abstractmethod
    def cerrar_puertas(self):
        pass

    @abstractmethod
    def prender_luces(self):
        pass

    @abstractmethod
    def apagar_luces(self):
        pass


# --------------------------------------------------------------------
# 6. CLASE CONCRETA: VAGON DE PASAJEROS
# --------------------------------------------------------------------
class VagonPasajeros(Vagon):
    def abrir_puertas(self):
        print("Vagón de pasajeros abre sus puertas.")

    def cerrar_puertas(self):
        print("Vagón de pasajeros cierra sus puertas.")

    def prender_luces(self):
        print("Vagón de pasajeros enciende las luces.")

    def apagar_luces(self):
        print("Vagón de pasajeros apaga las luces.")


# --------------------------------------------------------------------
# 7. MAIN: DEMOSTRACIÓN
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Crear instancias de cada tipo de Zombie
    z_perro = Zombie_perro(salud=50, velocidad=10)
    z_chilango = Zombie_chilango(salud=60, velocidad=8)
    z_fit = Zombie_fit(salud=80, velocidad=15)
    z_gentri = Zombie_gentrificador(salud=70, velocidad=5)

    # Probar métodos de cada Zombie
    print("=== PRUEBAS: ZOMBIES ===")
    zombies = [z_perro, z_chilango, z_fit, z_gentri]
    for zombie in zombies:
        zombie.ataque()
        zombie.hablar()
        zombie.caminar()

        # Llamar el método especial de cada Zombie
        if isinstance(zombie, Zombie_perro):
            zombie.correr_en_cuatro_patas()
        elif isinstance(zombie, Zombie_chilango):
            zombie.lanzar_guajolotas()
        elif isinstance(zombie, Zombie_fit):
            zombie.correr()
        elif isinstance(zombie, Zombie_gentrificador):
            zombie.quejarse_del_ruido()

        print("-" * 40)

    # Crear y probar un Metro
    print("=== PRUEBAS: METRO ===")
    metro = MetroDeCdmx()
    metro.avanzar()
    metro.detenerse()
    metro.abrir_puertas()
    metro.cerrar_puertas()
    metro.anunciar_parada()
    metro.modo_panico()
    metro.cambiar_via()
    print("-" * 40)

    # Crear y probar un Vagon
    print("=== PRUEBAS: VAGON ===")
    vagon = VagonPasajeros()
    vagon.abrir_puertas()
    vagon.cerrar_puertas()
    vagon.prender_luces()
    vagon.apagar_luces()
    print("-" * 40)