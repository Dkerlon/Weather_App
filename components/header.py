from flet import *
from scripts.load_api import today,load_api_data
from scripts.funcionalidades import clima,images,get_local_time

class Header(Column):
    def __init__(self):
        super().__init__()
        self.image_0_src = images(0)
        self.clima = clima(0)
        self.menu_press = False
        self.controls=[
                Row(
                    vertical_alignment='center',
                    spacing=10,
                    controls=[
                        IconButton(
                            on_click= lambda e:self._expand(e),
                            content=Image(src='assets/menu_icon.png',width=19,height=19,color='white')
                        ),
                        Text(f'{load_api_data()['Nome']}', weight='bold',font_family='Georgia, serif',size=16)
                    ]
                ),
                Container(
                    padding=padding.only(left=10),
                    content=
                        Column(
                            spacing=5,
                            controls=[
                            Row(
                                width=230,
                                alignment='spaceBetween',
                                controls=[
                                    Text(f'{load_api_data()["Temperatura"]}°', weight='bold',font_family='Georgia, serif',size=45),
                                    Image(src=f'{self.image_0_src}',width=90,height=90)
                                ]
                            ),
                            Text(f"{self.clima}", weight='bold',font_family='Georgia, serif',size=14),
                            Row(height=5),
                            Row(controls=[
                                Text(f"{load_api_data()['Temperatura_max']}° / {load_api_data()['Temperatura_min']}° Sensação térmica de {load_api_data()['Sensação_termica']}°",font_family='Georgia, serif',size=14)
                            ]),
                            Text(f"{today[0]}., {get_local_time(load_api_data()['Lat'],load_api_data()['Lon'])}",font_family='Georgia, serif',size=14)
                        ]
                    )
                )
            ]
    def _expand(self,e):
        
        if not self.menu_press:
            self.parent.parent.right = -250
            self.parent.parent.border_radius = border_radius.only(top_right=35,bottom_right=35,top_left=0,bottom_left=0)
            self.menu_press = True
        else:
            self.parent.parent.right = 0
            self.parent.parent.border_radius = 35
            self.menu_press = False
        self.parent.parent.update()