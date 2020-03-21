from distutils.core import setup

setup(
  name = 'covid19uncle',         # How you named your package folder (MyLib)
  packages = ['covid19uncle'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Information of COVID-19 [Global] and [Thailand]',   # Give a short description about your library
  long_description='please read in: https://github.com/UncleEngineer/covid19',
  author = 'Loong Wissawakorn',                   # Type in your name
  author_email = 'loong.wissawakorn@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/UncleEngineer/covid19',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/UncleEngineer/covid19/archive/0.0.1.zip',    # I explain this later on
  keywords = ['COVID-19', 'CORONA VIRUS', 'Uncle Engineer', 'UncleEngineer'],   # Keywords that define your package best
  install_requires=[
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
