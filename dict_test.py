def seq_concat(a, b, **kwargs):
    """concatenate seq."""
    seq = a + b

    for key in kwargs:
        seq+= kwargs[key]

    return seq
