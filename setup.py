from setuptools import setup, find_packages

exec(open('magvit2_pytorch/version.py').read())

def parse_requirements(filename):
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith('#')]

setup(
  name = 'magvit2-pytorch',
  packages = find_packages(),
  version = __version__,
  license='MIT',
  description = 'MagViT2 - Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/magvit2-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformer',
    'attention mechanisms',
    'generative video model'
  ],
  install_requires=parse_requirements('requirements.txt'),
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
