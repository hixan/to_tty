from setuptools import setup
setup(
        name='to_tty',
        author='Hixan',
        author_email='Alex.88.Elias@gmail.com',
        version='1.0',
        py_modules=['to_tty'],
        install_requires=['Click', 'to_tty'],
        entry_points = '''
        [console_scripts]
        to-tty=to_tty:main
        '''
)
