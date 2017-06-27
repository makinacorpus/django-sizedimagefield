from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


def changes():
    with open('CHANGES.rst') as f:
        return f.read()


setup(
    name='django-sizedimagefield',
    version='0.1.1',
    description='A very simple Django field to resize images at upload.',
    long_description=readme() + '\n\n' + changes(),
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='django sized image resize thumbnail',
    url='http://github.com/makinacorpus/django-sizedimagefield',
    author='Gagaro',
    author_email='yann.fouillat@makina-corpus.com',
    license='BSD',
    packages=['sizedimagefield'],
    zip_safe=False
)
