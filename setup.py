from setuptools import setup, find_packages

setup(
    name='pydashlite',
    version='0.2.0',
    description='Simple tools similar to pydash, but more specific and faster.',
    url='https://github.com/glowlex/pydashlite',
    author='glowlex',
    author_email='antonioavocado777@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    test_suite="tests",
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    )
