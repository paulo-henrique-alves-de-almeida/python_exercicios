import requests

api_url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/brl.min.json'
requisicao = requests.get(api_url)

print()
print('=' * 20, 'CONVERSÃO DE MOEDAS', '=' * 20)
print()

while True:
    try:
        dinheiro = float(input('Digite quanto dinheiro você tem agora: R$'))
    except:
        print('Digite apenas números.')
        print()
    else:
        break
print()

if dinheiro > 0:
    if requisicao.status_code == 200:
        dados = requisicao.json()
        
        date = dados['date'].split('-')
        date[0], date[2] = date[2], date[0]
        date = ' / '.join(date)

        valores = dados['brl']
        moedas = {'dolar': str(valores['usd'] * dinheiro).replace('.', ',').split(','),
                  'euro': str(valores['eur'] * dinheiro).replace('.', ',').split(','),
                  'iene': str(valores['jpy'] * dinheiro).replace('.', ',').split(','),
                  'dolar canadense': str(valores['cad'] * dinheiro).replace('.', ',').split(','),
                  'peso argentino': str(valores['ars'] * dinheiro).replace('.', ',').split(','),
                  'won': str(valores['krw'] * dinheiro).replace('.', ',').split(','),
                  'kwanza': str(valores['aoa'] * dinheiro).replace('.', ',').split(','),
                  'bitcoin': str(valores['btc'] * dinheiro).replace('.', ','),
                  'ethereum': str(valores['eth'] * dinheiro).replace('.', ','),
                  'litecoin': str(valores['ltc'] * dinheiro).replace('.', ','),
                  'ouro': str(valores['xau'] * dinheiro).replace('.', ',')}
        
        str_dinheiro = str(dinheiro).replace('.', ',').split(',')
        if len(str_dinheiro[1]) < 2:
            str_dinheiro[1] += '0'
        
        print(' ' * 5, f'Atualizado na data: {date}')

        print(f'''
Com R${str_dinheiro[0]},{str_dinheiro[1][:2]} você pode comprar:

{moedas['dolar'][0]},{moedas['dolar'][1][:2]} Dólar(es) americano(s)
{moedas['euro'][0]},{moedas['euro'][1][:2]} Euro(s)
{moedas['iene'][0]},{moedas['iene'][1][:2]} Iene(s)
{moedas['dolar canadense'][0]},{moedas['dolar canadense'][1][:2]} Dólar(es) canadense(s)
{moedas['peso argentino'][0]},{moedas['peso argentino'][1][:2]} Peso(s) argentino(s)
{moedas['won'][0]},{moedas['won'][1][:2]} Won(es)
{moedas['kwanza'][0]},{moedas['kwanza'][1][:2]} Kwanza(s)
{moedas['bitcoin']} Bitcoin
{moedas['ethereum']} Ethereum
{moedas['litecoin']} Litecoin
{moedas['ouro']} Ouro''')
    else:
        print('Não consegui verificar as cotações das moedas. Verifique sua internet.')
elif dinheiro == 0:
    print('Com R$0 você não pode comprar nenhuma outra moeda.')
else:
    print('Você precisa pagar suas dívidas antes de converter moedas XD')
print()
