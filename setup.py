try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='notify-pipe',
    version='0.0.1',
    author='Alexander Treptau',
    author_email='alex@treptau.eu',
    url='https://github.com/fasib/notify-pipe',
    py_modules=['notify_pipe',],
    entry_points={
        'console_scripts': [
            'notify-pipe = notify_pipe:_main',
        ],
    },
)
