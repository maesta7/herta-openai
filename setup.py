from setuptools import setup, find_packages

setup(
    name='herta-openai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "openai", "git+https://github.com/maesta7/herta.git"
    ],
    author='Pon Pongwachirin',
    author_email='tar.workspace@gmail.com',
    description='Herta OpenAI Package',
    url='https://github.com/maesta7/herta',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
