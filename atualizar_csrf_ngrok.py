import requests
import os

# Caminho absoluto ou relativo para seu settings.py
SETTINGS_PATH = './core/settings.py'

def get_ngrok_url():
    try:
        resp = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = resp.json().get("tunnels", [])
        for t in tunnels:
            if t['proto'] == 'https':
                return t['public_url']
    except Exception as e:
        print("Erro ao acessar ngrok:", e)
    return None

def atualizar_settings(csrf_url):
    if not csrf_url:
        print("Domínio do ngrok não encontrado.")
        return

    csrf_line = f"CSRF_TRUSTED_ORIGINS = ['{csrf_url}']\n"

    with open(SETTINGS_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(SETTINGS_PATH, 'w', encoding='utf-8') as f:
        found = False
        for line in lines:
            if line.strip().startswith("CSRF_TRUSTED_ORIGINS"):
                f.write(csrf_line)
                found = True
            else:
                f.write(line)
        if not found:
            f.write('\n' + csrf_line)

    print(f"✅ CSRF_TRUSTED_ORIGINS atualizado com: {csrf_url}")

if __name__ == '__main__':
    url = get_ngrok_url()
    atualizar_settings(url)
