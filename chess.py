


from typing import Tuple


class Figure():
    line = 0
    row = 0
    figure_image = {
        'black':{
            'pawn':'path to image', 
            'king':'path to image', 
            'queen':'path to image', 
            'elephant':'path to image',
            'horse':'path to image',
            'rook':'path to image' 
        },
        'white':{
            'pawn':'path to image', 
            'king':'path to image', 
            'queen':'path to image', 
            'elephant':'path to image',
            'horse':'path to image',
            'rook':'path to image' 
        }
    }

    def __init__(self, type:str, color:str)->None:
        """
        При создании класса передаются один из типов фигуры [pow, king, queen, elephant, horse, rook]
        и один из цветов фигуры [black, white] 
        """
        pass

    def move(self, new_position:tuple, have_opponent:bool)->bool:
        """
        Пhоверяет возможен ли ход для данной фигуры
        """
        pass

    def set_position(self, new_position:tuple, have_opponent:bool)->bool:
        """
        Смена позиции или установка фигуры на доску.
        have_opponent проверяет наличие противника на новой позиции (расширяет возможные ходы для пешки)
        """
        if self.move(new_position, have_opponent):
            pass
        

    def get_figure_info(self)->tuple:
        """
        Возвращает кортеж (image, color, position)
        """
        pass

    def __str__(self) -> str:
        return f'{self.color} , {self.type}; position: {self.line}:{self.row}'

