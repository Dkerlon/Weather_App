from flet import *
from scripts.load_api import load_api_data
from scripts.funcionalidades import clima
more_info_styled = {
    "margin":margin.only(top=10),
    "padding":padding.only(top=5,bottom=5,right=10,left=19),
    "width":290,
    "height":100,
    "border_radius":15,
    "bgcolor":'white10',
}
class More_info(Container):
    def __init__(self):
        super().__init__(**more_info_styled)
        self.pressao_text = clima(1)
        self.vento_text = clima(2)
        self.uv_text = clima(3)
        self.content=Row(
            spacing=15,
            scroll='auto',
            controls=[
                Column(
                    spacing=10,
                    controls=[
                        Row(
                            spacing=3,
                            controls=[
                                Image(src="assets/pressao_at.png",color='white', width=18,height=18),
                                Text('Pressão amanhã',weight=FontWeight.W_600,size=13)
                            ]
                        ),
                        Row(
                            spacing=2,
                            width=245,
                            height=50,
                            vertical_alignment='start',
                            alignment='spaceBetween',
                            controls=[
                                Text(f'{self.pressao_text}',width=160,size=12),
                                Text(f'{load_api_data()["Pressao_Amanha"]}hPa',size=16,weight=FontWeight.BOLD,)
                            ]
                        )
                    ]
                ),

                Column(
                    spacing=10,
                    controls=[
                        Row(
                            spacing=3,
                            controls=[
                                Image(src="assets/pressao.svg",color='white', width=18,height=18),
                                Text(f'Ventos amanhã',weight=FontWeight.W_600,size=13)
                            ]
                        ),
                        Row(
                            spacing=2,
                            width=245,
                            height=50,
                            alignment='spaceBetween',
                            vertical_alignment='start',
                            controls=[
                                Text(f'{self.vento_text}',width=180,size=12),
                                Text(f'{load_api_data()['Vento_Amanha']}ms',size=16,weight=FontWeight.BOLD,)
                            ]
                        )
                    ]
                ),
                Column(
                    spacing=10,
                    controls=[
                        Row(
                            spacing=3,
                            controls=[
                                Image(src="assets/uv.png",color='white', width=18,height=18),
                                Text('Raios UV amanhã',weight=FontWeight.W_600,size=13)
                            ]
                        ),
                        Row(
                            spacing=2,
                            width=245,
                            height=50,
                            vertical_alignment='start',
                            alignment='spaceBetween',
                            controls=[
                                Text(f'{self.uv_text}',width=210,size=12),
                                Text(f'{load_api_data()['Uv_Amanha']}UV',size=16,weight=FontWeight.BOLD,)
                            ]
                        )
                    ]
                )
            ]
        )
    