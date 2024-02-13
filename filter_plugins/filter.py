from __future__ import annotations

from typing import ClassVar


class FilterModule:
    STRING_CLASSES: ClassVar[list[str]] = [
        "str",
        "string",
        "AnsibleUnicode",
        "AnsibleUnsafeText",
        "AnsibleVaultEncryptedUnicode",
    ]

    def filters(self):
        return {
            "is_list": self.is_list,
            "is_ne_list": self.is_not_empty_list,
            "is_dict": self.is_dict,
            "is_dicts_list": self.is_dicts_list,
            "is_ne_dict": self.is_not_empty_dict,
            "is_string": self.is_string,
            "is_ne_string": self.is_not_empty_string,
        }

    @staticmethod
    def is_list(var, *args, **kwargs):
        return var and var.__class__.__name__ == "list"

    @staticmethod
    def is_not_empty_list(var, *args, **kwargs):
        if var and isinstance(var, list) and len(var) > 0:
            return True
        return False

    @staticmethod
    def is_dict(var, *args, **kwargs):
        return var and var.__class__.__name__ == "dict"

    @staticmethod
    def is_not_empty_dict(var, *args, **kwargs):
        return var and var.__class__.__name__ == "dict" and var != {}

    @staticmethod
    def is_dicts_list(var, *args, **kwargs):
        if not var.__class__.__name__ == "list" or len(var) == 0:
            return False

        for d in var:
            if not d.__class__.__name__ == "dict" or d == {}:
                return False

        return True

    def is_string(self, var, *args, **kwargs):
        return var and var.__class__.__name__ in self.STRING_CLASSES

    def is_not_empty_string(self, var, *args, **kwargs):
        return (
            var
            and var.__class__.__name__ in self.STRING_CLASSES
            and len(var) > 0
        )
