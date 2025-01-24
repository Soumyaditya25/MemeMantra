"""
Imgflip Meme Generator
Supports English, Hindi, or any Unicode text captions.
Author: Soumyaditya
Version: 1.0
"""

import sys
import requests

API_BASE = 'https://api.imgflip.com'
USERNAME = 'ImgS'
PASSWORD = 'image123'


def fetch_templates() -> list:
    """Fetch meme templates from Imgflip API."""
    try:
        resp = requests.get(f'{API_BASE}/get_memes', timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if not data['success']:
            raise RuntimeError('Imgflip API returned failure status.')
        return data['data']['memes']
    except Exception as e:
        print(f'[Error] Unable to fetch templates: {e}', file=sys.stderr)
        sys.exit(1)


def choose_template(memes: list) -> dict:
    """Display templates and let user pick one by number."""
    print('\nAvailable Meme Templates:\n')
    for i, m in enumerate(memes, start=1):
        print(f"{i:3}. {m['name']} (id: {m['id']})")
    while True:
        choice = input('\nEnter template number: ').strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(memes)):
            print('Please enter a valid number between 1 and', len(memes))
            continue
        return memes[int(choice) - 1]


def get_captions() -> tuple:
    """Prompt for top and bottom text, supporting Unicode."""
    txt0 = input('Enter top text (Hindi/English/Unicode supported): ').strip()
    txt1 = input('Enter bottom text (Hindi/English/Unicode supported): ').strip()
    return txt0, txt1


def create_meme(template_id: str, text0: str, text1: str) -> dict:
    """Call the caption_image endpoint to generate meme."""
    payload = {
        'template_id': template_id,
        'username': USERNAME,
        'password': PASSWORD,
        'text0': text0,
        'text1': text1
    }
    try:
        resp = requests.post(f'{API_BASE}/caption_image', params=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if not data['success']:
            raise RuntimeError(data.get('error_message', 'Unknown API error'))
        return data['data']
    except Exception as e:
        print(f'[Error] Meme creation failed: {e}', file=sys.stderr)
        sys.exit(1)


def download_image(url: str, filename: str) -> None:
    """Download the generated meme image locally."""
    try:
        resp = requests.get(url, stream=True, timeout=10)
        resp.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)
        print(f'[Success] Image saved as: {filename}')
    except Exception as e:
        print(f'[Error] Download failed: {e}', file=sys.stderr)
        sys.exit(1)


def main():
    print("\n=== Imgflip Meme Generator ===\n")
    templates = fetch_templates()
    tmpl = choose_template(templates)
    print(f"\nSelected: {tmpl['name']} (id: {tmpl['id']})\n")
    top_text, bottom_text = get_captions()
    result = create_meme(tmpl['id'], top_text, bottom_text)
    print('\nMeme URL:', result['url'])
    print('Page URL:', result['page_url'], '\n')
    save = input('Download image? [y/N]: ').strip().lower()
    if save == 'y':
        # sanitize filename
        safe_name = tmpl['name'].replace(' ', '_').replace('/', '_')
        download_image(result['url'], f'{safe_name}.jpg')
    else:
        print('Skipped download.')
    print('\nThank you for using the Meme Generator!')


if __name__ == '__main__':
    main()
