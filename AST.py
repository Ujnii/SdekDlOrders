from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import keyboard
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver as webdriver


# Блок констант СДЭКа
url_site_on = "https://lk.cdek.ru"
I_login = "login"
I_pass = "parol"
#Login page info
E_login = "/html/body/div[1]/main/div/div/div[1]/form/div[1]/div/div[1]/input"
E_pass = "/html/body/div[1]/main/div/div/div[1]/form/div[2]/div/div[1]/input"
E_proceed = "/html/body/div[1]/main/div/div/div[1]/form/div[4]/button/div/div"
#start order
E_new_order = "/html/body/div[1]/section/div/div[2]/a/span"
#first order page
E_type_of_shipping_main = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[2]/div/div[2]/input"
E_our_role_sender = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[4]/div/div/button[1]"
E_start_place = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[5]/div[1]/div/div/div/input[1]"
I_start_place = "Москва"
E_start_place_choice = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[5]/div[1]/div/div[2]/a[1]"
E_end_place = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[5]/div[2]/div/div/div/input[1]"
# 1 piece of text 
# I_end_place 
E_end_place_choice = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[1]/form/div[5]/div[2]/div/div[2]/a[1]" 
E_to_step2 = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[1]"
#second order page
# перемещение кнопок может сбить настройку - без автозаполнения, перемещения кнопок не будет 
# Если использовать автозаполнение, надо найти кнопку по подписи в ее теле и определить порядок
E_prepare_to_choosing = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/input"
E_prepare_to_choosing2 = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[2]/div[1]/div/input"
E_from_to_info = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[3]/div/a[1]/div/div[1]"
E_to_step3 = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[2]/div/button[1]"
#third order page
E_to_step4 = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[3]/div/button[1]"
E_start_time = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div/input"
E_enter_time = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/ul/li[31]"
#maybe end time need to be modified
#maybe street need to be entered
E_street_of_sender = ""
I_street_of_sender = ""
E_house_number_of_sender = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[3]/div/div/div[2]/input"
I_house_number_of_sender = "д.11 стр.21"
E_room_number_of_sender = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[3]/div/div/div[3]/input"
I_room_number_of_sender = "732"
E_INN_of_sender = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[4]/div/input"
I_INN_of_sender = "7733356071"
E_name_of_sender = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[5]/div/input"
I_name_of_sender = "Евгений"
E_phone_of_sender = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[6]/div[1]/div/div/input"
I_phone_of_sender = "79773391947"
#polovina klienta
E_type_of_receiver = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[1]/div/div[2]/input"
E_organisation_name = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[2]/div/div[1]/div[1]/div/input[1]"
# 2 piece of text
# I_organisation_name
E_street_of_receiver = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[3]/div/div/div[1]/div[1]/div/div/input[1]"
#
# I_street_of_receiver 
E_house_number_of_receiver = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[3]/div/div/div[2]/input"
#
# I_house_number_of_receiver 
E_room_number_of_receiver = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[3]/div/div/div[3]/input"
#
# I_room_number_of_receiver 
E_INN_of_receiver = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[4]/div/input"
#
I_INN_of_receiver = "7733356071"
E_name_of_receiver = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[5]/div/input"
#
# I_name_of_receiver 
E_phone_of_receiver = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[2]/div[6]/div[1]/div/div/input"
#
# I_phone_of_receiver 
E_to_step5 = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/div/button[1]"
#new page
E_create_id = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[1]/div[1]/div/div/a"
E_dop_percent1 = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[2]/div[1]/div/div/input"
I_dop_percent1 = "0"
E_dop_percent2_click = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[4]/div[1]/select"

E_place_field_id = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[8]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/input[1]"
I_place_field_id = "-"
E_place_field_name = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[8]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/input[1]"
I_place_field_name = "-"
E_place_field_price = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[8]/div[2]/div[2]/div[1]/div[4]/input"
I_place_field_price = "100"
E_place_field_weight = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[8]/div[2]/div[2]/div[2]/div[1]/input"
I_place_field_weight = "0,1"
E_place_field_count = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[8]/div[2]/div[2]/div[2]/div[2]/input"
I_place_field_count = "1"
E_place_field_payment = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[8]/div[2]/div[2]/div[2]/div[3]/input"
I_place_field_payment = "0"
E_place_field_NDS_click = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[5]/form/div[8]/div[2]/div[2]/div[2]/div[4]/select"
E_to_step6 = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[6]/div/button[1]"

