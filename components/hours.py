from flet import *
from scripts.load_api import today,load_api_data
from scripts.funcionalidades import get_local_time,create_column_hours
from datetime import datetime
from scripts.funcionalidades import clima,images
hours_styled = {
    "margin":margin.only(top=10),
    "padding":padding.only(top=5,bottom=5,right=10,left=19),
    "width":290,
    "height":160,
    "border_radius":15,
    "bgcolor":'white10',
}

class Hours(Container):
    def __init__(self):
        super().__init__(**hours_styled)
        self.clima = clima(0)
        self.content = Column(
            spacing=3,
            controls=[
                Text(f'{self.clima}. Mínima de {load_api_data()['Temperatura_min']}°.',weight=FontWeight.W_600,size=13),
                Divider(color='white',height=1,opacity=0.2),
                Container(height=5),
                Row(
                    scroll='auto',
                    expand=True,
                    controls=[
                         
                    ]
                )
            ]
        )
        self.colum_1 = create_column_hours(self.content.controls[3])