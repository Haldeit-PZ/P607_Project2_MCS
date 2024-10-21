# Always prefer setuptools over distutils

from setuptools import setup, find_packages

setup(
    name='2D_Box',
    version='0.1.0',
    author='Ben Maves, Haoyang Zhou',
    description="A Monte-Carlo Simulation of 2D Box Containing Ideal Gas Particles", 
    author_email='hzhou51@syr.edu',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Haldeit-PZ/P607_Project2_MCS.git', 
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
    ],
    entry_points={
        'console_scripts': [
            'my-command=scripts.my_script:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
