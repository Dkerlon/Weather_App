from scripts.load_api import today,load_api_data
from flet import *
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz

#Cria Colunas de horários dentro de hours.py
def create_column_hours(controls):
    controls.controls = []
    range_min = today[1] + int(get_local_time(load_api_data()['Lat'],load_api_data()['Lon']).split(":")[0])
    range_max = today[2] + int(get_local_time(load_api_data()['Lat'],load_api_data()['Lon']).split(":")[0])
    range_min_image = int(get_local_time(load_api_data()['Lat'],load_api_data()['Lon']).split(":")[0])
    for x in load_api_data()['Horas']:
        image_tempo = images(1,load_api_data()["Umidade_horas"][range_min],range_min_image)
        if range_max < range_min:
                break
        controls.controls.append(
                Column(
                horizontal_alignment='center',
                controls=[
                    Text(f'{load_api_data()['Horas'][range_min].split(" ")[1]}',weight=FontWeight.W_300,size=12),
                    Image(src=f'{image_tempo}',width=27,height=27),
                    Text(f'{int(load_api_data()['Temperatura_horas'][range_min])}°',weight=FontWeight.W_700,size=15),
                    Row(
                        spacing=0,
                        controls=[
                            Image(src='assets/umidade.png',width=12,height=12,color='white',opacity=1),
                            Text(f'{load_api_data()['Umidade_horas'][range_min]}%',weight=FontWeight.W_200,size=12)
                        ]
                    )
                ]
            ),
        )
        range_min+=1
        range_min_image+=1
        if range_min_image > 28:
            range_min_image = 5
#Obtém o horário do local atual
def get_local_time(latitude,longitude):

    tf =TimezoneFinder()
    timezone_str = tf.timezone_at(lat=latitude,lng=longitude)

    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone).strftime("%H:%M")
        return local_time
    else:
        return "Fuso horário não encontrado."
    
#Retorna um texto  para quem está chamada com base no retorno da API
def clima(control):
    if control == 0:
        if load_api_data()["Umidade"] < 60:
            clima = "Limpo"
        elif load_api_data()["Umidade"] > 60 and load_api_data()["Umidade"] < 80:
            clima = "Nublado"
        else:
            clima="Chuvoso"
        return clima
    if control == 1:
        if load_api_data()['Pressao_Amanha'] > 1020:
            pressao_text = 'Pode dificultar a respiração. Hidrate-se e evite esforço excessivo.'
        elif load_api_data()['Pressao_Amanha'] >=1010 and load_api_data()['Pressao_Amanha'] < 1020:
            pressao_text = "Condição normal, mas fique atento a mudanças no tempo."
        else:
            pressao_text = "Pode causar fadiga e indicar chuva. Descanse e acompanhe a previsão."
        return pressao_text
    if control == 2:
        if load_api_data()['Vento_Amanha'] < 2.8:
            vento_text = "Brisa leve, sem riscos. Aproveite o clima."
        elif load_api_data()['Vento_Amanha'] > 2.8 and load_api_data()['Vento_Amanha'] <11.1:
            vento_text = "Pode causar desconforto. Proteja objetos leves."
        else:
            vento_text = "Risco de quedas de galhos e objetos. Evite áreas abertas."
        return vento_text
    if control == 3:
        if load_api_data()['Uv_Amanha'] < 2:
            uv_text = "Risco mínimo, mas óculos de sol podem ajudar."
        elif load_api_data()['Uv_Amanha'] > 3 and load_api_data()['Uv_Amanha'] <7:
            uv_text = "Use protetor solar e evite exposição prolongada."
        else:
            uv_text = "Evite o sol ao meio-dia. Use protetor, chapéu e óculos."
        return uv_text
