

from gtts import gTTS
from playsound import playsound

#from io import BytesIO
#mp3_fp = BytesIO()

#Language
'''
  af: Afrikaans
  ar: Arabic
  bn: Bengali
  bs: Bosnian
  ca: Catalan
  cs: Czech
  cy: Welsh
  da: Danish
  de: German
  el: Greek
  en-au: English (Australia)
  en-ca: English (Canada)
  en-gb: English (UK)
  en-gh: English (Ghana)
  en-ie: English (Ireland)
  en-in: English (India)
  en-ng: English (Nigeria)
  en-nz: English (New Zealand)
  en-ph: English (Philippines)
  en-tz: English (Tanzania)
  en-uk: English (UK)
  en-us: English (US)
  en-za: English (South Africa)
  en: English
  eo: Esperanto
  es-es: Spanish (Spain)
  es-us: Spanish (United States)
  es: Spanish
  et: Estonian
  fi: Finnish
  fr-ca: French (Canada)
  fr-fr: French (France)
  fr: French
  hi: Hindi
  hr: Croatian
  hu: Hungarian
  hy: Armenian
  id: Indonesian
  is: Icelandic
  it: Italian
  ja: Japanese
  jw: Javanese
  km: Khmer
  ko: Korean
  la: Latin
  lv: Latvian
  mk: Macedonian
  ml: Malayalam
  mr: Marathi
  ne: Nepali
  nl: Dutch
  no: Norwegian
  pl: Polish
  pt-br: Portuguese (Brazil)
  pt-pt: Portuguese (Portugal)
  pt: Portuguese
  ro: Romanian
  ru: Russian
  si: Sinhala
  sk: Slovak
  sq: Albanian
  sr: Serbian
  su: Sundanese
  sv: Swedish
  sw: Swahili
  ta: Tamil
  te: Telugu
  th: Thai
  tl: Filipino
  tr: Turkish
  uk: Ukrainian
  vi: Vietnamese
  zh-cn: Chinese (Mandarin/China)
  zh-tw: Chinese (Mandarin/Taiwan)
'''
tts=gTTS(text='You are under arrest.', lang='en-ca')

tts.save('happybirthday.mp3')

#tts.write_to_fp(mp3_fp)


playsound('happybirthday.mp3')

