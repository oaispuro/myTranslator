import os
import openai
import config


openai.api_key = config.api_key


def getLanguageTranslation(prompt, language ):
    response = openai.Completion.create(
        engine="text-davinci-002",
         prompt="Translate this into {}\n{}".format(language, prompt),
         temperature=0.3,
         max_tokens=100,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0)

    if 'choices' in response:
        if len(response['choices']) > 0:
            ans = response['choices'][0]['text']
        else:
            ans = 'You bested AI this time'
    else:
        ans = 'You bested AI this time'

    return ans 





