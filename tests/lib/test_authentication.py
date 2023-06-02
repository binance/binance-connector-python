from binance.lib.authentication import hmac_hashing, rsa_signature, ed25519_signature
import pytest


def test_hamc_hashing():
    secret = "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"
    data = "timestamp=1578963600000"
    hash_value = hmac_hashing(secret, data)
    hash_value.should.equal(
        "d84e6641b1e328e7b418fff030caed655c266299c9355e36ce801ed14631eed4"
    )


def test_rsa_signature():
    rsa_secret_key = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPrfWMr2yqxJgJ
cIyA5TDFpZBlB9E3RMbbEcPZijmPDiciZjuRiD1Q6oQzi1MFGTZ523HwSXe9XG3R
NQaLCjxi+VkLsvCoxzgurkWXoQr0VHJyEDxnyRaCzTyvvHQgt0LKCWfqalYNz0ue
doxnYnde3DH/tFFXX0/rTkJyK6LpOyKOAqE0G7OhuQWkLvlUO8mqwtGNqdrtOgzv
kTN5rhb5VeWB4JGWDcAYFb9CQI9wD7/JJU1XQGIOJEY3L/PjGLcjDEiROt57/RS3
i6OVTiAgDcgA405tNLgS326hfbEchI5tKeOxqrFYVfvOK8+4o+rrUBnMhrBg0tJv
1feQKeAnAgMBAAECggEAUdB8PZIWQyfzpTRbhaPElPhmbAaqWxWTKVZUS2zyw/KV
ZC3WJb0AOtJIhm3KpOWL2nGi70BiFY1GDfbPvxKnO25zr/IscLEa5vjsnZFp2Vsz
QtA2m8RSQ/FKiQi6zvCjNSiDcYu2nvYdGi4lnczirdIdOFj2+m6n81D/SC78nNhj
P/JLbSPFw+XOfVqOVelXHw7XGtMH9dgFjWDdB317HcJjZyPDahpQQ7s6PcecDwuv
Qucs+Hi4sAWiHOiwKusx3sT/NL5Og/jAvC5aMy1QswWFnPr90T3qFE4MN1GZszzX
DmDkWaGaRwuwdpi/ocIZF3R9XX3m+WOVdEZRfzzcEQKBgQDt11achN666/j1kgQM
xPdzo06eUUZb/JUtEXz8hU+AzRsN/eso/47pjaPq7nrXFYE4aEx7Je2I9S52Y+b/
SLrctuza25VOxvqIpDynlvM/Iatg9WuTEIuOk7gkBFanDNjDjZDKFuDYSEfN+sX+
UakFT7cm+xu12PWR8HlZmFZL5QKBgQDfiRrC8zADSIE74uFBJ5K88t6cwrktqdPH
9QT69j+VpRXssyUoCfR4/zchKbEyTwSASvL1saJR14Opmvn6Le+0DKq+EV7Z1UM6
svVIzd9pWWMhRh9G83CC5Krx9Ie+34QHNRxBf+rya5if/aBCDtBFedRGbR6Le8MB
yvrpT5hzGwKBgQCU2+QPjnHA2BQ3zq3OODEQJTP9jqzUwd+0F2/8tIsv+C9osHXQ
cTLHJqljTuN/XqxD27OSmAh1Yc80tg5L1P9vSOYxjKGEbrE7eF+mHKod5zrWMoSj
xQUztWzYzgZWA4pfymjGs08Czypx1vS42e9JrbzaHuwXArWgI7wvwVKxqQKBgQCS
ByIZav7Zljr+oUdf5fdBQjPVGowYXZJBVTpMrCN7od4BxEIotuAjTy53lqHwaJhb
KxsvED0m0/BqExjsq6ek6oV8JyLckSobJZ+BUSR60O8mZIW4Nv4wNCvMZl9rfN7m
SnbL/0G/3jRViD1yCfVa/ayD2XMT0eThvfVOBzZjMwKBgB5jasP9TcDAyaEKta+g
6glTM0MKUWfhZzYRbvDXdnatjjMEdixWm9aXwc0Nw+aN0KkdLBwvnDiVMtX+Xl2n
BU2Gxxe3H8qrvkoi8zmzh3VWpqzfB+L3sXAq+6VNNYLEFLBR6D2u4DD86FvY+DsU
miJlY6JEKpSxvkrS04XrbvHk
-----END PRIVATE KEY-----"""
    payload = "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"
    expected_signature = "uz2xmNkOf1EEsnZoWGraxR13F4jF9JYdC68uvWqYyjFyjwDgcoiMRm23UqsxWkmA208smu7TuGVxm1cWoZa/5fLQ2T/RcfLW9sokNWDzf1vM/xEpSmQEsSyIzd/c0pMWGsUkXsYpIarp3e/KSFzgwI73qZfbalBRkkK7u3dLWRVRk4kmEVf6dQUWMyXC44X8LB0M1XFrhkqcFYdcP9NcaCZCvb8nzG/nyUPtCJdBxVn8MMgXaVCM8DIbSrUBT0ZUxFQ3gTSd929LR1Tp6P2y4pHiWSElW5nJZYRRn2zUFt4xH7wvVKvuuEi8HH0Dusf6KBcWq8/3viAcRUh1Cj4fsQ=="
    sign = rsa_signature(rsa_secret_key, payload).decode("utf-8")
    sign.should.equal(expected_signature)


def test_encrypted_rsa_signature():
    rsa_secret_key = """-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIE6TAbBgkqhkiG9w0BBQMwDgQIeaAJMt/f5woCAggABIIEyI2jIbFTPo/YBmwH
