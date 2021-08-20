3.1. Сделайте в своём коде три примера наглядных методов-фабрик.
3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы, напишите несколько примеров их правильного именования.

class figure # родительский класс геометрических фигур
class triangle_model(figure) # классы-наследник
class circle_model(figure)

class figure_factory # класс-фабрика
class triangle(figure_factory) # интерфейс создания треугольника
class circle(figure_factory) # интерфейс создания круга


class NPC # родительский класс персонажей
class dwarf_impl(NPC) # реализация класса гномов
class orc_impl(NPC) # реализация класса орков

class NPC_Factory
class dwarf(NPC_Factory) 
class orc(NPC_Factory) 


class transport
class car_dummy(transport)
class moto_dummy(transport)

class transport_factory
class car(transport_factory)
class moto(transport_factory)