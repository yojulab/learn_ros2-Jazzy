from setuptools import find_packages, setup

package_name = 'first_package_msgs'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Add the message files to be installed
        ('share/' + package_name + '/msg', ['msg/CmdAndPoseVel.msg']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sanghun-oh',
    maintainer_email='otter.oh@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
