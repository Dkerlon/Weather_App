from flet import *
from components.header import Header
from components.hours import Hours
from components.more_info import More_info
from components.header_menu import Header_menu
from components.localizations import Localizations
from datetime import datetime

def main(page:Page):
    hora_atual = datetime.now().strftime("%H")
    linearGradient_main_container_color_1 = 'lightblue500' 
    linearGradient_main_container_color_2 = 'lightblue900' 

    linearGradient_menu_container_color_1 = 'lightblue500' 
    linearGradient_menu_container_color_2 = 'lightblue900' 
    if int(hora_atual) > 17:
        linearGradient_main_container_color_1 = '#2d2e70'
        linearGradient_main_container_color_2 = '#1d1e54'
    if int(hora_atual) > 17:
        linearGradient_menu_container_color_1 = '#1d1d54'
        linearGradient_menu_container_color_2 = '#1d1e54'
    page.title = "WeatherApp"
    page.vertical_alignment="center"
    page.horizontal_alignment="center"

    #Componentes Main Container
    header = Header()
    hours = Hours()
    more_info = More_info()
    
    #Componentes Menu Container
    localizations = Localizations()
    header_menu = Header_menu(header,hours,more_info,localizations)
    #Containers Principais
    main_container = Container(
        animate_position=animation.Animation(duration=550,curve="decelerate"),animate=animation.Animation(duration=550,curve="decelerate"),
        right= 0,
        width=310,
        height=550,
        border_radius=35,
        padding=15,
        gradient=LinearGradient(
        begin=alignment.bottom_left,
        end=alignment.top_right,
        colors=[linearGradient_main_container_color_1,linearGradient_main_container_color_2]
        ),
        content=Column(
            controls=[
                header,
                hours,
                more_info
            ]
        )
    )
    menu_container =Container(
        animate=animation.Animation(duration=700,curve="decelerate"),
        width=305,
        height=550,
        border_radius=35,
        padding=padding.only(15,10,15,10),
        gradient=LinearGradient(
        begin=alignment.bottom_left,
        end=alignment.top_right,
        colors=[linearGradient_menu_container_color_1,linearGradient_menu_container_color_2]
        ),
        content=Container(
            border_radius=35,
            padding=padding.only(5,0,5,0),
                gradient=LinearGradient(
                        begin=alignment.bottom_left,
                        end=alignment.top_right,
                        colors=["white10","white12"]
                    ),
                content=Column(
                controls=[
                    header_menu,
                    Container(height=5),
                    localizations
                ]
            )
        )
    )
    
    _C = Container(
        width=320,
        height=560,
        border_radius=35,
        bgcolor='black',
        padding=5,
        content=Stack(
            controls=[
                menu_container,
                main_container,
            ]
        )
    )
    page.add(_C)

app(target=main,assets_dir='assets')