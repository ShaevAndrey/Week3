class Map:
    """
    __road_signs=[
            {
            position:'координаты знака',
            sign:'экземпляр объекта знака'
            },
        ]
    """
    
    
    def __init__(self, map_image) -> None:
        self.__map_image=map_image
        self.__road_signs=list()

    def draw_map(self)->None:
        """ Метод отрисовывает карту для пользователя """
        pass 

    def check_sign(self, coordinates):
        """ Метод возвращает знаки по заданной координате """
        pass
    
    def add_sign(self, sign, coordinates)->None:
        """ Добавляем знак на карту по координатам. Получает название  знака и координатыю
        Далее создаёт экземпляр Sign и добавляет его в __road_signs
        """
        pass

    def remove_sign(self, coordinates, sign_name)->None:
        """ Метод удаляет знак с карты. Получает название знака и координаты  """
        pass

    def change_sign(self, coordinates, old_sign, new_sign):
        """
        Вызывает change_sign у знака по координатам и меняет его значение на new_sign
        """
        pass
    
    def change_or_add_sign_features(self, action, data):
        """
        Вызывает hange_sign_features или add_new_sign у класса Sign и в зависимости от action либо изменяет
        знак, либо добавляет новый
        """
        pass




class Sign:
    
    signs = {
        'STOP':{
            'description':'описание знака',
            'image':'изображение знака',
            'category':'категория знака (запрещающий и т.п.)',
            'fine':'штраф'
        },
        # ...
    }
    def __init__(self, name) -> None:
        """
        Сохраняем имя, как ключ словаря. В последствии находим нужные данные по ключу.
        """
        self.name = name
     
    def create_note(self,note):
        """
        Добавляет заметку к знаку. 
        Например что знак временный, или работает только во время нападения бурундуков) 
        """
        pass

    def change_sign(self, new_sign):
        """
        Заменяет тип знака на другой 
        (наверное так удобнее, если в карте надо заменить знакб тогда не будет дополнительной работы с массивом)
        """
    
    @classmethod
    def change_sign_features(cls, data):
        """
        Изменяет переменную класса signs. Например еслт поменядся штраф за знак, то просто в соотвествии с data
        изменяет параметр, для изменения всех экземпляров класса. 
        """
        pass
    
    @classmethod
    def add_new_sign(cls, data):
        """
        Изменяет переменную класса signs. Например еслт поменядся штраф за знак, то просто в соотвествии с data
        изменяет параметр, для изменения всех экземпляров класса. 
        """
        pass