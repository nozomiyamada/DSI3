import re, emoji, urllib, html
from pythainlp import word_tokenize

def tokenize(
        text:str,
        return_list=True,
        keep_whitespace=False,
        remove_emoji=True,
        only_thaiword=True
        ):
    ### REMOVE URL ###
    text = html.unescape(urllib.parse.unquote(text)) # unescape for unicode, unquote for escaped URL
    text = re.sub(r'https?.+?(?:\s|$)', '', text) # remove URL link
    ### REMOVE EMOJI ###
    if remove_emoji:
        text = emoji.replace_emoji(text) # remove emoji
    ### REPLACE CHARACTERS ###
    text = re.sub(r'[“”„\"]', '', text) # remove double quotations
    text = re.sub(r'[‘’′′′′`\']', '', text) # remove single quotations
    text = re.sub(r'[\n\t\u00a0\xa0\u3000\u2002-\u200a\u202f]+', ' ', text) # shrink whitespaces e.g. good  boy -> good boy
    text = re.sub(r'[\r\u200b\ufeff]+', '', text) # remove non-breaking space
    text = re.sub(r'เเ', 'แ', text)
    ### SHRINK REDUPLICATIONS ###
    text = re.sub(r'าา+', 'า', text)
    text = re.sub(r'ยย+', 'ย', text)
    text = re.sub(r'ๆๆ+', 'ๆ', text)
    text = re.sub(r'ะะ+', 'ะ', text)
    text = re.sub(r'\.\.+', '', text)
    ### vowel am ###
    text = re.sub(r'ํา','ำ', text) # o + า -> ำ
    text = re.sub(r'\u0E33([\u0E48\u0E49\u0E4A\u0E4B])', r'\1'+'\u0E33', text) # am + tone -> tone + am
    ### TOKENIZE AND FILTERING ###
    tokens = word_tokenize(text, keep_whitespace=keep_whitespace)
    tokens = [token.strip('(').strip(')') for token in tokens]
    if only_thaiword:
        tokens = [token for token in tokens if re.match(r'[ก-ไ][ก-๙\.]*', token)]
    ### RETURN ###
    if return_list:
        return tokens
    else:
        return ' '.join(tokens)
    
def convert_datetime(text):
    text = text.strip()
    text = re.sub('[\n\t\s\xa0\u3000\u2002-\u200a\u202f\r\u200b\ufeff]+', ' ', text) # shrink whitespaces
    d, m, y = text.split()
    m = {'ม.ค.': '1',
    'ก.พ.': '2',
    'มี.ค.': '3',
    'เม.ย.': '4',
    'พ.ค.': '5',
    'มิ.ย.': '6',
    'ก.ค.': '7',
    'ส.ค.': '8',
    'ก.ย.': '9',
    'ต.ค.': '10',
    'พ.ย.': '11',
    'ธ.ค.': '12',
    'มกราคม': '1',
    'กุมภาพันธ์': '2',
    'มีนาคม': '3',
    'เมษายน': '4',
    'พฤษภาคม': '5',
    'มิถุนายน': '6',
    'กรกฎาคม': '7',
    'สิงหาคม': '8',
    'กันยายน': '9',
    'ตุลาคม': '10',
    'พฤศจิกายน': '11',
    'ธันวาคม': '12'}.get(m, m)
    if int(y) > 2300:
        y = int(y) - 543
    return f'{y}-{m.zfill(2)}-{d.zfill(2)}'

def edit_distance(s1, s2, replace_cost=1):
    dist = [[j for j in range(len(s2)+1)]]
    for i in range(1, len(s1)+1):
        dist.append([i] + [0]*len(s2))
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            right = dist[i][j-1] + 1
            down = dist[i-1][j] + 1
            if s1[i-1] == s2[j-1]:
                diag = dist[i-1][j-1]
            else:
                diag = dist[i-1][j-1] + replace_cost
            dist[i][j] = min(right, down, diag)
    return dist[-1][-1]