N1QqzFgnMK5LJ0pKY5O71Z8EZIBVrXtEdcFzswbwRZajMpMyxFBjhrd2Y4kQvt9K
aQfwyJFQxs8L2hC1GRYf5ba6aNZHkWendNFvOET02UQwgDNdGdWCfcaoMCap0ZQ2
7VOyqbwtuRkM2LNlrtbu282FbwXe4wKljSNUIXTU3UaCmjOq5KIwBoRKJYlwn0qt
IzlyJKVurHX4cl/1mw55Qs+hRL1CdK/iYF5yqclbK96zq16SKZsaZZhHMf1oub4U
v5QjJiiQZc+WONFpBi2TybQ1qXF/6+70lDofY3+moUVcPgFHVsKEVQJtYuRZoGoc
QlXyyCRTyCIQSO41jhkRcJtjCpVCfvCwlob0cM59Hlfll9DdjKyAtaUsuA+cDMqd
ZE8HSjBGXuSwWthHSfblZ84LReHufmiIYGO3+n0dyjdLKcakYJ5V4QwxN2y4CwE7
TxszcZo7QYDRaWlz7Lx2gtXlS6UNhs5Ylt7lm/omkdg57zf9DO9P8Vhn0thXs5Ql
7QIUzhhg0kgnagwmy682AkV+O6F1wWw8qV0uUxABvo9VNuUF8aYBFr9iJn1fUg8Y
kjCXKns/S9l6Zhz3rSgjFzNdWmm+1TigjyqaVgK9Jdte/v9IG46R3q/rQDMSqIFn
zO25DfwOr8GvSgxN4Ervy/IwqoC94ptFCLfTJdL2n7IRWX9B+ai2RVSnBEXti4BR
nigKUkVR7+ynwA8KN5sf6Zc0apHIuylXnu4xeO0rehxhh920v05IjAPm9YIOP33/
UkHZWtXe2MooV4jmSiWMfAAgL8J26vML2xeGjhFZNQPM1/C3TB+UBxvKbD47EO6k
FgoVmpFZGTXbF1Rq9hyUpABOSDhPyVuQxW+Tmyjm8O0Oc7KABUP09DKneiNFFtO9
/B2u7FZ2ArfUzHesEJLWU+CtYVPdpbvtmd054tMV53j3cga2SQmg/yYWOQ7LyMjo
7FR04aBTq+BXGgU/fZryyHUb1fULy7YTCiMyvi2m+JrZ+TE7DSvbDiJVcZ52x++J
UpmID04q3wSRrOjci3yXUBvSa1yqxH8F5j3tv/nVM8x2s8ZLEgOHARS0CHZ6KRGD
TP3KqsOPoKognk712zbqJPWhx9HdAm9+B/5qWtUEOoeFXlzyzj0suVICg9rPNJm1
zx+STX5zTQ9oPNj6MFgZPSzIoW5Wb6vEdu7ANoANuStMp3E2sQf7q0gY5UkfnYyj
beTf+1t3k9ybAVZiT6yZ7T5KGeh040zSN2vpVKEEWzkGrL4wGs+aMpvtBEnVJYLl
medTIY6Z2PM/GFd8Ky8I+uTazXfvZUdilYCyZeIoO6Hyomy7TrnCzc/vjkhWtQrW
+Pu5GjcGziUXNpzHNS+7uIOOa4f6VpGB8m5QsGUT7nPvVQqvta5fgJ8+W9J5Ifp5
JqlyEAC7b7PFP9Rz65Do9AsbUbDStKMHl5CR/+CeOnzgfgeHCA8EroQ6WxMHFXec
GSsZ7VWSSlgOyIEcNMhiM9PKAbx65TbUcvb+KWAI5aUwmdjrKFqOKDloX+2fn9y8
qoOMy1yIoV7uYL+c4zugjzpgy58iBAiR1IVectxQY9lx1+d9tfjwK2Ne96hdzlLO
/zJyaPr5pCU/IAr6Rg==
-----END ENCRYPTED PRIVATE KEY-----"""
    payload = "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"
    expected_signature = "uz2xmNkOf1EEsnZoWGraxR13F4jF9JYdC68uvWqYyjFyjwDgcoiMRm23UqsxWkmA208smu7TuGVxm1cWoZa/5fLQ2T/RcfLW9sokNWDzf1vM/xEpSmQEsSyIzd/c0pMWGsUkXsYpIarp3e/KSFzgwI73qZfbalBRkkK7u3dLWRVRk4kmEVf6dQUWMyXC44X8LB0M1XFrhkqcFYdcP9NcaCZCvb8nzG/nyUPtCJdBxVn8MMgXaVCM8DIbSrUBT0ZUxFQ3gTSd929LR1Tp6P2y4pHiWSElW5nJZYRRn2zUFt4xH7wvVKvuuEi8HH0Dusf6KBcWq8/3viAcRUh1Cj4fsQ=="
    sign = rsa_signature(rsa_secret_key, payload, private_key_pass="password").decode(
        "utf-8"
    )
    sign.should.equal(expected_signature)


def test_invalid_rsa_secret_key():
    invalid_rsa_secret_key = """-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIE6TAbBgkqhkiG9w0BBQMwDgQIeaAsdasdlju9u21u381273872138ydJMt/f5woCAggABIIEyI2jIbFTPo/YBmwH
