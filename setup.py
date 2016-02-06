from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-jwt-cookie-auth',
    description='JWT Cookie Auth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.1.0',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    license='MIT',
    url='https://github.com/guardian/httpie-jwt-cookie-auth',
    download_url='https://github.com/guardian/httpie-jwt-cookie-auth',
    py_modules=['httpie_jwt_cookie_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_jwt_cookie_auth = httpie_jwt_cookie_auth:JwtCookieAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'PyJWT'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
