from django.db import models
from django.urls import reverse

MAX_LENGTH = 255


class Block29(models.Model):
    pri_long = models.CharField(max_length=MAX_LENGTH)
    pri_len = models.CharField(max_length=MAX_LENGTH)
    pri_desc = models.TextField()
    coll_long = models.CharField(max_length=MAX_LENGTH, blank=True, default=None)
    coll_len = models.CharField(max_length=MAX_LENGTH, blank=True, default=None)
    coll_desc = models.TextField(blank=True, default=None)
    watch = models.CharField(max_length=MAX_LENGTH, blank=True, default=None)
    watch_len = models.CharField(max_length=MAX_LENGTH, blank=True, default=None)
    umuic = models.CharField(max_length=MAX_LENGTH, default=None)
    cross = models.BooleanField(default=False)
    mob = models.CharField(max_length=MAX_LENGTH, default=None)
    pfa = models.CharField(max_length=MAX_LENGTH, blank=True, default=None)
    atadt1 = models.CharField(max_length=MAX_LENGTH, blank=True, default=None)
    atadt2 = models.CharField(max_length=MAX_LENGTH, blank=True, default=None)

    def __str__(self):
        return self.pri_long
    
    def get_absolute_url(self):
        return reverse('/block29app/')

    @staticmethod
    def format(inputs):
        inputs = {k: str(v) or None for k, v in inputs.items()}
        # Primary duty
        if inputs['pri_long'] is None or inputs['pri_len'] is None or inputs['pri_desc'] is None:
            raise ValueError("Primary duty not entered.")
        formatted = f"PRI: {inputs['pri_long']}-{inputs['pri_len']}. {inputs['pri_desc']} "
        # Collateral duty
        if inputs['coll_long'] is not None:
            formatted = formatted + f"COLL: {inputs['coll_long']}-{inputs['coll_len']}. {inputs['coll_desc']} "
        # Watch
        if inputs['watch'] is not None:
            formatted = formatted + f"WATCH: {inputs['watch']}-{inputs['watch_len']}. "
        # Mobilization
        if inputs['umuic'] is None:
            raise ValueError("UMUIC not entered.")
        if inputs['mob'] is None:
            raise ValueError("Mobilization billet not entered.")
        if inputs['cross'] == 'False':
            formatted = formatted + f"UMUIC: {inputs['umuic']}; {inputs['mob']}. "
        else:
            formatted = formatted + f"UMUIC: Cross-assigned to {inputs['umuic']}; {inputs['mob']}. "
        # PFA
        if inputs['pfa'] is not None:
            formatted = formatted + f"PFA: {inputs['pfa']}. "
        # AT/ADT
        if inputs['atadt1'] is not None:
            formatted = formatted + f"AT/ADT: {inputs['atadt1']}."
            if inputs['atadt2'] is not None:
                formatted = formatted[:-1] + f"; {inputs['atadt2']}."
        else:
            formatted = formatted + "AT/ADT: None."
        return formatted
