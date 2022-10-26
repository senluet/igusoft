import time

import requests
import json
from re import findall

def get_data():
    with open('source.txt', 'r') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            wallet = line.split(';')[0]
            tg_nick = line.split(';')[1]
            twitter_nick = line.split(';')[2]
            proxies = line.split(';')[3]
            proxy = {'https': proxies}
            ds_token = line.split(';')[4]
            ref_link = line.split(';')[5]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "DNT": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1"
            }
            response = requests.get(ref_link, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get('https://iguverse.com/whitelist-free-mint-login', headers=headers_for_igu, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            dis_ap = findall('discord_application=(.*?),', str(response.headers))[0]
            client_id = findall('client_id=(.*?)&', str(response.text))[0]
            headers = {
                "accept": "*/*",
                "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "authorization": ds_token,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Content-Type": "application/json"
            }
            apilink = "https://discord.com/api/v9/oauth2/authorize?" \
                      f"client_id={client_id}" \
                      "&response_type=code" \
                      "&redirect_uri=https://iguverse.com/discord/callback" \
                      "&scope=identify email guilds"
            body = {"permissions":"0","authorize":"true"}
            data = json.dumps(body)
            response = requests.post(apilink, headers=headers, data=data, proxies=proxy)
            location = findall('": "(.*?)"', response.text)[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get(location, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get('https://iguverse.com/whitelist-free-mint', headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get('https://iguverse.com/whitelist-free-mint-verify', headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            location = 'https://iguverse.com/whitelist-free-mint-login'
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get(location, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            location = 'https://iguverse.com/whitelist-free-mint-subscribe'
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get(location, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            try:
                token = findall('csrf-token" content="(.*?)"', str(response.text))[0]
            except:
                pass
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get('https://iguverse.com/whitelist-free-mint-subscribe?skip=1', headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            try:
                token = findall('csrf-token" content="(.*?)"', str(response.text))[0]
            except:
                pass
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            location = findall("Location': '(.*?)'", str(response.headers))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get(location, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            try:
                token = findall('csrf-token" content="(.*?)"', str(response.text))[0]
            except:
                pass
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            location = 'https://iguverse.com/whitelist-free-mint-verify'
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            response = requests.get(location, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            try:
                token = findall('csrf-token" content="(.*?)"', str(response.text))[0]
            except:
                pass
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "193",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            data = f"_token={token}&email=1{tg_nick}1%40rambler.ru&telegram_username=1{tg_nick}1&twitter_username=1{twitter_nick}1&bsc_address={wallet}"
            response = requests.post('https://iguverse.com/whitelist-free-mint-profile', data=data, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            location = findall('Redirecting to <a href="(.*?)"', str(response.text))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Referer": "https://iguverse.com/whitelist-free-mint-profile",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            time.sleep(2)
            response = requests.get(location, headers=headers_for_igu, allow_redirects=False, proxies=proxy)
            x_csrf = findall('XSRF-TOKEN=(.*?);', str(response.headers))[0]
            ig_ses = findall('iguverse_session=(.*?);', str(response.headers))[0]
            headers_for_igu = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "Cookie": f"discord_application={dis_ap}; XSRF-TOKEN={x_csrf}; iguverse_session={ig_ses}",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "TE": "trailers"
            }
            try:
                invite_link = findall('class="form-control" readonly value="(.*?)"', str(response.text))[0]
                print(f"Ref ready / {invite_link}")
            except:
                print("Something troubles, CHECK ERRORS.TXT, RUN IT AGAIN")
                with open('errors.txt', 'a') as file3:
                    file3.write(line + '\n')
            # uncomment this if you want to write HEADERS to the file ^-^
            """ 
            with open('headers.txt', 'a') as file1:
                file1.write(str(headers_for_igu) + '\n')
            with open('invite_links.txt', 'a') as file2:
                file2.write(invite_link + '\n')
            """

            time.sleep(3)
def main():
    get_data()

if __name__ == "__main__":
    main()