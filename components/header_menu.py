from flet import *
from scripts.load_api import fetch_api_location
from scripts.funcionalidades import update_all_components
header_menu_styled = {
    "width":230,
    "alignment":'end',
    "vertical_alignment":'center',
    "spacing":1,
}
class Header_menu(Row):
    def __init__(self,header,hours,more_info,localizations):
        super().__init__(**header_menu_styled)
        self.header = header
        self.hours = hours
        self.more_info = more_info
        self.localizations = localizations
        self.clicked = False
        self.location_value = TextField(
            animate_opacity=animation.Animation(150, curve=AnimationCurve.DECELERATE),
            animate_scale=animation.Animation(150, curve=AnimationCurve.DECELERATE),
            opacity=0,
            scale=0.8,
            text_size=14,
            cursor_height=10,
            width=140,
            height=40,
            expand=True,
            border_color='white12',
            border_radius=35,
            text_align=TextAlign.RIGHT,
            hint_text='Pesquisar',
        )
        self.search_menu = Row(
                spacing=5,
                width=220,
                alignment='end',
                vertical_alignment='center',
                height=50,
                controls=[
                    self.location_value,Row(
                        spacing=0,
                        controls=[
                            IconButton(
                                on_click= lambda e:self.load_fetch_api_location(e),
                                content=Image(
                                src='assets/search.png',
                                width=20,
                                height=20,
                                color='white',
                                )
                            ),IconButton(
                                    content=Image(
                                    src='assets/settings.png',
                                    width=20,
                                    height=20,
                                    color='white'
                                )
                            )       
                        ]
                    )
            ],
        )
        self.controls=[
            Container(
                on_hover=lambda _e:self.view_searchTextField(self.clicked),
                content=self.search_menu
            )
        ]
    def view_searchTextField(self,e):
        if self.clicked == False:
            self.location_value.opacity = 1 
            self.location_value.scale = 1
            self.clicked = True
        else:
            self.location_value.opacity = 0
            self.location_value.scale = 0.8 
            self.clicked = False
        self.location_value.update()
    def load_fetch_api_location(self,e):
        if self.location_value.value:
            fetch_api_location(self.location_value.value)
            update_all_components(self.header,self.hours,self.more_info,self.localizations)
        self.location_value.focus()
        self.location_value.value = ''