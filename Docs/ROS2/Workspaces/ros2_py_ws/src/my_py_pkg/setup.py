from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Choaib ELMADI',
    maintainer_email='choaibamd@gmail.com',
    description='This is the description for my package',
    license='This is the license declaration for my package',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'pub_node = my_py_pkg.pub_node:main',
                             'sub_node = my_py_pkg.sub_node:main'
        ],
    },
)
