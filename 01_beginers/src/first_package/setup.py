from setuptools import find_packages, setup

package_name = 'first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'first_node = first_package.first_node:main',
            'turtlesim_publisher = first_package.turtlesim_publisher:main',
            'turtlesim_subscriber = first_package.turtlesim_subscriber:main',
            'turtlesim_cmd_and_pose = first_package.turtlesim_cmd_and_pose:main',
            'first_service_server = first_package.first_service_server:main',
            'turtlesim_service_multispawns = first_package.turtlesim_service_multispawns:main',
            'first_action_server = first_package.first_action_server:main',
            'first_multi_thread = first_package.first_multi_thread:main',
        ],
    },
)
