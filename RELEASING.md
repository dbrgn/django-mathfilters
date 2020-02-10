# Release process

Signing key: 3578F667F2F3A5FA (https://keybase.io/dbrgn)

Used variables:

    export VERSION={VERSION}
    export GPG=3578F667F2F3A5FA

Update version numbers:

    vim -p setup.py CHANGELOG.rst

Do a signed commit and signed tag of the release:

    git add setup.py CHANGELOG.rst
    git commit -S${GPG} -m "Release v${VERSION}"
    git tag -u ${GPG} -m "Release v${VERSION}" v${VERSION}

Build source and binary distributions:

    python3 setup.py sdist
    python3 setup.py bdist_wheel

Sign files:

    gpg --detach-sign -u ${GPG} -a dist/django-mathfilters-${VERSION}.tar.gz
    gpg --detach-sign -u ${GPG} -a dist/django_mathfilters-${VERSION}-py3-none-any.whl

Upload package to PyPI:

    twine3 upload dist/django-mathfilters-${VERSION}*.tar.gz
    twine3 upload dist/django_mathfilters-${VERSION}*.whl
    git push
    git push --tags
