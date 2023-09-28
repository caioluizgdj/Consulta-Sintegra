import pyautogui 
import time

cnpj = "77044618000188"
estado = "PR"

pyautogui.PAUSE = 0.5

#pyautogui.click => NECESSIDADE DE SE ADEQUAR A RESOLUÇÃO DA MÁQUINA QUE EXECUTA

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dfe-portal.svrs.rs.gov.br/NFE/CCC")
pyautogui.press("enter")
pyautogui.click(x=257, y=701) # entra na seleção de sigla do estado
if estado == "PR":
    pyautogui.write("pr") 
    pyautogui.press("enter")
    pyautogui.click(x=484, y=956) # campo para preeencher com cnpj
    pyautogui.write(cnpj)
    pyautogui.scroll(-250)
    pyautogui.click(x=203, y=902) # TALVEZ PEÇA O CAPTCHA (FAZER TRATAMENTO)
    pyautogui.click(x=943, y=643) 
    pyautogui.mouseDown(x=479, y=886)
    pyautogui.moveTo(x=577, y=886)
    pyautogui.mouseUp()
    #pyautogui.hotkey('ctrl', 'c')
    #pyautogui.press("win")
    #pyautogui.hotkey('ctrl', 'v')