N1QqzFgnMK5LJ0pKY5O71Z8EZIBVrXtEdcFzswbwRZajMpMyxFBjhrd2Y4kQvt9K
aQfwyJFQxs8L2hC1GRYf5ba6aNZHkWendNFvOET02UQwgDNdGdWCfcaoMCap0ZQ2
7VOyqbwtuRkM2LNlrtbu282FbwXe4wKljSNUIXTU3UaCmjOq5KIwBoRKJYlwn0qt
IzlyJKVurHX4cl/1mw55Qs+hRL1CdK/iYF5yqclbK96zq16SKZsaZZhHMf1oub4U
v5QjJiiQZc+WONFpBi2TybQ1qXF/6+70lDofY3+moUVcPgFHVsKEVQJtYuRZoGoc
QlXyyCRTyCIQSO41jhkRcJtjCpVCfvCwlob0cM59Hlfll9DdjKyAtaUsuA+cDMqd
ZE8HSjBGXuSwWthHSfblZ84LReHufmiIYGO3+n0dyjdLKcakYJ5V4QwxN2y4CwE7
TxszcZo7QYDRaWlz7Lx2gtXlS6UNhs5Ylt7lm/omkdg57zf9DO9P8Vhn0thXs5Ql
7QIUzhhg0kgnagwmy682AkV+O6F1wWw8qV0uUxABvo9VNuUF8aYBFr9iJn1fUg8Y
kjCXKns/S9l6Zhz3rSgjFzNdWmm+1TigjyqaVgK9Jdte/v9IG46R3q/rQDMSqIFn
zO25DfwOr8GvSgxN4Ervy/IwqoC94ptFCLfTJdL2n7IRWX9B+ai2RVSnBEXti4BR
nigKUkVR7+ynwA8KN5sf6Zc0apHIuylXnu4xeO0rehxhh920v05IjAPm9YIOP33/
UkHZWtXe2MooV4jmSiWMfAAgL8J26vML2xeGjhFZNQPM1/C3TB+UBxvKbD47EO6k
FgoVmpFZGTXbF1Rq9hyUpABOSDhPyVuQxW+Tmyjm8O0Oc7KABUP09DKneiNFFtO9
/B2u7FZ2ArfUzHesEJLWU+CtYVPdpbvtmd054tMV53j3cga2SQmg/yYWOQ7LyMjo
7FR04aBTq+BXGgU/fZryyHUb1fULy7YTCiMyvi2m+JrZ+TE7DSvbDiJVcZ52x++J
UpmID04q3wSRrOjci3yXUBvSa1yqxH8F5j3tv/nVM8x2s8ZLEgOHARS0CHZ6KRGD
TP3KqsOPoKognk712zbqJPWhx9HdAm9+B/5qWtUEOoeFXlzyzj0suVICg9rPNJm1
zx+STX5zTQ9oPNj6MFgZPSzIoW5Wb6vEdu7ANoANuStMp3E2sQf7q0gY5UkfnYyj
beTf+1t3k9ybAVZiT6yZ7T5KGeh040zSN2vpVKEEWzkGrL4wGs+aMpvtBEnVJYLl
medTIY6Z2PM/GFd8Ky8I+uTazXfvZUdilYCyZeIoO6Hyomy7TrnCzc/vjkhWtQrW
+Pu5GjcGziUXNpzHNS+7uIOOa4f6VpGB8m5QsGUT7nPvVQqvta5fgJ8+W9J5Ifp5
JqlyEAC7b7PFP9Rz65Do9AsbUbDStKMHl5CR/+CeOnzgfgeHCA8EroQ6WxMHFXec
GSsZ7VWSSlgOyIEcNMhiM9PKAbx65TbUcvb+KWAI5aUwmdjrKFqOKDloX+2fn9y8
qoOMy1yIoV7uYL+c4zugjzpgy58iBAiR1IVectxQY9lx1+d9tfjwK2Ne96hdzlLO
/zJyaPr5pCU/IAr6Rg==
---23123--END ENCRYPTED PRIVATE KEY-----"""
    payload = "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"
    with pytest.raises(ValueError):
        rsa_signature(
            invalid_rsa_secret_key, payload, private_key_pass="password"
        ).decode("utf-8")


def test_ed25519_signature():
    ed25519_secret_key = """-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIE4rJ0goma1nbu1d8T1dp//0pe40jnf8tghwRhsSY4Bk
-----END PRIVATE KEY-----"""
    payload = "type=SPOT&timestamp=1685686334211"
    expected_signature = "E4nWIl3yUJgJFL6LoWImsrEwNegMiN9SN1FWKw+P3xXkJ2T/MtSq3Cg7fVnOGFWxTBX6vrTJJNoZnVtAgs1CAQ=="
    sign = ed25519_signature(ed25519_secret_key, payload, private_key_pass=None).decode(
        "utf-8"
    )
    sign.should.equal(expected_signature)


def test_ed25519_signature_invalid_format():
    invalid_ed25519_secret_key = """-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK231297dsah3167bjsfdaVwBCIEIE4rJ0goma1nbu1d8T1dp//0pe40jnf8tghwRhsSY4Bk
--123321---END PRIVATE KEY-----"""
    payload = "type=SPOT&timestamp=1685686334211"
    with pytest.raises(ValueError):
        ed25519_signature(
            invalid_ed25519_secret_key, payload, private_key_pass=None
        ).decode("utf-8")