#Retorna um src com uma imagem para quem está chamada com base no retorno da API
def images(control,Umidade_horas=None,range_min=None):
    if control == 0:
        if load_api_data()["Umidade"] < 60:
            src = "assets/sol.png"
        elif load_api_data()["Umidade"] > 60 and load_api_data()["Umidade"] < 80:
            src = "assets/c.png"
        else:
            src="assets/nuvem_chuvosa.png"
        return src
    elif control == 1:
        if Umidade_horas <= 60 and range_min < 18 and range_min >= 5:
            src = "assets/sol.svg"
        elif Umidade_horas <= 60 and range_min >= 18 and range_min <5:
            src = "assets/lua.svg"
        elif Umidade_horas > 60 and Umidade_horas < 80 and range_min < 18 and range_min >= 5:
            src = "assets/nublado.svg"
        elif Umidade_horas > 60 and Umidade_horas < 80 and range_min >= 18 and range_min < 5:
            src = "assets/lua_nublada.svg"
        elif Umidade_horas >= 80 and range_min < 18 and range_min >= 5:
            src="assets/chuvoso.svg"
        else:
            src="assets/lua_chuvosa.svg"
        return src

#Atualiza toda a página com as informações atuais
def update_all_components(header,hours,more_info,localizations):
    hora_local = get_local_time(load_api_data()['Lat'], load_api_data()['Lon'])
    header.controls[0].controls[1].value = f"{load_api_data()["Nome"]}°" #Nome da cidade
    header.controls[1].content.controls[0].controls[0].value = f"{load_api_data()["Temperatura"]}°" #Temperatura
    header.controls[1].content.controls[0].controls[1].src = f"{images(0)}"
    header.controls[1].content.controls[1].value = f"{clima(0)}" #Clima
    header.controls[1].content.controls[3].controls[0].value = f"{load_api_data()['Temperatura_max']}° / {load_api_data()['Temperatura_min']}° Sensação térmica de {load_api_data()['Sensação_termica']}°" 
    header.controls[1].content.controls[4].value = f'{today[0]}., {hora_local}' 
    hours.content.controls[0].value = f'{clima(0)}. Mínima de {load_api_data() ['Temperatura_min']}°.' #Clima e TempMin
    create_column_hours(hours.content.controls[3])

    more_info.content.controls[0].controls[1].controls[0].value = f'{clima(1)}'
    more_info.content.controls[0].controls[1].controls[1].value = f'{load_api_data()["Pressao_Amanha"]}hPa' #Pressão
    more_info.content.controls[1].controls[1].controls[0].value = f'{clima(2)}'
    more_info.content.controls[1].controls[1].controls[1].value = f'{load_api_data()["Vento_Amanha"]}ms' #Vento
    more_info.content.controls[2].controls[1].controls[0].value = f'{clima(3)}'
    more_info.content.controls[2].controls[1].controls[1].value = f'{load_api_data()["Uv_Amanha"]}UV' #Raios UV

    localizations.content.controls[0].controls[0].controls[1].value = f"{load_api_data()["Nome"]}" #Nome do local
    localizations.content.controls[0].controls[1].controls[0].src = f"{images(0)}"
    localizations.content.controls[0].controls[1].controls[1].value = f"{load_api_data()['Temperatura']}°" #Temperatura
    
    #Alterando o tema do APP com base na hora
    if int(hora_local.split(':')[0]) > 17:
        linearGradient_main_container_color_1 = '#2d2e70'
        linearGradient_main_container_color_2 = '#1d1e54'

        linearGradient_menu_container_color_1 = '#1d1d54'
        linearGradient_menu_container_color_2 = '#1d1e54'
    else:
        linearGradient_main_container_color_1 = 'lightblue500' 
        linearGradient_main_container_color_2 = 'lightblue900'

        linearGradient_menu_container_color_1 = 'lightblue500' 
        linearGradient_menu_container_color_2 = 'lightblue900' 
    header.parent.parent.gradient = LinearGradient(
        begin=alignment.bottom_left,
        end=alignment.top_right,
        colors=[linearGradient_main_container_color_1,linearGradient_main_container_color_2]
    )

    header.parent.parent.parent.controls[0].gradient = LinearGradient(
        begin=alignment.bottom_left,
        end=alignment.top_right,
        colors=[linearGradient_menu_container_color_1,linearGradient_menu_container_color_2]
    )
    header.parent.parent.parent.update()
    