from abc import ABC, abstractmethod

# --------------------------------------------------------------------
# CLASE ABSTRACTA: ZOMBIE
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
# CLASES DE ZOMBIE
# --------------------------------------------------------------------
class ZombiePerro(Zombie):
    def __init__(self, salud, velocidad):
        self.salud = salud
        self.velocidad = velocidad

    def ataque(self):
        print("Zombie perro muerde con furia.")

    def hablar(self):
        print("Zombie perro emite un gruñido aterrador.")

    def caminar(self):
        print("Zombie perro se desplaza sobre cuatro patas.")

    # Método extra
    def correr_en_cuatro_patas(self):
        print("Zombie perro corre rápidamente en cuatro patas.")

class ZombieChilango(Zombie):
    def __init__(self, salud, velocidad):
        self.salud = salud
        self.velocidad = velocidad

    def ataque(self):
        print("Zombie chilango ataca lanzando garnachas.")

    def hablar(self):
        print("Zombie chilango dice: '¡La chamba, la chamba!'")

    def caminar(self):
        print("Zombie chilango camina al ritmo de la cumbia.")

    # Método extra
    def lanzar_guajolotas(self):
        print("Zombie chilango lanza guajolotas explosivas a sus víctimas.")

class ZombieFit(Zombie):
    def __init__(self, salud, velocidad):
        self.salud = salud
        self.velocidad = velocidad

    def ataque(self):
        print("Zombie fit hace un ataque con mancuernas.")

    def hablar(self):
        print("Zombie fit gruñe: 'Pro... te... ína...'")

    def caminar(self):
        print("Zombie fit trota con energía.")

    # Método extra
    def correr(self):
        print("Zombie fit corre a toda velocidad para entrenar.")

class ZombieGentrificador(Zombie):
    def __init__(self, salud, velocidad):
        self.salud = salud
        self.velocidad = velocidad

    def ataque(self):
        print("Zombie gentrificador incrementa la renta y ataca tu bolsillo.")

    def hablar(self):
        print("Zombie gentrificador se queja de la falta de opciones gourmet.")

    def caminar(self):
        print("Zombie gentrificador camina con aires de superioridad.")

    # Método extra
    def quejarse_del_ruido(self):
        print("Zombie gentrificador: '¿Podrían bajar el volumen? Estoy tomando mi matcha latte.'")

# --------------------------------------------------------------------
# CLASE ABSTRACTA: METRO
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

    # Métodos que manifiestan la dependencia con Zombie
    @abstractmethod
    def agregar_zombie(self, zombie: Zombie):
        pass

    @abstractmethod
    def remover_zombie(self, zombie: Zombie):
        pass

    @abstractmethod
    def listar_zombies(self):
        pass

# --------------------------------------------------------------------
# CLASE: METRO DE CDMX
# --------------------------------------------------------------------
class MetroDeCdmx(Metro):
    def __init__(self):
        # Almacén de Zombies "dentro" del Metro
        self._zombies = []

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
        print("¡El Metro de la CDMX entra en modo pánico! Los pasajeros entran en caos.")

    def cambiar_via(self):
        print("El Metro de la CDMX cambia de vía.")

    def agregar_zombie(self, zombie: Zombie):
        self._zombies.append(zombie)
        print(f"{type(zombie).__name__} (Salud={getattr(zombie, 'salud', 'N/A')}) se ha subido al Metro.")

    def remover_zombie(self, zombie: Zombie):
        if zombie in self._zombies:
            self._zombies.remove(zombie)
            print(f"{type(zombie).__name__} se ha bajado del Metro.")
        else:
            print("Ese zombie no se encuentra en el Metro.")

    def listar_zombies(self):
        if not self._zombies:
            print("No hay zombies en el Metro.")
        else:
            print("Zombies dentro del Metro:")
            for z in self._zombies:
                print(f" - {type(z).__name__} (Salud={z.salud}, Velocidad={z.velocidad})")

# --------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------
if __name__ == "__main__":
    metro = MetroDeCdmx()
    z_perro = ZombiePerro(salud=50, velocidad=10)
    z_chilango = ZombieChilango(salud=60, velocidad=8)
    z_fit = ZombieFit(salud=80, velocidad=15)
    z_gentri = ZombieGentrificador(salud=70, velocidad=5)

    print("=== PRUEBAS: METRO ===")
    metro.avanzar()
    metro.detenerse()
    metro.abrir_puertas()
    metro.cerrar_puertas()
    metro.anunciar_parada()
    metro.modo_panico()
    metro.cambiar_via()
    print("-" * 40)

    print("=== SUBEN ZOMBIES AL METRO ===")
    metro.agregar_zombie(z_perro)
    metro.agregar_zombie(z_chilango)
    metro.agregar_zombie(z_fit)
    metro.agregar_zombie(z_gentri)
    print("-" * 40)

    print("=== ZOMBIES ABORDO ===")
    metro.listar_zombies()
    print("-" * 40)

    print("=== METODOS DE CADA ZOMBIE ===")
    for z in [z_perro, z_chilango, z_fit, z_gentri]:
        z.ataque()
        z.hablar()
        z.caminar()
        if isinstance(z, ZombiePerro):
            z.correr_en_cuatro_patas()
        elif isinstance(z, ZombieChilango):
            z.lanzar_guajolotas()
        elif isinstance(z, ZombieFit):
            z.correr()
        elif isinstance(z, ZombieGentrificador):
            z.quejarse_del_ruido()
        print("-" * 40)

    print("=== BAJAN ZOMBIES DEL METRO ===")
    metro.remover_zombie(z_perro)
    metro.remover_zombie(z_fit)

    print("=== ZOMBIES RESTANTES ===")
    metro.listar_zombies()
    print("-" * 40)