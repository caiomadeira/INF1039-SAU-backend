from playwright.sync_api import sync_playwright, BrowserType
from bs4 import BeautifulSoup
from datetime import date
import subprocess
import os
#from dotenv import load_dotenv
import time

#load_dotenv()

path = 'https://sau.puc-rio.br/WebLoginPucOnline/Default.aspx?sessao=VmluY3Vsbz1BJlNpc3RMb2dpbj1QVUNPTkxJTkVfQUxVTk8mQXBwTG9naW49TE9HSU4mRnVuY0xvZ2luPUxPR0lOJlNpc3RNZW51PVBVQ09OTElORV9BTFVOTyZBcHBNZW51PU1FTlUmRnVuY01lbnU9TUVOVQ__'
#print(os.getenv('USER'), os.getenv('PASSWORD'))

html_ctx: dict = {
    'input_user': 'input#txtLogin',
    'input_password': 'input#txtSenha',
    'submit_btn': 'input[type=submit]',
    'username': '#lblNomeUsuario',
}

def make_login(hide_browser: bool, user: str, password: str):
    try:
        with sync_playwright() as p:
            bw = p.chromium.launch(headless=hide_browser, slow_mo=50)
            pg = bw.new_page()
            pg.goto(path)
            pg.fill(html_ctx['input_user'], user)
            pg.fill(html_ctx['input_password'], password)
            pg.click(html_ctx['submit_btn'])
            error_login = pg.is_visible('div.pnlAlertModalTipoErro')
            print(error_login)
            if error_login:
                print("Erro no login.\n")
            else:
                html = pg.inner_html(html_ctx['username'])
                print(str(html))
                #save_log(html)
                return html

            #sau_goto(pg, 'Horários e salas de aula')
    except Exception as e:
        print("Error: ", e)
        return e
    except BrowserType.launch:
        print("Instaaling playwright")
        os.system("playwright install")
        time.sleep(2)
        return make_login(hide_browser, user, password)

def save_log(text: str):
    with open(f'log_{date.today()}.txt', 'w') as f:
        f.write(text)
    f.close()
    print("Sucess writing log.\n")

def sau_goto(pg, menu_item: str):
    if menu_item == 'Horários e salas de aula':
        pg.get_by_text("Horários e salas de aula").click()
        content = pg.inner_html('#pnlListDisc')
        elemento = getClasses(content)
        for k,v in elemento.items():
            print(f"{k} = {v} \n\n\n")


def getClasses(contentHorarios):
    soup = BeautifulSoup(contentHorarios, 'html.parser')
    classesDict = {}
    for i in range(1,16):
        try:
            codigoTurma = soup.find('span', id=f'rpHorarioSala_ctl0{i}_lblDisciplinaTurmaCod').text
            codigoTurma = codigoTurma.split("/")
            codigo = codigoTurma[0]
            turma = codigoTurma[1]
            nome_disciplina = soup.find('span', id=f'rpHorarioSala_ctl0{i}_lblDisciplinaTurmaNome').text
            horario_sala = soup.find('span', id=f'rpHorarioSala_ctl0{i}_lblDiaHorarioSala').text
            classDict = {"codigo": codigo, "horario": horario_sala, "turma": turma}
            classesDict[nome_disciplina] = classDict
        except:
            break
    return classesDict
 

#make_login(hide_browser=False, user="1921050", password="thelonel")
