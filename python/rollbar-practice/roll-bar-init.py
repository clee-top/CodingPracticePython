import rollbar

rollbar.init(
    # Maybe don't commit your token, nerd...
    access_token='NOTASECRET',
    environment='testenv',
    code_version='1.0'
)
rollbar.report_message('Rollbar is configured correctly. Meow.', 'info')