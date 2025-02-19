# Zombies en el metro de la Ciudad de México
from abc import ABC, abstractmethod

# --------------------------------------------------------------------
# Clase abstracta Zombie
# --------------------------------------------------------------------
class Zombie(ABC):
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
# Clase abstracta Metro
# (todos métodos, sin atributos)
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
# Hijos de la clase Zombie
# --------------------------------------------------------------------
class Zombie_perro(Zombie):
    def ataque(self):
        print("Zombie perro ataca con mordida.")

    def hablar(self):
        print("Zombie perro emite gruñidos.")

    def caminar(self):
        print("Zombie perro corre en cuatro patas.")


class Zombie_fit(Zombie):
    def ataque(self):
        print("Zombie fit hace un ataque con pesas.")

    def hablar(self):
        print("Zombie fit dice: 'Auurrrgh, dame proteínas.'")

    def caminar(self):
        print("Zombie fit trota a un ritmo constante.")


class Zombie_chilango(Zombie):
    def ataque(self):
        print("Zombie chilango lanza guajolotas explosivas.")

    def hablar(self):
        print("Zombie chilango dice: '¡Hora de la garnacha, bro!'")

    def caminar(self):
        print("Zombie chilango camina bailando cumbia.")


class Zombie_gentrificador(Zombie):
    def ataque(self):
        print("Zombie gentrificador sube la renta y ataca tu bolsillo.")

    def hablar(self):
        print("Zombie gentrificador se queja del ruido y pide matcha.")

    def caminar(self):
        print("Zombie gentrificador camina con aires de superioridad.")


# --------------------------------------------------------------------
# Hijos de la clase Metro
# --------------------------------------------------------------------
class MetroCDMXVagon5(Metro):
    def avanzar(self):
        print("El MetroCDMX Vagón 5 avanza sobre la vía.")

    def detenerse(self):
        print("El MetroCDMX Vagón 5 se detiene en la estación.")

    def abrir_puertas(self):
        print("El MetroCDMX Vagón 5 abre sus puertas.")

    def cerrar_puertas(self):
        print("El MetroCDMX Vagón 5 cierra sus puertas.")

    def anunciar_parada(self):
        print("El MetroCDMX Vagón 5 anuncia la siguiente parada.")

    def modo_panico(self):
        print("¡Alerta! El MetroCDMX Vagón 5 entra en modo pánico.")

    def cambiar_via(self):
        print("El MetroCDMX Vagón 5 cambia de vía.")


# --------------------------------------------------------------------
# main para probar
# --------------------------------------------------------------------
if __name__ == "__main__":
    # Instancias de zombies
    z_perro = Zombie_perro()
    z_fit = Zombie_fit()
    z_chilango = Zombie_chilango()
    z_gentri = Zombie_gentrificador()

    # Probamos métodos en cada zombie
    print("=== PRUEBAS ZOMBIES ===")
    for zombie in (z_perro, z_fit, z_chilango, z_gentri):
        zombie.ataque()
        zombie.hablar()
        zombie.caminar()
        print("-" * 40)

    # Instanciamos un metro
    vagon5 = MetroCDMXVagon5()
    print("=== PRUEBAS METRO ===")
    vagon5.avanzar()
    vagon5.detenerse()
    vagon5.abrir_puertas()
    vagon5.cerrar_puertas()
    vagon5.anunciar_parada()
    vagon5.modo_panico()
    vagon5.cambiar_via()