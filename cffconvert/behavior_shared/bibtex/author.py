from abc import abstractmethod


class BibtexAuthorShared:

    def __init__(self, author):
        self._author = author
        self._behaviors = {
            'GFAN': self._from_given_and_last,
            'GFA_': self._from_given_and_last,
            'GF_N': self._from_given_and_last,
            'GF__': self._from_given_and_last,
            'G_AN': self._from_given,
            'G_A_': self._from_given,
            'G__N': self._from_given,
            'G___': self._from_given,
            '_FAN': self._from_last,
            '_FA_': self._from_last,
            '_F_N': self._from_last,
            '_F__': self._from_last,
            '__AN': self._from_alias,
            '__A_': self._from_alias,
            '___N': self._from_name,
            '____': BibtexAuthorShared._from_thin_air
        }

    def _exists_nonempty(self, key):
        value = self._author.get(key, None)
        return value is not None and value != ''

    def _from_alias(self):
        return self._author.get('alias')

    def _from_given_and_last(self):
        return self._from_last() + ", " + self._from_given()

    def _from_given(self):
        return self._author.get('given-names')

    def _from_last(self):
        nameparts = [
            self._author.get('name-particle'),
            self._author.get('family-names'),
            self._author.get('name-suffix')
        ]
        return ' '.join([n for n in nameparts if n is not None])

    def _from_name(self):
        return self._author.get('name')

    @staticmethod
    def _from_thin_air():
        return None

    @abstractmethod
    def as_string(self):
        pass