E_finish_order = "/html/body/div[1]/div[1]/main/div[2]/div[2]/div[2]/div[2]/div[7]/div/button[1]"








##########################

url_site_on2 = "https://www.dellin.ru/"
E_login_button2 = "/html/body/div[1]/header/div/div/div/div[1]"
E_login2 = "/html/body/div[1]/header/div/div/div[2]/div[2]/div/form/div[1]/div/input"
I_login2 = "login"
E_pass2 = "/html/body/div[1]/header/div/div/div[2]/div[2]/div/form/div[2]/div/input"
I_pass2 = "parol"
E_login_finish2 = "/html/body/div[1]/header/div/div/div[2]/div[2]/div/form/button"

E_start_place2 = "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/form/div[1]/div[1]/input"
I_start_place2 = "Москва"
E_start_place_choice2 = "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/form/div[1]/div[1]/div/div[1]/p"
E_end_place2 = "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/form/div[1]/div[2]/input"
E_end_place_choice2 = "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/form/div[1]/div[2]/div/div[1]/p"
E_next_step = "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/form/button[3]/span"
E_type_of_things = "/html/body/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div[7]/div[1]/div/span[2]/a[1]"
E_from_adress = "/html/body/div[2]/div/div[2]/div/div/form/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[2]/label/input"
E_saved_adresses = "/html/body/div[2]/div/div[2]/div/div/form/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/a"
E_field_of_adresses = "/html/body/div[2]/div/div[2]/div/div/form/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/input"
I_adress_of_sender = "Золото"
E_adress_of_sender_choice = "/html/body/div[2]/div/div[2]/div/div/form/div[1]/div[5]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/ul/li[2]"
E_


def register_in_systems(browser):
	
	# Регистрация в ДЛ
	
	browser.get(url_site_on2)
	time.sleep(2)
	browser.find_element(by ="xpath", value=E_login_button2).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_login2).send_keys(I_login2)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_pass2).send_keys(I_pass2)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_login_finish2).click()
	time.sleep(3)
	
	# Регистрация в СДЭКе
	
	browser.get(url_site_on)
	time.sleep(2)
	browser.find_element(by ="xpath", value=E_login).send_keys(I_login)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_pass).send_keys(I_pass)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_proceed).click()
	time.sleep(3)
	
	
def dellin_order(browser, file):

	I_end_place2 = file.readline()

	browser.get(url_site_on2)
	time.sleep(4)
	#
	browser.find_element(by ="xpath", value=E_start_place2).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_start_place2).clear()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_start_place2).send_keys(I_start_place2)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_start_place_choice2).click()
	time.sleep(1)
	#
	browser.find_element(by ="xpath", value=E_end_place2).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_end_place2).clear()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_end_place2).send_keys(I_end_place2)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_end_place_choice2).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_next_step).click()
	time.sleep(1)
	#
	# @!@#!@$@$!@$!$
	browser.current_url
	browser.close()
	time.sleep(1)
	browser.switch_to.window(browser.window_handles[0])
	time.sleep(2)
	browser.find_element(by ="xpath", value=E_type_of_things).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_from_adress).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_saved_adresses).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_field_of_adresses).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_field_of_adresses).send_keys(I_adress_of_sender)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_adress_of_sender_choice).click()
	time.sleep(1)

	
	


