#### Introduction

A basic CLI tool to create environment variables in linux by parsing JSON file in Google client secrets format for web applications.

More info on client secrets: [Google API Client Secrets](https://developers.google.com/api-client-library/dotnet/guide/aaa_client_secrets)

The JSON file is used for storing `client_id`, `client_secret`, and other OAuth 2.0 parameters like:
```
{
    "web":{
        "client_id":"asdfjasdljfasdkjf",
        "project_id":"project_foo_id",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
        "client_secret":"1912308409123890sdfscsdfa",
        "redirect_uris":["http://www.example.com/login/auth"],
        "javascript_origins":["http://www.example.com/"]
    }
}
```

#### Usage

Requires: `pip` and `python 3.6+`

```
$ pip install --editable .
$ gcp_secrets_to_env -j client_secrets.json -p ENV_Prefix

reading secrets from client_secrets.json
dectected OS: linux
writing to bashrc
created env ENV_Prefix_CLIENT_ID for parameter client_id
created env ENV_Prefix_PROJECT_ID for parameter project_id
created env ENV_Prefix_AUTH_URI for parameter auth_uri
created env ENV_Prefix_TOKEN_URI for parameter token_uri
created env ENV_Prefix_AUTH_PROVIDER_X509_CERT_URL for parameter auth_provider_x509_cert_url
created env ENV_Prefix_CLIENT_SECRET for parameter client_secret
created env ENV_Prefix_REDIRECT_URIS for parameter redirect_uris
created env ENV_Prefix_JAVASCRIPT_ORIGINS for parameter javascript_origins

```