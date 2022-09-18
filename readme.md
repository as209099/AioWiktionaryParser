### Async AioWiktionary Parser

This Repository comes from [Wiktionary](https://github.com/Suyash458/WiktionaryParser)

A python project which downloads words from English Wiktionary ([en.wiktionary.org](https://en.wiktionary.org)) and parses articles' content in an easy to use JSON format. Right now, it parses etymologies, definitions, pronunciations, examples, audio links and related words.

#### JSON structure

```json
[{
    "pronunciations": {
        "text": ["pronunciation text"],
        "audio": ["pronunciation audio"]
    },
    "definitions": [{
        "relatedWords": [{
            "relationshipType": "word relationship type",
            "words": ["list of related words"]
        }],
        "text": ["list of definitions"],
        "partOfSpeech": "part of speech",
        "examples": ["list of examples"]
    }],
    "etymology": "etymology text",
}]
```

#### Installation

##### From Source
* Clone the repo or download the zip
* `cd` to the folder
* run `pip install -r "requirements.txt"`
* run `python3 -m setup.py build`
* run `python3 -m setup.py install`

#### Usage

 - Import the AioWiktionaryParser class.
 - Initialize an object and use the `fetch("word", "language")` method.
 - The default language is English, it can be changed using the `set_default_language method`.
 - Include/exclude parts of speech to be parsed using `include_part_of_speech(part_of_speech)` and `exclude_part_of_speech(part_of_speech)`
 - Include/exclude relations to be parsed using `include_relation(relation)` and `exclude_relation(relation)`

#### Examples

```python
>>> import asyncio
>>> from aiowiktionaryparser import AioWiktionaryParser
>>> parser = WiktionaryParser()
>>> word = 'test'
>>> task = parser.fetch(word)
>>> loop = asyncio.get_event_loop()
>>> word_data:dict = loop.run_until_complete(task)
```

#### Requirements

 - requests==2.20.0
 - beautifulsoup4==4.4.0
 - aiohttp
 - async_retrying

#### Contributions

If you want to add features/improvement or report issues, feel free to send a pull request!

#### License

Wiktionary Parser is licensed under [MIT](LICENSE.txt).
