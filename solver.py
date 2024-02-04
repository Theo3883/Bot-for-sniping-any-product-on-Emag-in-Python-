# https://github.com/2captcha/2captcha-python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', '068fdbce83d42cae604e817a0bdac220')

solver = TwoCaptcha(api_key)

try:
    result = solver.hcaptcha(
        sitekey='6LelWGYpAAAAAH6Z0u0z7Hb3csAIcB4jqQ3kxEfn',
        url='https://auth.emag.ro/user/login',
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))