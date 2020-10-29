# modern python project

## create a repository in github

* gitignore
* license
* readme

## global tools

### pyenv

```bash
brew install pyenv

# modify shell
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile

# build dependencies of python
brew install openssl readline sqlite3 xz zlib

source ~/.bash_profile
```

### python

```bash
pyenv install 3.9.0

# make python version in local directory
pyenv local 3.9.0
```

### poetry

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

1. open a new shell, initialize python project

    ```bash
    peotry init -n
    ```

2. 修改 `project.toml`

3. 增加 `src`, 在其中增加 `modern_python` package
    repository --> kebab case  `modern-python`
    python package --> snake case `modern_python`

4. `__init__.py`
    ```python
    # src/modern_python/__init__.py
    __version__ = "0.1.0"
    ```

5. 创建python虚拟环境

    ```bash
    poetry install

    # run python inside the new venv
    poetry run python
    ```
6. 添加依赖

    ```bash
    poetry add click
    ```