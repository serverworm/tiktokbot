from selenium import webdriver
from os import system, name
import pyfiglet, threading
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()


def clear():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')


clear()


print(pyfiglet.figlet_format("TIKTOKBOT", font="slant"))
print("👀 1. Viewbot.\n❤ 2. Heartbot (IN DEVELOPMENT)\n👥 3. Followerbot (IN DEVELOPMENT)\n📩 4. Sharebot.\n")

auto = int(input("➡ Select mode: "))

if auto == 1 or auto == 4:
    vidUrl = input("➡ Paste TikTok video URL: ")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1024, 650)


def beautify(arg):
    return format(arg, ',d').replace(',', '.')


def loop1():
    while True:
        try:
            driver.find_element("xpath", "//BUTTON[@type='submit']")
            sleep(1)
        except:
            print("Captcha successfully complete")
            break
    try:
        sleep(2)
        driver.find_element("xpath", "(//BUTTON[@type='button'])[11]").click()
        sleep(2)
        driver.find_element("xpath", "(//INPUT[@type='search'])[4]").send_keys(vidUrl)
        sleep(2)
        driver.find_element("xpath", '/html/body/div[10]/div/form/div/div/button').click()
        sleep(2)
        driver.find_element("xpath", '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
        sleep(2)
        driver.refresh()
        print("✅ Views sended!")

        sleep(170)
        loop1()
    except:
        print("⛔ An error occured. Retrying..")
        driver.refresh()
        loop1()


def loop2():
    print(pyfiglet.figlet_format("⚒ IN DEVELOPMENT", font="slant"))
    input('Press ENTER to exit')


def loop3():
    print(pyfiglet.figlet_format("⚒ IN DEVELOPMENT", font="slant"))
    input('Press ENTER to exit')


def loop4():
    while True:
        try:
            driver.find_element("xpath", "//BUTTON[@type='submit']")
            sleep(5)

        except:
            print("Captcha successfully complete")
            break

    try:
        sleep(2)
        driver.find_element("xpath", "(//BUTTON[@type='button'])[12]").click()
        sleep(1)
        driver.find_element("xpath", "(//INPUT[@type='search'])[5]").send_keys(vidUrl)
        sleep(2)
        driver.find_element("xpath", "/html/body/div[4]/div[6]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element("xpath", "/html/body/div[4]/div[6]/div/div/div[1]/div/form/button").click()
        driver.refresh()
        print("✅ Shares sent!")
        sleep(170)
        loop4()
    except:
        print("⛔ An error occured. Retrying..")
        driver.refresh()
        loop4()
clear()


print("\n\nℹ___INFO___ℹ")
if auto == 1:
    driver.get("https://zefoy.com/")
    threading.Thread(target=loop1).start()

elif auto == 2: threading.Thread(target=loop2).start()
elif auto == 3: threading.Thread(target=loop3).start()

elif auto == 4:
    driver.get("https://zefoy.com/")
    threading.Thread(target=loop4).start()

else:
    print(f"{auto} is not a valid option. Please pick 1, 2, 3, 4 or 5")