#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
	   
   def getVehicle(self):
      vehicle = Vehicle()
      
      # Primero el body
      body = self.__builder.getBody()
      vehicle.setBody(body)
      
      # Luego las turbinas
      engine = self.__builder.getEngine()
      vehicle.setEngine(engine)
      
      # Luego las alas
      wings = self.__builder.getWings()
      vehicle.setWings(wings)
      
      # Finalmente el tren de aterrizaje
      landing_gear = self.__builder.getLandingGear()
      vehicle.setLandingGear(landing_gear)

      # Retorna el avión completo
      return vehicle

#*----------------------------------------------------------------
#* Esta es la definición de un objeto vehiculo inicializando 
#* todos sus atributos
#*----------------------------------------------------------------
class Vehicle:
   def __init__(self):
      self.__wings = list()
      self.__engine = None
      self.__body = None
      self.__landing_gear = None

   def setBody(self, body):
      self.__body = body

   def setEngine(self, engine):
      self.__engine = engine

   def setWings(self, wings):
      self.__wings.append(wings)

   def setLandingGear(self, landing_gear):
      self.__landing_gear = landing_gear

   def specification(self):
      print ("Cuerpo: %s" % (self.__body.shape))
      print ("Turbinas: %d" % (self.__engine.turbines))
      print ("Alas: %d" % (len(self.__wings)))
      print ("Tren de aterrizaje: %s" % (self.__landing_gear.type))

#*-----------------------------------------------------------------
#* Builder
#* Clase genérica que solo define la interfaz de los métodos que el
#* Builder específico tiene que implementar
#*-----------------------------------------------------------------
class Builder:
	
      def getBody(self): pass
      def getEngine(self): pass
      def getWings(self): pass
      def getLandingGear(self): pass

#*-----------------------------------------------------------------
#* Esta es la hoja de ruta para construir un avión
#* Establece instancias para tomar cuerpo, turbinas, alas y tren de
#* aterrizaje estableciendo las partes específicas que (en un avión) 
#* deben tener esas partes
#*-------------------------------------------------------
class AirplaneBuilder(Builder):
   
   def getBody(self):
      body = Body()
      body.shape = "Avión"
      return body
   
   def getEngine(self):
      engine = Engine()
      engine.turbines = 2
      return engine
   
   def getWings(self):
      wing = Wing()
      return wing
   
   def getLandingGear(self):
      landing_gear = LandingGear()
      landing_gear.type = "Plegable"
      return landing_gear

#*----------------------------------------------------------------
#* Define partes genéricas para un vehiculo (sin inicializar)
#*----------------------------------------------------------------
class Engine:
   turbines = None

class Body:
   shape = None

class Wing:
   pass

class LandingGear:
   type = None

#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* Esta es la estructura main()
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
def main():

#*----------------------------------------------------------------
#* Instancia la clase que será el resultado y la que guiará el 
#* proceso de construcción
#*----------------------------------------------------------------
   airplaneBuilder = AirplaneBuilder()
   director = Director()

#*----------------------------------------------------------------
#* Pasa al director la hoja de ruta para construir un Avión
#*----------------------------------------------------------------   
   director.setBuilder(airplaneBuilder)

#*----------------------------------------------------------------
#* Ordena al director agregar los componentes de un Avión según
#* la hoja de ruta
#*----------------------------------------------------------------
   airplane = director.getVehicle()

#*---------------------------------------------------------------
#* Finalizada la construcción verifica que sea completa
#*---------------------------------------------------------------
   airplane.specification()
   print ("\n\n")

#*----------------------------------------------------------------------
#* Se detecta el entry point y se lo deriva a una sección main() propia
#*----------------------------------------------------------------------
if __name__ == "__main__":
   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")

   main()
