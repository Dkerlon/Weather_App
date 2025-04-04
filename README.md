# ☁️ Weather App - Previsão do Tempo com Python e Flet

Este é um aplicativo de previsão do tempo moderno e responsivo, desenvolvido com [Flet](https://flet.dev) (framework para construir interfaces com Python), com dados fornecidos pela API [Meteoblue](https://www.meteoblue.com/) e localização via [Nominatim](https://nominatim.org/).

O projeto foi inspirado no aplicativo de clima da Samsung, e possui visual dinâmico, informações meteorológicas completas e funcionalidades pensadas para o usuário comum.

---

## 🚀 Funcionalidades

- 🌤️ **Previsão atual detalhada** com temperatura, sensação térmica, umidade e condições do céu.
- 🕓 **Gráfico de horas do dia** com ícones ilustrativos do clima (sol, lua, nublado, chuvoso...).
- 📍 **Geolocalização automática via latitude e longitude**.
- 🎨 **Tema do app muda automaticamente** entre dia e noite com base na hora local.
- 💾 **Locais pesquisados são salvos automaticamente** e carregados ao iniciar o app.
- 📌 **Seleção de locais salvos** via menu suspenso com atualização dinâmica dos dados.
- 📊 **Informações complementares** sobre:
  - Pressão atmosférica
  - Velocidade do vento
  - Índice UV
  - Tradução e interpretação dos dados técnicos em linguagem acessível para o usuário

---

## 🧠 Tecnologias e Bibliotecas Utilizadas

| Tecnologia        | Função no Projeto                                      |
|-------------------|--------------------------------------------------------|
| Python            | Lógica de programação principal                       |
| Flet              | Interface gráfica (UI responsiva e moderna)           |
| datetime / pytz   | Cálculo de horário local com fuso horário             |
| timezonefinder    | Obtenção do fuso com base na latitude/longitude       |
| JSON              | Armazenamento local de cidades pesquisadas            |
| API Meteoblue     | Fonte dos dados meteorológicos                        |
| API Nominatim     | Geocodificação de nome de cidade para coordenadas     |

---

## 📁 Estrutura do Projeto

