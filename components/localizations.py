from flet import *
from scripts.load_api import load_api_data
from scripts.funcionalidades import images

localizations_styled = {
    "width":230,
    "padding":padding.only(15,0,15,0)
}
class Localizations(Container):
    def __init__(self):
        super().__init__(**localizations_styled)
        self.content = Column(
            controls=[
                    Row(
                    alignment='spaceBetween',
                    controls=[
                        Row(
                            vertical_alignment='center',
                            spacing=7,
                            controls=[
                                Image(src='assets/localização.png',color='white',width=17,height=17),
                                Text(f"{load_api_data()['Nome']}",weight=FontWeight.BOLD,size=14,font_family='Georgia, serif')
                            ]
                        ),
                        Row(
                            vertical_alignment='center',
                            spacing=7,
                            controls=[
                                Image(src=f'{images(0)}',color='white',width=17,height=17),
                                Text(f"{load_api_data()['Temperatura']}°",weight=FontWeight.BOLD,size=14,font_family='Georgia, serif')
                            ]
                        ),
                    ]
                ),
                Divider(
                height=1,
                color="white12",
                thickness=1,
                opacity=1,
                ) 
            ]
        )
    """Container(
                    padding=20,
                    content=Row(
                        alignment='spaceBetween',
                        controls=[
                            Row(
                                vertical_alignment='center',
                                spacing=7,
                                controls=[
                                    Text(f"{local_home['City']}",weight=FontWeight.W_600,size=13,font_family='Georgia, serif')
                                ]
                            ),
                            Row(
                                vertical_alignment='center',
                                spacing=7,
                                controls=[
                                    Image(src='assets/chuvoso.svg',color='white',width=17,height=17),
                                    Text(f"25°",weight=FontWeight.BOLD,size=13,font_family='Georgia, serif')
                                ]
                            ),
                        ]
                    )
                )"""