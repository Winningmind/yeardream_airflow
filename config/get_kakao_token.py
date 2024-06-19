import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = 'a237b86212fd39bf5eae997f260e6da2'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'wztQpd-wBWhfnZ7BrCq_P1Bra7h98eQAvJfAIbJ8UAj5uRnqvWKzLAAAAAQKKw0gAAABkC30AcBSGUcvaFb1Eg'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)