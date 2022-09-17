from setuptools import setup,find_packages

with open('readme.md', 'r') as readme:
  long_desc = readme.read()

setup(
  name = 'aiowiktionaryparser',
  version = '0.0.1',
  description = 'A async tool to parse word data from wiktionary.com into a JSON object',
  long_description = long_desc,
  long_description_content_type='text/markdown',
  packages = ['aiowiktionaryparser', 'tests'],
  data_files=[('testOutput', ['tests/testOutput.json']), ('readme', ['readme.md']), ('requirements', ['requirements.txt'])],
  author = 'as209099',
  author_email = 'as209099@gmail.com',
  url = 'https://github.com/as209099/AioWiktionaryParser', 
  keywords = ['Parser', 'Wiktionary', 'Async'],
  install_requires = ['beautifulsoup4','requests', 'aiohttp', 'async_retrying'],
  classifiers=[
   'Development Status :: 5 - Production/Stable',
   'License :: OSI Approved :: MIT License',
  ],
)