def sdek_order(browser, file):
	# Новый заказ СДЭК
	I_end_place = file.readline().strip()
	I_room_number_of_sender 
	I_organisation_name = file.readline().strip()
	I_street_of_receiver = file.readline().strip()
	I_house_number_of_receiver = file.readline().strip()
	I_room_number_of_receiver = file.readline().strip()
	I_name_of_receiver = file.readline().strip()
	I_phone_of_receiver = file.readline().strip()
	browser.get(url_site_on)
	time.sleep(3)
	browser.find_element(by ="xpath", value=E_new_order).click()
	time.sleep(5)
	# 
	browser.find_element(by ="xpath", value=E_start_place).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_start_place).clear()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_start_place).send_keys(I_start_place)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_start_place_choice).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_end_place).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_end_place).clear()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_end_place).send_keys(I_end_place)
	time.sleep(2)
	browser.find_element(by ="xpath", value=E_end_place_choice).click()
	time.sleep(1)
	#
	browser.find_element(by ="xpath", value=E_to_step2).click()
	time.sleep(1)
	# By smth search of element
	# Вместо поиска по инфе, уборка иных вариков и жесткое ограничение по количеству, вопрос в автозаполнении этого выбора
	browser.find_element(by ="xpath", value=E_prepare_to_choosing).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_prepare_to_choosing2).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_from_to_info).click()
	#spisok = browser.find_element(By.CSS_SELECTOR, '[name="b"]').click()
	#print(spisok)
	time.sleep(1)
	#
	browser.find_element(by ="xpath", value=E_to_step3).click()
	time.sleep(1)
	#
	browser.find_element(by ="xpath", value=E_to_step4).click()
	time.sleep(1)
	# if time more than 15 or 16 go to next date or smth
	browser.find_element(by ="xpath", value=E_start_time).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_enter_time).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_house_number_of_sender).clear()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_house_number_of_sender).send_keys(I_house_number_of_sender)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_room_number_of_sender).clear()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_room_number_of_sender).send_keys(I_room_number_of_sender)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_INN_of_sender).clear()
	time.sleep(0.1)
	browser.find_element(by ="xpath", value=E_INN_of_sender).send_keys(I_INN_of_sender)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_name_of_sender).clear()
	time.sleep(0.1)
	browser.find_element(by ="xpath", value=E_name_of_sender).send_keys(I_name_of_sender)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_phone_of_sender).click()
	time.sleep(1)
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	keyboard.press_and_release('backspace')
	browser.find_element(by ="xpath", value=E_phone_of_sender).send_keys(I_phone_of_sender)
	time.sleep(1)
	#polovina klienta 
	browser.find_element(by ="xpath", value=E_type_of_receiver).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_organisation_name).send_keys(I_organisation_name)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_street_of_receiver).send_keys(I_street_of_receiver)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_house_number_of_receiver).send_keys(I_house_number_of_receiver)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_room_number_of_receiver).clear()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_room_number_of_receiver).send_keys(I_room_number_of_receiver)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_INN_of_receiver).send_keys(I_INN_of_receiver)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_name_of_receiver).send_keys(I_name_of_receiver)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_phone_of_receiver).send_keys(I_phone_of_receiver)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_to_step5).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_create_id).click()
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_dop_percent1).send_keys(I_dop_percent1)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_dop_percent2_click).click()
	time.sleep(1)
	keyboard.press_and_release('down')
	keyboard.press_and_release('down')
	keyboard.press_and_release('enter')
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_place_field_id).send_keys(I_place_field_id)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_place_field_name).send_keys(I_place_field_name)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_place_field_price).send_keys(I_place_field_price)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_place_field_weight).send_keys(I_place_field_weight)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_place_field_count).send_keys(I_place_field_count)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_place_field_payment).send_keys(I_place_field_payment)
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_place_field_NDS_click).click()
	time.sleep(1)
	keyboard.press_and_release('down')
	keyboard.press_and_release('down')
	keyboard.press_and_release('enter')
	time.sleep(1)
	browser.find_element(by ="xpath", value=E_to_step6).click()
	time.sleep(1)
	#browser.find_element(by ="xpath", value=E_finish_order).click()
def start_run():

	# Запустить браузер и открыть кабинет сдека
	browser = webdriver.Chrome()
	time.sleep(5)
	#
	register_in_systems(browser)
	file = open("ast_atributes.txt", "r")
	qualifier = file.readline().strip().lower()
	while(qualifier != "end") :

		qualifier = file.readline().strip().lower()
		if qualifier == "сдэк" :
			# SDEK ORDER 
			sdek_order(browser,file)
			time.sleep(4)
		if qualifier == "дл" :
			# DL ORDER
			dellin_order(browser,file)
			time.sleep(4)


	file.close()
	browser.close()
	

# pomenat knopku nov zakaza

def main():
    start_run()
    
if __name__ == '__main__':
    main()

